import cv2

image = cv2.imread("pika.png")

if image is None:
    print("Error, image not found")
    exit()

cv2.imshow("Original Image", image)

cv2.imwrite("saved_image.jpg", image)

grayimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray Scale", grayimage)

cv2.waitKey(0)
cv2.destroyAllWindows()