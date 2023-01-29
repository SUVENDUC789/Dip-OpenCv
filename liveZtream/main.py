import cv2
import time

cap = cv2.VideoCapture(0)


if (cap.isOpened() == False):
    print('Unaable to open camera feed')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(
    'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))


# while (True):

mytime = int(input('Enter time in second : '))


for x in range(mytime, 0, -1):
    # second = x % 60
    # minute = int(x/60) % 60
    # hour = int(x/3600)
    # print(f'{hour:02} : {minute:02} : {second:02} ')

    ret, frame = cap.read()

    if ret == True:
        cv2.flip(frame, 180)
        out.write(frame)
        # cv2.imshow('Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    # time.sleep(1)




cap.release()
cv2.destroyAllWindows()
