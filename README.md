# Smart Surveillance: Object Detection & Telegram Notifier

A real-time object detection system that leverages YOLOv5 to identify specific objects (like people, cats, dogs, and cars) from a live camera feed and sends instant notifications, along with a captured image, to a Telegram chat. The system also includes a Telegram bot that can receive images from users.

---

## ✨ Features

- **Real-time Object Detection**: Continuously monitors a live camera feed for predefined objects.
- **YOLOv5 Integration**: Utilizes the powerful YOLOv5 model for accurate and fast object recognition.
- **Configurable Target Classes**: Easily specify which objects you want to detect (e.g., person, cat, dog, car).
- **Intelligent Notification System**: Sends Telegram notifications only after a specified interval to prevent spam.
- **Image Capture & Sharing**: Saves detected object frames with bounding boxes and sends them directly to your Telegram chat.
- **Telegram Bot Interaction**: A Telegram bot that can receive images from users and provide a simple acknowledgment.
- **Easy Setup**: Minimal configuration required to get started.

---

## 🚀 Technologies Used

| Technology                | Description                                           | Icon                                   |
|--------------------------|-------------------------------------------------------|----------------------------------------|
| **Python**               | The core programming language for the application.    | ![Python](https://img.icons8.com/color/48/000000/python.png) |
| **OpenCV (cv2)**        | Library for computer vision and image processing.      | ![OpenCV](https://img.icons8.com/color/48/000000/opencv.png) |
| **PyTorch (torch)**     | Deep learning framework for building neural networks.  | ![PyTorch](https://img.icons8.com/color/48/000000/pytorch.png) |
| **YOLOv5 (Ultralytics)**| State-of-the-art object detection model.               | ![YOLO](https://img.icons8.com/color/48/000000/yolo.png) |
| **python-telegram-bot** | Library for interacting with the Telegram Bot API.    | ![Telegram](https://img.icons8.com/color/48/000000/telegram-app.png) |
| **python-dotenv**       | Tool for managing environment variables.                | ![Dotenv](https://img.icons8.com/color/48/000000/dotenv.png) |

---

## 🏗️ Architecture

The system operates with a straightforward architecture, designed for real-time processing and efficient notification.

### Conceptual Flow:
1. **Camera Feed**: The system continuously captures frames from a connected webcam.
2. **Object Detection (YOLOv5)**: Each captured frame is fed into the pre-trained YOLOv5 model.
3. **Filtering & Analysis**: The model's detections are filtered to identify only the `TARGET_CLASSES`. A time-based debounce mechanism prevents excessive notifications.
4. **Image Capture**: If a target object is detected and the notification interval has passed, the frame (with bounding boxes drawn) is saved locally.
5. **Telegram Notification**: A message, along with the captured image, is sent to your configured Telegram chat ID.
6. **Telegram Bot Listener**: Separately, the Telegram bot listens for incoming messages, specifically photos, and responds accordingly.

[![Architecture Diagram](https://via.placeholder.com/800x400?text=Architecture+Diagram)](https://github.com/your-username/smart-surveillance)

---

## ⚙️ Setup and Installation

Follow these steps to get your Smart Surveillance system up and running.

### Prerequisites
- Python 3.8+
- A webcam connected to your system.
- A Telegram account.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/smart-surveillance.git
cd smart-surveillance
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
_(You'll need to create a requirements.txt file based on the provided code. It should contain: opencv-python, torch, ultralytics/yolov5, python-telegram-bot, python-dotenv.)_

### 4. Configure Environment Variables
Create a .env file in the root directory of your project:
```bash
TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID="YOUR_TELEGRAM_CHAT_ID"
```

#### How to get YOUR_TELEGRAM_BOT_TOKEN:
- Open Telegram and search for @BotFather.
- Start a chat with BotFather and send /newbot.
- Follow the instructions to choose a name and username for your bot.
- BotFather will provide you with an API Token. Copy this token and paste it into your .env file.

#### How to get YOUR_TELEGRAM_CHAT_ID:
- Start a conversation with your newly created bot in Telegram.
- Send any message to your bot.
- Open your web browser and go to:
```bash
https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/getUpdates
```
- Look for the chat object in the JSON response. The id field within this object is your CHAT_ID. Copy this ID and paste it into your .env file.

---

## ▶️ Usage

Once everything is set up, you can run the main script:
```bash
python your_main_script_name.py
```

### What to Expect:
- A window titled "Object Detection" will appear, displaying the live camera feed with bounding boxes around detected objects.
- When a TARGET_CLASS object is detected, and the DETECTION_INTERVAL has passed, a notification and an image will be sent to your Telegram chat.
- You can press `q` on the "Object Detection" window to quit the application.
- You can send images to your Telegram bot, and it will acknowledge receipt.

---

## 🔧 Customization

You can easily customize the detection behavior by modifying the following variables in the script:

- **TARGET_CLASSES**: A list of strings representing the object classes you want to detect.
```python
TARGET_CLASSES = ['person', 'cat', 'dog', 'car']
```

- **DETECTION_INTERVAL**: The minimum time (in seconds) between sending notifications for new detections. This prevents notification spam.
```python
DETECTION_INTERVAL = 5  # seconds
```

- **Camera Selection**: If you have multiple cameras, you might need to change `cap = cv2.VideoCapture(0)` to `1`, `2`, etc., to select a different camera.

---

## 💡 Future Enhancements

- **Customizable Notification Messages**: Allow users to define their own notification message templates.
- **Multiple Camera Support**: Extend to monitor multiple camera feeds simultaneously.
- **Web Interface**: Develop a simple web interface for configuration and viewing detection history.
- **Cloud Storage**: Option to upload captured images to cloud storage (e.g., Google Cloud Storage, AWS S3) instead of local storage.
- **Advanced Alerting**: Integrate with other notification services (e.g., email, SMS).
- **Time-based Scheduling**: Allow users to schedule when the detection system should be active.
- **Motion Detection Pre-filter**: Use basic motion detection to trigger YOLOv5 inference only when movement is detected, saving resources.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute code, please feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License** - a permissive license that allows for flexible usage, modification, and distribution. For more details, check out the full [LICENSE](LICENSE) file.

---

## 📱 Let's Connect!

I love collaborating, sharing knowledge, and connecting with like-minded individuals. Feel free to reach out to me through any of the following platforms:

- 🌟 **[LinkedIn](https://www.linkedin.com/in/v-athul/)** – Connect with me professionally and view my latest career updates.
- 🐦 **[Twitter](https://x.com/AthulViswanthan)** – Follow me for updates, tech insights, and occasional musings.
- 🧑‍💻 **[GitHub](https://github.com/athul12v)** – Explore my repositories, open-source projects, and contributions to the community.

Let's grow together! 🚀

---
# SmartSurveillanceBot
