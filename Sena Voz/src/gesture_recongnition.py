import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils


def recognize_gesture(hand_landmarks):
    """
    Simple rule-based gesture recognition.
    You can replace this with ML later.
    """

    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb
    fingers.append(hand_landmarks.landmark[tips[0]].x <
                   hand_landmarks.landmark[tips[0]-1].x)

    # Other fingers
    for tip in tips[1:]:
        fingers.append(hand_landmarks.landmark[tip].y <
                       hand_landmarks.landmark[tip-2].y)

    if all(fingers):
        return "Hello"
    elif fingers[1] and not any(fingers[2:]):
        return "Yes"
    elif not any(fingers):
        return "No"
    else:
        return "Unknown"


def process_frame(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    gesture = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)

    return frame, gesture
