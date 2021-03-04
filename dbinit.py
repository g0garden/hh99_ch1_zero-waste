from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

client = MongoClient('mongodb://strong1133:tjrwls455@15.164.102.138', 27017)
db = client.dbhh99

# 크롬드라이버설정
chrome_driver_dir = './static/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless') -> 크롬 백그라운드 실행

# 드라이버로 크롬 연결 및 url설정
driver = webdriver.Chrome(
    chrome_driver_dir)  # chrome_options=chrome_options # Optional argument, if not specified will search path.및

# 인스타 태그 검색어 아스키 코드 처리  이후 확장성을 위해 검색어 별도 변수 선언
base_url = 'https://www.instagram.com/explore/tags/'
plus_url = '환경운동'
url = base_url + quote_plus(plus_url)
driver.get('https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet');
action = ActionChains(driver)

# db.db_zerowaste.drop()

time.sleep(1)  # 크롬 지연//

# 인스타 로그인 요청으로 인한 로그인 자동화
driver.find_elements_by_name("username")[0].send_keys("h99test455@gmail.com")
driver.find_elements_by_name("password")[0].send_keys("gkdgo99@")
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").submit()

time.sleep(2)  # 크롬 지연//

# 로그인 후 타켓 URL 이동을 위한 URL 재 호출
driver.get(url);
time.sleep(3)  # 크롬 지연//

# 목적지 까지 크롬 이동후 bs4로 크롤링
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

insta = soup.select('.v1Nh3.kIKUG._bz0w')  # 이미지 URL 정보가 들어있는 클래스 타겟팅 -> 전체 게시물 수 파악
article_base = "https://www.instagram.com"  # 게시물 URL 제작을 위한 사전 작업

for i in insta:  # 이미지가 들어있는 게시물 전체 갯수 만큼 반복문
    img_url = i.select_one('.KL4Bh').img['src']  # 한개의 게시물에 있는 이미지 타겟팅
    article_url = i.select_one('a')['href']  # 한개의 게시물에 있는 원문 URL 정보 타겟팅

    article_url = article_base + article_url  # 활용 가능한 URL 로 다듬어주기
    # print(img_url, article_url)
    time.sleep(3)
    driver.get(article_url)  # 획득한 원문 URL로 크롬 이동 -> 게시물 내용물들 긁어오기 위함
    time.sleep(5)

    title = driver.find_elements_by_css_selector('.sqdOP.yWX7d._8A5w5.ZIAjV')[0].text  # 작성자(제목) 타겟팅
    tags = driver.find_elements_by_css_selector('.xil3i')  # 해당 게시물에 있는 태그들 갈무리

    tag_list = []  # 한개의 게시물에 여러 태그가 있기 때문에 db 저장시 한 줄에 여러 태그를 포함 시키기 위한 리스트 선언

    for i in tags:
        # print(title.text, i.text)
        tag_list.append(i.text)
    # 태그가 여러개 이기 때문에 반목문으로 하나씩 뽑아서 리스트에 담아줌

    doc = {
        'title': title,
        'tags': tag_list,
        'img_url': img_url,
        'article_url': article_url,
    }  # 만들어진 데이터들을 db에 넣기 위해 딕셔너리로 가공

    db.db_zerowaste.insert_one(doc)  # DB 저장
    print(doc)
