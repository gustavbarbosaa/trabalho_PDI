import cv2
import cv2 as cv
from matplotlib import pyplot as plt

imagem = cv.imread('images/images.png', 0)

ret, t1 = cv.threshold(imagem, 127, 255, cv.THRESH_BINARY)
ret, t2 = cv.threshold(imagem, 127, 255, cv.THRESH_BINARY_INV)
ret, t3 = cv.threshold(imagem, 127, 255, cv.THRESH_TRUNC)
ret, t4 = cv.threshold(imagem, 127, 255, cv.THRESH_TOZERO)

titulos = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
imagens = [imagem, t1, t2, t3, t4]

for i in range(5):

    plt.subplot(2, 3, i + 1), plt.imshow(imagens[i], 'gray', vmin=0, vmax=255)
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

cv2.imwrite('images/t1.jpg', t1)
cv2.imwrite('images/t2.jpg', t2)
cv2.imwrite('images/t3.jpg', t3)
cv2.imwrite('images/t4.jpg', t4)
plt.show()

