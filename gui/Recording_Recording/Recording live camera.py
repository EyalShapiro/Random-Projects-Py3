# import numpy as np
import cv2


FILE_NAME = "output.avi"


def main():
    cap = cv2.VideoCapture(0)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(FILE_NAME, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret is True:
            frame = cv2.flip(frame, 0)
            out.write(frame)

            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()

    out.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
