import cv2

def show_learning_mode():
    cap = cv2.VideoCapture(0)

    instructions = [
        "Open Palm - Hello",
        "Index Finger - Yes",
        "Closed Fist - No"
    ]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        y = 50
        for text in instructions:
            cv2.putText(frame, text, (20, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            y += 40

        cv2.imshow("Learning Mode - Press Q to Exit", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
