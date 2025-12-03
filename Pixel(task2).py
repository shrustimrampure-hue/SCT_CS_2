import cv2
import numpy as np
img=cv2.imread('E:\\internship\\pic.png')
img=cv2.resize(img,(300,600))
#split the image
b,g,r=cv2.split(img)
#cv2.imshow('blue',b) 
#cv2.imshow('green',g)
#cv2.imshow('red',r)
mr1=cv2.merge((b,g,r))
cv2.imshow('rgb',mr1)
#print('shape of image',img.shape)
#print('total number of pixels',img.size)
#print('datatype',img.dtype)
#print('image type',type(img))
cv2.imshow('orginial',img)
cv2.waitKey(0)
cv2.destroyAllWindows()