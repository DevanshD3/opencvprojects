import cv2
from PIL import Image
import numpy as np
print("hey you need to press '0' after every image to continue!!")
#this is the code for accessing the webcam
camera_port = 0 
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
return_value, image = camera.read()
cv2.imwrite("image.png", image)
cv2.imshow("image.png", image)

camera.release()#releases the shutter of the camera
#waits for you to press 0
cv2.waitKey(0) 
#destroys all the additional wondows created by the program
cv2.destroyAllWindows()
image= cv2.imread("image.png")
print(image)
#to invert the image
imagem = cv2.bitwise_not(image)
#to save a new inverted image
cv2.imwrite("img_inv.png",imagem)
cv2.imshow("img_inv.png", imagem)
camera.release()
cv2.waitKey(0) 
cv2.destroyAllWindows()


#to print all the types of flags/ colour conversions
# print("these are all the flags")
# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print (flags)

#to convert into RGB we use the normal PIL format to display
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
img = Image.fromarray(hsv, 'RGB')
img.save('hsv.png')
img.show()
#to convert into BGR we need to display using opencv
bgr = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
cv2.imwrite("img_bgr.png",bgr)
cv2.imshow("img_bgr.png", bgr)
camera.release()
cv2.waitKey(0) 
cv2.destroyAllWindows()
#to convert into HSL 
hls = cv2.cvtColor(image,cv2.COLOR_BGR2HLS)
cv2.imwrite("img_hsl.png",hls)
cv2.imshow("img_hsl.png", hls)
camera.release()
cv2.waitKey(0) 
cv2.destroyAllWindows()
