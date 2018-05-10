import cv2

#load image from file
img = cv2.imread('../images/pencils.png')
#resize image
scaled_image = cv2.resize(img,(256,256))
#show resize image
cv2.imshow('resize image',scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#save resize image to file
cv2.imwrite('pencils_256x256.png',scaled_image)

#load image from file
img = cv2.imread('pencils_gray.png')
#resize image
scaled_image = cv2.resize(img,(256,256))
#show resize image
cv2.imshow('resize image',scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#save resize image to file
cv2.imwrite('pencils_gray_256x256.png',scaled_image)
