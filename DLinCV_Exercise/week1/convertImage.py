import cv2

# Load an color image
img = cv2.imread('../images/pencils.png')

cv2.imshow('Origin Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#convert img to grayscale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#save converted gray image to file
outputFileName = 'pencils_gray.png'
cv2.imwrite(outputFileName,img_gray)

#reload gray image
img_gray = cv2.imread(outputFileName)
cv2.imshow('Converted Image',img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
