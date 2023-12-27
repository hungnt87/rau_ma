import pyautogui as pg
import numpy as np
import cv2 as cv
from PIL import ImageGrab, Image
import time

REGION = (0, 0, 2000, 1230)
GAME_OVER_PICTURE_PIL = None
GAME_OVER_PICTURE_CV = Image.open("./data/image/Look.jpg")
# data\image\Look.png

def install():
    global GAME_OVER_PICTURE_PIL, GAME_OVER_PICTURE_CV
    GAME_OVER_PICTURE_PIL = Image.open("./data/image/Look.jpg")
def check():
    global GAME_OVER_PICTURE_PIL, GAME_OVER_PICTURE_CV
    if GAME_OVER_PICTURE_PIL is None:
        print("Khong tim thay hinh anh")
        GAME_OVER_PICTURE_PIL = Image.open("./data/image/Look.jpg")
       
    else:
        print("Tim thay hinh anh")
if __name__ == "__main__":
   
    check()
    pass
