</br>

<h1 align="center" style="color:red"> 항해99 Cpt#1 Zero-waste  :zap: </h1>

</br></br>

## 🌏 http://hh99zerowaste.shop/

</br>

## 🤠 Part

총 2인

- 정석진 : 백엔드

- 고정원 : 프론트

## :rocket:기능

- 회원가입, 로그인, 개인 프로필 설정
- 해쉬태그 기반 인스타그램 게시물 크롤링
- 인스타그램 게시물에 회원별 마킹 및 나의 마킹 게시물 모아보기
- 마킹 게시물에 메모하기 기능

</br>

## 🦄 프로젝트 썸네일

<p align="center">
<p>로그인 페이지 </p>
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-01.png?raw=true" width="60%"></img>
</p>


<p align="center">
    <p>인스타그램 게시물 전체 보기</p>
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-03.png?raw=true" width="70%"></img>
</p>


</br>
</br>
<br/>

## :mag: 요약

- 지구를 살리는 운동 `````#제로웨이스트````` 운동을 알리고 동참하기 위해 다른 챌린저 들이 
- 해당 운동에 어떻게 참여하고 있는 지 등을 인스타그램을 통해 모아보고 마킹하고 
- 마킹한 게시물에 간단 메모 할 수 있는 서비스!

</br>

## :closed_book: 기술

#### :orange_book: backend

- Python
- Flask
- Beautifulsoup
- Selenium
- Mongodb - pymongo
- PYJWT -토른
- SSR - Jinja2

#### :orange_book: frontend

- HTML
- CSS
- JavaScript
- JQuery

#### :orange_book: Hosting

- AWS: EC2
- ubuntu

</br>

## :package: 개발 환경

- Pycharm
- ubuntu, aws

</br>

## 📸 Schreenshot

#### :heavy_check_mark: 로그인 페이지

<p align="center">
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-01.png?raw=true" width="70%"></img>
</p>

</br>

#### :heavy_check_mark: 회원가입 페이지

<p align="center">
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-02.png?raw=true" width="70%"></img>
</p>

</br>

#### :heavy_check_mark: 인스타그램 전체 보기

<p align="center">
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-03.png?raw=true" width="70%"></img>
</p>

</br>

#### :heavy_check_mark: 마킹 게시물 모아보기

<p align="center">
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-04.png?raw=true" width="70%"></img>
</p>

</br>

#### :heavy_check_mark: 개인 프로필 편집

<p align="center">
<img src="https://github.com/strong1133/hh99_zero-waste/blob/main/sample_img/sample-05.png?raw=true" width="70%"></img>
</p>

</br>


</br>


## 💽 Setting

- 패키지 설치  ```pip install -r requierments.txt```
- 실행 ``` python app.py ```
- localhost에서 실행 할 경우  
    ```client = MongoClient('localhost', 27017)```
- ubuntu로 실행시 크롬옵션 관련 이슈 발생시  
    1. 크롬버전 확인 ``` google-chrome --version ```
    2. 크롬 버전에 맞는 리눅스용 크롬드라이버를 다운받아 static>bin안에 넣어줘야함.
    3. 관련 블로그  
     https://somjang.tistory.com/entry/Ubuntu-Ubuntu-%EC%84%9C%EB%B2%84%EC%97%90-Selenium-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0 


</br>

### 👑 After 프로젝트

- 공유하기 기능을 추가해 내가 마킹하고 적은 메모를 공유하기 탭에 옴겨 게시판 처럼 쓸수 있는 페이지 구축
- 반응형 
