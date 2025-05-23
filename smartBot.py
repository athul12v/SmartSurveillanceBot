import cv2
import torch
import time
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
import asyncio
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

# Initialize camera (0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera is available
if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5s for faster inference

TARGET_CLASSES = ['person', 'cat', 'dog', 'car']
PERSON_CLASS = 'person'

last_detection_time = time.time()
DETECTION_INTERVAL = 5  # seconds

if not os.path.exists('captures'):
    os.makedirs('captures')

# Send a Telegram notification with the captured image
async def send_telegram_notification(message, image_path):
    try:
        # Send message
        await application.bot.send_message(chat_id=CHAT_ID, text=message)

        # Send photo
        with open(image_path, 'rb') as image_file:
            await application.bot.send_photo(chat_id=CHAT_ID, photo=image_file)

        print(f"Telegram notification sent: {message}")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")

# Function for detecting objects and sending notifications
async def detect_and_notify():
    global last_detection_time
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        results = model(frame)

        results.render()

        output_frame = results.ims[0]

        # Loop through the detections in the frame
        for idx, conf, bbox in zip(results.xyxy[0][:, -1], results.xyxy[0][:, -2], results.xyxy[0][:, :-2]):
            class_name = model.names[int(idx)]  # Get the class name (person, dog, etc.)
            
            # Check if the object belongs to the target classes
            if class_name in TARGET_CLASSES:
                current_time = time.time()

                # Only send notifications if enough time has passed (avoid spam)
                if current_time - last_detection_time > DETECTION_INTERVAL:
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    filename = f"captures/captured_{class_name}_{timestamp}.jpg"
                    cv2.imwrite(filename, output_frame)  # Save the image with bounding boxes

                    # Special case for "person"
                    if class_name == PERSON_CLASS:
                        message = f"A person was detected at {timestamp}. Image saved."
                    else:
                        message = f"Object detected: {class_name} at {timestamp}. Image saved."
                    
                    # Send Telegram notification with the captured image
                    await send_telegram_notification(message, filename)

                    # Update last detection time
                    last_detection_time = current_time

        # Display the frame with bounding boxes
        cv2.imshow("Object Detection", output_frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

async def handle_image(update: Update, context):
    user_id = update.message.from_user.id  # Get the user ID
    file = await update.message.photo[-1].get_file()  # Get the photo file sent by the user
    file_path = f'captures/user_image_{user_id}.jpg'
    await file.download(file_path)  # Save the received image

    # Send a reply to the user
    await update.message.reply_text(f"Received your image! Someone detected!")

    with open(file_path, 'rb') as image_file:
        await update.message.reply_photo(photo=image_file)

# Add the image handler to the application
application.add_handler(MessageHandler(filters.PHOTO, handle_image))

async def main():
    # Start the object detection and notification loop
    await detect_and_notify()

if __name__ == '__main__':
    asyncio.run(main())
