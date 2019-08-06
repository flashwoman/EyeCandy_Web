# EyeCandy_Web_Ver0

![EyeCandy](https://github.com/arara90/images/blob/master/fleshwoman/EyeCandy_main.png?raw=true)



### The first Upload

#### 1.   EyeCandy?

- OpenCV를 이용한 Object detection / SOM, KNN을 이용한 이미지 분석

- 기획 :  기능 및 UI- **https://ovenapp.io/view/gtunfBRgZEruy15poKXND961AD3ThtVC/C9XhD**

  

#### 2. 현재 버전

- openCV의 window를 웹과 연결하지 못한 상태입니다. 따라서 유저가 책장을 선택하여 책과 분리하는 로직이 가능하여, 전체 로직 확인을 위해 중간 단계에 속하는 해당 로직(책-책장의 구분)의 결과인 마스크 이미지([test1_mask.jpg](https://github.com/flashwoman/EyeCandy_Web/blob/master/CandyMaker/img/masks/test1_mask.jpg))를 미리 저장하였고, [test1.jpg](https://github.com/flashwoman/EyeCandy_Web/blob/master/media/origin/test1.jpg) 파일로 확인합니다.

- 해당 버전의 개발 과정은 [Object-detection](https://github.com/flashwoman/EyeCandy), [EyeCandy](https://github.com/flashwoman/EyeCandy)를 통해 확인할 수 있습니다.

- **실행 결과 이미지**

  !<img src="https://github.com/flashwoman/EyeCandy_Web/blob/master/media/origin/test1.jpg?raw=true" style="width:350px">  ▶▶   <img src="https://github.com/flashwoman/EyeCandy_Web/blob/master/media/output/output_test1.jpg?raw=true">

  

#### 3. 문제점?



#### 4. 1차 목표

- 책장과 분리하는 로직 연결

  - 현재 생각한 방안

    - 로직 그대로 Window를 웹에 올리는 것 연구해보기 ( 사례 조사 미진행 )

    - watershed를 통한 구현

    - Color Channel 활용하기.

      

- object detection 정확도 높이기..................

  - 실제 책등(book spine) 이미지 모아서 활용해보기.

    



#### 5. 2차 목표

- 딥러닝 로직 향상
- 유저별로 관리