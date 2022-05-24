import cv2
import mediapipe 
from light_control import *

camera_id = 0

capture = cv2.VideoCapture(camera_id)

drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

with handsModule.Hands(static_image_mode=False, 
                       min_detection_confidence=0.7, 
                       min_tracking_confidence=0.7, 
                       max_num_hands=1) as hands:

    while True:

        ret, frame = capture.read()

        results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks != None:

            for handLandmarks in results.multi_hand_landmarks:
                
                # Thumb
                
                thumb_tip = 4
                thumb_tip_normalizedLandmark = handLandmarks.landmark[thumb_tip]
                thumb_tip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(thumb_tip_normalizedLandmark.x, thumb_tip_normalizedLandmark.y, frameWidth, frameHeight)
                
                thumb_ip = 3
                thumb_ip_normalizedLandmark = handLandmarks.landmark[thumb_ip]
                thumb_ip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(thumb_ip_normalizedLandmark.x, thumb_ip_normalizedLandmark.y, frameWidth, frameHeight)
                
                if thumb_tip_pixelCoordinatesLandmark[0] > thumb_ip_pixelCoordinatesLandmark[0]:
                    thumb_led(status=1)
                if thumb_tip_pixelCoordinatesLandmark[0] < thumb_ip_pixelCoordinatesLandmark[0]:
                    thumb_led(status=0)
                
                # Index finger
                
                index_fingertip = 8
                index_fingertip_normalizedLandmark = handLandmarks.landmark[index_fingertip]
                index_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(index_fingertip_normalizedLandmark.x, index_fingertip_normalizedLandmark.y, frameWidth, frameHeight)
                
                index_fingerpip = 6
                index_fingerpip_normalizedLandmark = handLandmarks.landmark[index_fingerpip]
                index_fingerpip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(index_fingerpip_normalizedLandmark.x, index_fingerpip_normalizedLandmark.y, frameWidth, frameHeight)
                
                if index_fingertip_pixelCoordinatesLandmark[1] < index_fingerpip_pixelCoordinatesLandmark[1]:
                    index_led(status=1)
                if index_fingertip_pixelCoordinatesLandmark[1] > index_fingerpip_pixelCoordinatesLandmark[1]:
                    index_led(status=0)
                    
                # Middle finger
                
                mid_fingertip = 12
                mid_fingertip_normalizedLandmark = handLandmarks.landmark[mid_fingertip]
                mid_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(mid_fingertip_normalizedLandmark.x, mid_fingertip_normalizedLandmark.y, frameWidth, frameHeight)
                
                mid_fingerpip = 10
                mid_fingerpip_normalizedLandmark = handLandmarks.landmark[mid_fingerpip]
                mid_fingerpip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(mid_fingerpip_normalizedLandmark.x, mid_fingerpip_normalizedLandmark.y, frameWidth, frameHeight)
                
                if mid_fingertip_pixelCoordinatesLandmark[1] < mid_fingerpip_pixelCoordinatesLandmark[1]:
                    middle_led(status=1)
                if mid_fingertip_pixelCoordinatesLandmark[1] > mid_fingerpip_pixelCoordinatesLandmark[1]:
                    middle_led(status=0)
                    
                # Ring finger
                
                ring_fingertip = 16
                ring_fingertip_normalizedLandmark = handLandmarks.landmark[ring_fingertip]
                ring_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(ring_fingertip_normalizedLandmark.x, ring_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

                ring_fingerpip = 14
                ring_fingerpip_normalizedLandmark = handLandmarks.landmark[ring_fingerpip]
                ring_fingerpip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(ring_fingerpip_normalizedLandmark.x, ring_fingerpip_normalizedLandmark.y, frameWidth, frameHeight)

                if ring_fingertip_pixelCoordinatesLandmark[1] < ring_fingerpip_pixelCoordinatesLandmark[1]:
                    ring_led(status=1)
                if ring_fingertip_pixelCoordinatesLandmark[1] > ring_fingerpip_pixelCoordinatesLandmark[1]:
                    ring_led(status=0)

                # Pinky finger
                
                pinky_fingertip = 20
                pinky_fingertip_normalizedLandmark = handLandmarks.landmark[pinky_fingertip]
                pinky_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(pinky_fingertip_normalizedLandmark.x, pinky_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

                pinky_fingerpip = 18
                pinky_fingerpip_normalizedLandmark = handLandmarks.landmark[pinky_fingerpip]
                pinky_fingerpip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(pinky_fingerpip_normalizedLandmark.x, pinky_fingerpip_normalizedLandmark.y, frameWidth, frameHeight)

                if pinky_fingertip_pixelCoordinatesLandmark[1] < pinky_fingerpip_pixelCoordinatesLandmark[1]:
                    pinky_led(status=1)
                if pinky_fingertip_pixelCoordinatesLandmark[1] > pinky_fingerpip_pixelCoordinatesLandmark[1]:
                    pinky_led(status=0)

        # if results.multi_hand_landmarks != None:
        #     GPIO.output(5, False)
        #     GPIO.output(6, False)
        #     GPIO.output(13, False)
        #     GPIO.output(19, False)
        #     GPIO.output(26, False)

        cv2.imshow('Light control', frame)
        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()
    capture.release()
    thumb_led(status=0)
    index_led(status=0)
    middle_led(status=0)
    ring_led(status=0)
    pinky_led(status=0)
