import cv2
#p1
img_bgr = cv2.imread('images/variant-8.jpeg')
assert img_bgr is not None, "file could not be read, check with os.path.exists()"

img_h, img_w = img_bgr.shape[:2]

cropped = img_bgr[((img_h//2)-200):((img_h//2)+200), ((img_w//2)-200):((img_w//2)+200)]

cv2.imwrite('cropped.jpg', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()