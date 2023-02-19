from tkinter import *
from tkinter import ttk
from deepface import DeepFace as dp
import cv2
import matplotlib.pyplot as ppt
import uuid
import os

root = Tk()
root.geometry('500x500')
root.title("Musical Recognition")


def picture():
    REAL_PATH = os.path.join('data', 'tests')
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        ret, frame = capture.read()

        frame = frame[100:100+250,200:200+250,:]

        if cv2.waitKey(1) & 0XFF == ord('c'):
            imgname = os.path.join(REAL_PATH, '{}.jpg'.format(uuid.uuid1()))
            cv2.imwrite(imgname,frame)
            break;

        cv2.imshow('Image Collection', frame)
        # if cv2.waitKey(1) & 0XFF == ord('q'):
        #     break
    capture.release()
    cv2.destroyAllWindows()

    i_path = imgname

    img = cv2.imread(i_path)

    demo = dp.analyze(i_path, enforce_detection=False)
    demo

    main_emotion = demo[0]['dominant_emotion']  
    if main_emotion == 'discust':
        print("No time for music! Your main emotion is " + main_emotion +  " Go exercise.")
    else:
        print("Your main emotion was " + main_emotion)

def login():
    b1 = ttk.Button(frm, text="Take Picture", command= picture).grid(column=2, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=7)

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Musical Recognition").grid(column=0, row=0)

b0=ttk.Button(frm, text = "Login", command = login).grid(column=2, row=1)


root.mainloop()