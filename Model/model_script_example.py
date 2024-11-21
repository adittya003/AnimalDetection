from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO('wild_boar.pt')


video_path = 'wld boar.mp4'  
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()


while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Run YOLO prediction on the current frame
    results = model.predict(source=frame, conf=0.5, show=True)  # Adjust confidence threshold as needed

    # Display the processed frame with detections
    cv2.imshow('YOLO Detection', frame)

    # Press 'q' to exit the video early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
