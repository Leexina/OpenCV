import cv2 as cv

img = cv.imread('D:\Python\Python project\OpenCV\cat.jpg')
print(img)
cv.imshow("cat",img)
cv.waitKey(0)    
cv.destroyAllWindows() 
print(img.shape[0])
print(img.shape[1])
print(img.shape[2])
print(img.shape[:2])
print(img.shape[:3])