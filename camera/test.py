# camera_test.py
import cv2

print("Testing camera...")

# Try camera 0 (laptop webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera 0 not found, trying camera 1...")
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("❌ Camera 1 not found, trying camera 2...")
        cap = cv2.VideoCapture(2)

if not cap.isOpened():
    print("❌ No camera found! Check:")
    print("   - Is your webcam plugged in?")
    print("   - Is your laptop camera enabled?")
    print("   - Try closing other apps using camera (Zoom, Teams, etc.)")
    exit()

print("✅ Camera opened successfully!")
print(f"   Camera ID: {cap.get(cv2.CAP_PROP_BACKEND)}")
print(f"   Width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"   Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print("\nPress 'q' to quit\n")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    # Show the frame
    cv2.imshow('Camera Test', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Camera test complete!")
