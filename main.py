from model import *
import cv2
import os


model = URetinex_Net()
for im_name in os.listdir('demo/inputs/'):
    img = cv2.imread('demo/inputs/'+im_name)
    im_shape = (img.shape[1]//16*16, img.shape[0]//16*16)
    img = cv2.resize(img, im_shape)
    out = model.run(img)
    cv2.imwrite('demo/outputs/URetinex_Net/'+im_name,out)
