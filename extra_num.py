import cv2
import numpy as np

def video_processing():
    cap = cv2.VideoCapture(0)

    fly_img = cv2.imread('images/fly64.png')
    flyH, flyW = fly_img.shape[:2]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        height, width = frame.shape[:2]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (9, 9), 0)

        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100, param1=80, param2=40, minRadius=30, maxRadius=250)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            x, y, r = circles[0, 0]

            fly_x1 = x - (flyW // 2)
            fly_x2 = fly_x1 + flyH
            fly_y1 = y - (flyH // 2)
            fly_y2 = fly_y1 + flyH

            if 0 <= fly_x1 < width and 0 <= fly_y1 < height and fly_x2 < width and fly_y2 < height:
                fly_region = frame[fly_y1:fly_y2, fly_x1:fly_x2]

                if fly_img.shape[2] == 4:
                    alpha_ch = fly_img[:, :, 3] / 255.0
                    for ch in range(3):
                        fly_region[:, :, ch] = (1 - alpha_ch) * fly_region[:, :, ch] + alpha_ch * fly_img[:, :,ch]
                else:
                    frame[fly_y1:fly_y2, fly_x1:fly_x2] = fly_img

            print(f"Координаты центра: ({x}, {y})")

        cv2.imshow('Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


video_processing()