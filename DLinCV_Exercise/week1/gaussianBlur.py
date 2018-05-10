import cv2
img = cv2.imread('../images/pencils.png')
#blur image by kennel size
kernelBlurImg = cv2.GaussianBlur(img, (15, 15), 0)
#blur image by sigma X
xSigmaBlurImg = cv2.GaussianBlur(img,(0,0),5)

#show image
cv2.imshow('original image',img)
cv2.imshow('kernel blur image', kernelBlurImg)
cv2.imshow('sigma x blur image', xSigmaBlurImg)
cv2.waitKey(0)
cv2.destroyAllWindows()