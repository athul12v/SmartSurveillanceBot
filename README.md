# Next-Gen Smart Surveillance | Real-Time Object Detection + Telegram Alert System

A sleek, real-time surveillance system built with **Streamlit** and **YOLOv5**, enabling live object detection through your webcam. It captures images of detected objects (like people, cats, dogs, cars) and sends instant alerts with snapshots to your Telegram chat — all wrapped in an intuitive, responsive web UI that looks and feels like a smart surveillance console.

---

## ✨ Features

- **Real-time Detection with Webcam**: Monitor live video feed and detect objects continuously.
- **YOLOv5 Model Integration**: Utilizes the fast and accurate YOLOv5s pre-trained model.
- **Configurable Target Objects**: Detects multiple objects, focusing on key targets like people, cats, dogs, and cars.
- **Telegram Notifications with Cooldown**: Sends image alerts to Telegram only after a cooldown period to prevent spamming.
- **Captured Image Storage**: Saves cropped detected object images locally with timestamped filenames.
- **Interactive Streamlit Dashboard**: Start/Stop monitoring with clear UI feedback, live video display with bounding boxes, and alert messages.
- **Robust Error Handling**: Handles webcam connection issues and Telegram notification failures gracefully.
- **Easy Setup & Deployment**: Lightweight dependencies and minimal configuration for quick start.

---

## 🚀 Tech Stack

| Technology                | Description                                      | Icon                                   |
|--------------------------|-------------------------------------------------|----------------------------------------|
| **Python**               | Core programming language                        | ![Python](https://img.icons8.com/color/48/000000/python.png) |
| **Streamlit**            | Interactive web app framework                    | ![Streamlit](https://img.icons8.com/color/48/000000/streamlit.png) |
| **OpenCV**               | Real-time computer vision                        | ![OpenCV](https://img.icons8.com/color/48/000000/opencv.png) |
| **PyTorch**              | Deep learning model loading and inference       | ![PyTorch](https://img.icons8.com/color/48/000000/pytorch.png) |
| **YOLOv5 (Ultralytics)** | State-of-the-art object detection                | ![YOLO](https://img.icons8.com/color/48/000000/yolo.png) |
| **Requests**             | HTTP requests for Telegram API integration      | ![Requests](https://img.icons8.com/color/48/000000/api-settings.png) |

---

## 🏗️ Architecture Overview

### Workflow:

1. **Start Monitoring**: User clicks the button to open the webcam feed.
2. **Frame Capture & Detection**: Frames are read in real-time and passed through YOLOv5.
3. **Object Filtering**: Only detections above confidence threshold and matching target classes are processed.
4. **Bounding Box Overlay**: Detected objects are marked visually on the live feed.
5. **Image Capture & Notification**: When a target (e.g., person) is detected and cooldown elapsed, a cropped image is saved and sent via Telegram.
6. **Stop Monitoring**: User can stop the feed to release resources gracefully.

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.8+
- A webcam connected and accessible
- Telegram account and bot token

### Steps

1. **Clone the repo**

```bash
git clone https://github.com/athul12v/smart-surveillance.git
cd SmartSurveillanBot
```

2. **Create & activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

*Example requirements.txt includes:*

```
streamlit
torch
opencv-python
requests
```

4. **Configure environment variables**

Create a `.env` file in project root:

```env
BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID="YOUR_TELEGRAM_CHAT_ID"
```

5. **Run the app**

```bash
streamlit run your_script_name.py
```

Open the URL printed by Streamlit in your browser to interact with the smart surveillance UI.

---

## ▶️ Usage Guide

* Click **Start Monitoring** to begin object detection via webcam.
* Watch the live feed on the dashboard with bounding boxes drawn.
* Receive Telegram alerts with images whenever your target objects are detected.
* Click **Stop Monitoring** to safely close the webcam and stop processing.
* Alerts won’t spam thanks to cooldown timers between notifications.
* Clear on-screen messages will inform you of detection status or errors.

---

## 🔧 Customization Options

* **Target Classes**: Change or add classes in the code (`'person'`, `'cat'`, `'dog'`, `'car'`).
* **Confidence Threshold**: Adjust minimum detection confidence (currently 0.5).
* **Alert Cooldown**: Modify cooldown seconds (default 30s) to tune notification frequency.
* **Camera Source**: Change the camera index in OpenCV capture for multiple webcams.

---

## 💡 Future Enhancements

* Add multi-camera support and switch camera feeds dynamically.
* Integrate motion detection as a pre-filter to optimize resource usage.
* Implement alert history and dashboard analytics.
* Allow configuring notification message templates via UI.
* Store captured images to cloud for remote access.
* Support additional notification channels like email or SMS.
* Enable scheduling and automatic start/stop times.

---

## 🤝 Contributing

We welcome all kinds of contributions — whether it's fixing bugs, improving documentation, adding features, or optimizing the codebase.

**How you can contribute:**

1. **Report Bugs**  
   Found an issue? Please open a detailed issue on GitHub so we can fix it quickly.

2. **Request Features**  
   Have an idea to make the project better? Submit a feature request with a clear description and use cases.

3. **Submit Pull Requests**  
   - Fork the repository  
   - Create a new branch (`git checkout -b feature/YourFeature`)  
   - Make your changes and commit with clear messages  
   - Push to your fork and submit a PR against the main branch  
   
   We’ll review your contribution and provide feedback if needed.

4. **Improve Documentation**  
   Clear documentation helps everyone! Feel free to suggest enhancements or fix typos.

5. **Spread the Word**  
   Share the project with your network to help us grow the community.

**Contribution Guidelines:**

- Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) coding standards for Python code.
- Write clean, readable, and well-commented code.
- Test your changes thoroughly.
- Keep pull requests focused and concise.
---

## 📱 Let’s Connect — I’m Just One Click Away!

<div align="center" style="margin-top: 10px; margin-bottom: 10px;">

[![LinkedIn](https://img.icons8.com/ios-filled/40/0077B5/linkedin.png)](https://www.linkedin.com/in/v-athul/) &nbsp;&nbsp;&nbsp;
[![Twitter](https://img.icons8.com/ios-filled/40/1DA1F2/twitter.png)](https://x.com/AthulViswanthan) &nbsp;&nbsp;&nbsp;
[![GitHub](https://img.icons8.com/ios-glyphs/30/ffffff/github.png)](https://github.com/athul12v)

</div>

> **Let's build the future of smart surveillance — together!**  
> _Reach out anytime for collaborations, ideas, or a quick hello._


---
