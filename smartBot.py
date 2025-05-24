import streamlit as st
import torch
import cv2
import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv

# ---- UI Setup ----
st.set_page_config(page_title="Smart Surveillance", layout="wide")

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    st.error("❌ BOT_TOKEN or CHAT_ID is not set. Please check your configuration.")

CAPTURE_FOLDER = "capture"
ALERT_COOLDOWN = 30  # seconds
os.makedirs(CAPTURE_FOLDER, exist_ok=True)

@st.cache_resource
def load_model():
    return torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model = load_model()

# Initialize session state
if "monitoring" not in st.session_state:
    st.session_state.monitoring = False
if "alert_sent_time" not in st.session_state:
    st.session_state.alert_sent_time = 0
if "cap" not in st.session_state:
    st.session_state.cap = None
if "alert_images" not in st.session_state:
    st.session_state.alert_images = []  # Store alert image paths for gallery

# Custom CSS for dark theme and styles
st.markdown(
    """
    <style>
    .css-18e3th9 { padding-top: 1rem; }
    .big-font { font-size:22px !important; font-weight: 700; }
    .status-ok { color: #00ff00; font-weight: 600; }
    .status-alert { color: #ff4c4c; font-weight: 700; }
    .alert-thumb { border-radius: 8px; margin: 5px; box-shadow: 0 0 8px rgba(255, 76, 76, 0.7); }
    .title-container { display: flex; align-items: center; justify-content: space-between; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📹 Smart Surveillance System")

def send_telegram_alert(img_path):
    try:
        caption = f"🚨 Person detected at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        with open(img_path, "rb") as f:
            files = {"photo": f}
            data = {"chat_id": CHAT_ID, "caption": caption}
            resp = requests.post(url, data=data, files=files)
            print("Telegram response:", resp.status_code, resp.text)
            return resp.status_code == 200
    except Exception as e:
        print("Telegram alert failed:", str(e))
        return False

def start_monitoring():
    if st.session_state.cap is None:
        st.session_state.cap = cv2.VideoCapture(0)
    st.session_state.monitoring = True

def stop_monitoring():
    if st.session_state.cap is not None:
        st.session_state.cap.release()
        st.session_state.cap = None
    st.session_state.monitoring = False

# --- Control Buttons ---
col1, col2 = st.columns([1,1])
with col1:
    if st.button("▶️ Start Monitoring", key="start_btn") and not st.session_state.monitoring:
        start_monitoring()
with col2:
    if st.button("⏹ Stop Monitoring", key="stop_btn") and st.session_state.monitoring:
        stop_monitoring()

# --- Layout ---
frame_col, info_col = st.columns([3,1])
frame_placeholder = frame_col.empty()
alert_placeholder = st.empty()
log_container = info_col.container()
alert_gallery = info_col.container()

# --- Monitoring Loop ---
if st.session_state.monitoring:
    cap = st.session_state.cap
    if cap is None or not cap.isOpened():
        st.error("⚠️ Cannot open webcam")
        stop_monitoring()
    else:
        for _ in range(1000):
            if not st.session_state.monitoring:
                break

            ret, frame = cap.read()
            if not ret:
                st.error("⚠️ Failed to grab frame")
                break

            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = model(img_rgb)
            df = results.pandas().xyxy[0]

            person_detected = False
            alert_sent_this_frame = False

            for _, row in df.iterrows():
                label = row['name']
                conf = row['confidence']
                if conf < 0.5:
                    continue

                x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(frame.shape[1]-1, x2), min(frame.shape[0]-1, y2)

                crop_img = frame[y1:y2, x1:x2]
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
                filename = f"{label}_{timestamp}.jpg"
                filepath = os.path.join(CAPTURE_FOLDER, filename)
                cv2.imwrite(filepath, crop_img)
                time.sleep(0.05)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                if label == "person":
                    person_detected = True
                    current_time = time.time()
                    if current_time - st.session_state.alert_sent_time > ALERT_COOLDOWN:
                        sent = send_telegram_alert(filepath)
                        if sent:
                            alert_placeholder.success(f"📸 Telegram alert sent: {filename}")
                            st.session_state.alert_sent_time = current_time
                            alert_sent_this_frame = True

                            # Add to alert gallery (keep only last 6)
                            st.session_state.alert_images.insert(0, filepath)
                            if len(st.session_state.alert_images) > 6:
                                st.session_state.alert_images.pop()
                        else:
                            alert_placeholder.error("❌ Failed to send Telegram alert.")

            # Display live frame with bounding boxes
            frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)

            # Update detection log
            status_text = (
                f"<span class='status-alert'>🚨 Person Detected</span>"
                if person_detected else
                f"<span class='status-ok'>✅ Clear</span>"
            )
            log_container.markdown(
                f"**🕒 {datetime.now().strftime('%H:%M:%S')}** – {status_text}",
                unsafe_allow_html=True
            )

            # Show alert thumbnails
            with alert_gallery:
                st.markdown("### Recent Alerts")
                if st.session_state.alert_images:
                    cols = st.columns(len(st.session_state.alert_images))
                    for i, img_path in enumerate(st.session_state.alert_images):
                        cols[i].image(img_path, width=100, caption=os.path.basename(img_path), use_column_width=False,
                                      output_format='JPEG')

            time.sleep(0.1)

        stop_monitoring()

else:
    st.info("▶️ Press 'Start Monitoring' to begin detection.")
