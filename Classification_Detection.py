import cv2
import torch
from ultralytics import YOLO

# Load the models
classification_model = YOLO("models/classification_model.pt")
detection_model = YOLO("models/detection_model.pt")
# Classify the fruit type
def classify_fruit(image):
    result = classification_model(image)
    
    class_id = torch.argmax(result[0].probs.data)
    class_label = classification_model.names[class_id.item()]
    
    confidence = result[0].probs.data[class_id].item()
    
    print(f"[INFO] Classified Fruit: {class_label} (Confidence: {confidence:.2f})")
    
    return class_label

# Detect if the fruit is rotten or healthy
def detect_rotten_or_healthy(image, class_label):
    result = detection_model(image)
    
    print(f"[INFO] Detection Model Result: {result}")

    # Debugging: Check detection model output, print all boxes and classes
    if result[0].boxes is not None and len(result[0].boxes) > 0:
        print(f"[DEBUG] Detection model found {len(result[0].boxes)} boxes.")
        for box in result[0].boxes:
            cls = int(box.cls)
            confidence = box.conf.item()
            print(f"[DETECTION] Detected Class: {cls}, Confidence: {confidence:.2f}")  # For debugging
            
            # Here we need to be sure the class_label matches the fruit
            # You can check class_label.lower() == "banana" as an example
            print(f"[DEBUG] Matching classified label '{class_label.lower()}' with detection class {cls}...")

            # You can map cls (0, 1, etc.) to actual labels for easier debugging
            if class_label.lower() in ["banana", "apple", "mango", "orange"]:  # Add other fruits as needed
                if confidence > 0.5:  # Confidence threshold
                    if cls == 0:  # Assuming 0 = rotten
                        return "rotten"
                    elif cls == 1:  # Assuming 1 = healthy
                        return "healthy"
    else:
        print(f"[DEBUG] No boxes detected in the frame for {class_label}")

    # Default to unknown if no valid detection
    return "Ripe"

# Open the video stream (camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Classify the fruit type
    class_label = classify_fruit(frame)
    
    # Step 2: Detect the fruit quality (rotten or healthy)
    status = detect_rotten_or_healthy(frame, class_label)
    
    # Terminal output for detection
    print(f"[INFO] Fruit Quality: {status}")
    print("-" * 50)
    
    # Display classification and detection results on the frame
    cv2.putText(frame, f"Fruit: {class_label}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f"Quality: {status}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the frame with the results
    cv2.imshow("Classification and Detection", frame)

    # Exit condition (press 'q' to quit the loop)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
