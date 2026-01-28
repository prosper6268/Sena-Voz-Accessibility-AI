import cv2
from src.gesture_recognition import process_frame
from src.audio_output import speak
from src.learning_module import show_learning_mode

print("Sena Voz – Sign Language Gesture Communication")
print("1. Communication Mode")
print("2. Learning Mode")

choice = input("Enter choice (1/2): ")

if choice == "2":
    show_learning_mode()
    exit()

cap = cv2.VideoCapture(0)
last_gesture = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, gesture = process_frame(frame)

    if gesture and gesture != last_gesture:
        speak(gesture)
        last_gesture = gesture

    if gesture:
        cv2.putText(frame, f"Gesture: {gesture}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Sena Voz - Communication Mode", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
