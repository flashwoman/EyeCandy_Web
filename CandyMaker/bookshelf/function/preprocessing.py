import cv2 as cv
import numpy as np


# def preprocessing(img_color, m=11, n=2):
# #
# #
# #     ## 1. 세로로 세워진 책들 색 균등화
# #     #  vertical kernel
# #     kernel = np.ones((m, n), np.uint8)
# #     # morphologyEx
# #     kernel_opening = cv.morphologyEx(img_color.copy(), cv.MORPH_OPEN, kernel, iterations=2)
# #
# #     # sure_bg = cv.dilate(opening, kernel, iterations=3)
# #     # display('1st_opening', kernel_opening)
# #
# #     gray = cv.cvtColor(kernel_opening, cv.COLOR_BGR2GRAY)
# #     # display('gray', gray)
# #
# #     ret, thresh = cv.threshold(gray, 10, 255, cv.THRESH_TOZERO)
# #     # display('thresh', thresh)
# #
# #     ## 2. 책 사이 간격 벌리기
# #     kernel_s = np.ones((2,1), np.uint8)
# #     erode = cv.morphologyEx(gray, cv.MORPH_ERODE, kernel_s, iterations=2)
# #     # display('eroding for gap', erode)
# #
# #     return erode

# import cv2 as cv
# import os
# import glob
# from .display import display
#
#######countours
# def contours(img_book_only, img_color):
#
#     img_for_save = img_color.copy()
#
#     # 1. Threshold
#     ret, img_binary = cv.threshold(img_book_only, 127, 255, 0)
#     # display("img_binary", img_binary)
#
#     # 2. Contour 찾기
#     contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#
#     # 3. 기존에 저장된 이미지 파일 삭제
#     path = "C:/flashwoman/Object-detection/image/result/"
#     files = '*.jpg'  # 찾고 싶은 확장자
#     for file in glob.glob(os.path.join(path, files)):
#         os.remove(file)
#
#     ## 4. countour 그리고 저장하기.
#     count = 0
#     rect = []
#     for cnt in contours:
#         ## 1.  사각형 만들어 좌표얻기.
#         x, y, w, h = cv.boundingRect(cnt)
#         cv.rectangle(img_color, (x, y), (x + w, y + h), (3, 255, 4), 2)  # contour 그리기
#         rect.append([(x, y), (x + w, y + h)])  # rect에 좌표 저장 [Left_Top, Right_Bottom]
#
#         ## 2. 각각의 책 이미지 저장 ##
#         img_result = img_for_save[y: y + h, x: x + w]
#         img_path = f"C:/flashwoman/Object-detection/image/result/book/img{count}.jpg"
#         cv.imwrite(img_path, img_result)
#
#         count = count + 1
#
#     path = "C:/flashwoman/Object-detection/image/result/result.jpg"
#     # display("result", img_color)
#     cv.imwrite(path, img_color)
#
#
#     return img_book_only, rect
#


def display(winname, img):

    cv.moveWindow(winname, 500, 0)
    cv.namedWindow(winname, cv.WINDOW_NORMAL)
    cv.imshow(winname, img)
    cv.waitKey(0)

img_color = cv.imread('C:/Flashwoman/CandyMaker/img/masks/test1_mask.jpg')
# display('img_color', img_color)
## 1. 세로로 세워진 책들 색 균등화
#  vertical kernel
kernel = np.ones((11, 2), np.uint8)
# kernel = np.ones(m, n), np.uint8)


# morphologyEx
kernel_opening = cv.morphologyEx(img_color.copy(), cv.MORPH_OPEN, kernel, iterations=2)
#
display('kernel_opening', kernel_opening)

# # sure_bg = cv.dilate(opening, kernel, iterations=3)
# # display('1st_opening', kernel_opening)
#
# gray = cv.cvtColor(kernel_opening, cv.COLOR_BGR2GRAY)
# # display('gray', gray)
#
# ret, thresh = cv.threshold(gray, 10, 255, cv.THRESH_TOZERO)
# # display('thresh', thresh)
#
# ## 2. 책 사이 간격 벌리기
# kernel_s = np.ones((2,1), np.uint8)
# erode = cv.morphologyEx(gray, cv.MORPH_ERODE, kernel_s, iterations=2)