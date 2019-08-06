import os
import cv2 as cv
from django.shortcuts import render,redirect
from django.conf import settings
from CandyMaker.bookshelf.function.contours import contours
from CandyMaker.bookshelf.function.preprocessing import preprocessing

# from django.conf import settings

def startmaker(request, param):
    # 0. get params : 2+ 이미지 full 주소 + pk
    #row = int(param.split('+')[0])
    row = 4
    img_url = param.split('+')[1]
    pk = int(param.split('+')[2])

    print(row, img_url, pk )

    ############################## 시연을 위한 로직 : mask를 찾기 위함 (html에 opencv window 출력 불가)
    filename= img_url.split('.')[0] #imagename_dslkfjlaew.jpg -> imagename
    mask_path = os.path.join(settings.BASE_DIR, 'CandyMaker', 'img', 'masks', f'{filename}_mask.jpg')
    ###################################################################################################
    print(filename, mask_path)

    # 1. load image
    img = cv.imread(mask_path)
    img_org = cv.imread(img_url)
    print('1')

    # 2. preprocess img
    # img = preprocessing(img)
    print('2')

    # img, rect = contours(img, img_org)  # rect에 좌표 저장 [Left_Top, Right_Bottom]
    # print('3')
    # # organizing rect
    # lt_x = [];
    # lt_y = [];
    # rb_x = [];
    # rb_y = [];
    # lt_coord = [];
    # rb_coord = []
    # for i in range(len(rect)):
    #     lt_x.append(list(rect[i][0])[0])
    #     lt_y.append(list(rect[i][0])[1])
    #     rb_x.append(list(rect[i][1])[0])
    #     rb_y.append(list(rect[i][1])[1])
    #     lt_coord.append([lt_x, lt_y])
    #     rb_coord.append([rb_x, rb_y])

    ## 6. Rearrange Books
    # coords = create_bookshelf(img_org)
    #print(coords)

    print('gi')
    return redirect('EyeCandy_Web:result', pk)
