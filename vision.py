import os, pathlib
import re
import cv2 # opencv library
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as plt
import glob
from PIL import Image

UPLOAD_FOLDER = pathlib.Path(os.path.dirname(os.path.abspath(__file__)), 'uploads').as_posix()
STATIC_FOLDER = pathlib.Path(os.path.dirname(os.path.abspath(__file__)), 'static').as_posix()

def crop_image(file_name):
    car_classifier = cv2.CascadeClassifier(pathlib.Path(STATIC_FOLDER, 'haarcascade_car.xml').as_posix())
    # file_name = pathlib.Path(UPLOAD_FOLDER, 'car.jpg').as_posix()

    # if file_name.endswith('.png'):
    #     im = Image.open(file_name)
    #     im.save(file_name.split('.png')[0] + '.jpg')
    #     file_name = file_name.split('.png')[0] + '.jpg'

    img = cv2.imread(file_name)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    cars = car_classifier.detectMultiScale(gray, 1.01, 2)
    biggest = sorted(cars, key=lambda x: x[2]*x[3], reverse=True)
    corners = (biggest[0][0], biggest[0][1]), (biggest[0][0]+biggest[0][2], biggest[0][1]+biggest[0][3])

    crop = img[corners[0][1]:corners[1][1], corners[0][0]:corners[1][0]]
    # cv2.imwrite(pathlib.Path(UPLOAD_FOLDER, 'cropped.jpg').as_posix(), crop)
    return crop

    # cv2.rectangle(img, (biggest[0][0], biggest[0][1]), (biggest[0][0]+biggest[0][2], biggest[0][1]+biggest[0][3]), (0, 255, 0), 2)
    # cv2.imwrite(pathlib.Path(UPLOAD_FOLDER, 'result.jpg').as_posix(), img)

if __name__ == '__main__':
    cv2.imwrite(pathlib.Path(UPLOAD_FOLDER, 'cropped.jpg').as_posix(), crop_image(pathlib.Path(UPLOAD_FOLDER, 'car.jpg').as_posix()))