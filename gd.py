import time
import pyperclip as pyperclip
from datetime import datetime
from cryptography.fernet import Fernet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

id_file_nm = 'gs_ids.ini'
id_list = []

url_naver_serch = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%B2%9C%ED%95%98%EC%A0%9C%EC%9D%BC+%EA%B1%B0%EC%83%81&oquery=%EA%B1%B0%EC%83%81&tqi=hvV4Elp0YidssmhszRwssssstAC-231111'
url_login = 'http://www.gersang.co.kr/pub/logi/login/login.gs?returnUrl=www%2Egersang%2Eco%2Ekr%2Fpub%2Fmemb%2Fsecu%2Fquie%2Egs%3F'
url_check = 'http://www.gersang.co.kr/event/2021/20210301_attendance/main.gs'
enc_key = b'NaFu0Jx5tASx9YWr5NHfe9ts-KLhN7HoCF48Uo63Zrw='
global driver

# 아이디 목록 파일 불러오기
file = open(id_file_nm, 'r')
line = file.readline()
while line != '':
    temp = line.split('/')
    tmp_dic = {}
    tmp_dic.setdefault('id', temp[0])
    # 복호화
    decrypt = Fernet(enc_key).decrypt(temp[1].encode())
    tmp_dic.setdefault('pw', decrypt.decode())
    id_list.append(tmp_dic)
    line = file.readline()
file.close()


# print(id_list)


# 거상 로그인
def login(login_id, login_pw):
    # 거상 로그인 열기
    driver.get(url_login)

    # id, pw 입력할 곳을 찾습니다.
    # tag_id = driver.find_element_by_name('GSuserID')
    tag_id = driver.find_element_by_xpath(
        '/html/body/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/input')
    tag_pw = driver.find_element_by_xpath(
        '/html/body/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table/tbody/tr/td[3]/input')
    tag_id.clear()
    time.sleep(1)

    # id 입력
    tag_id.click()
    pyperclip.copy(login_id)
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw 입력
    tag_pw.click()
    pyperclip.copy(login_pw)
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼을 클릭합니다
    driver.find_element_by_xpath(
        '/html/body/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[3]/input').click()

    # 슬립을 꼭 넣어줘야 한다.
    # 그렇지 않으면 로그인 끝나기도 전에 다음 명령어가 실행되어 제대로 작동하지 않는다.
    time.sleep(3)

    # 네이버 '거상' 검색 한 주소
    driver.get(url_naver_serch)
    time.sleep(3)
    # 거상 링크 클릭
    driver.find_element_by_xpath('//*[@id="main_pack"]/section[1]/div[2]/div[1]/div/div[2]/dl/div[5]/dd/a').click()
    time.sleep(3)
    # 거상 출석체크 페이지 이동
    driver.get(url_check)
    time.sleep(3)
    # 네이버 검색 팝업 클리
    driver.find_element_by_xpath('//*[@id="popup"]/div[1]/a/img').click()
    time.sleep(1)
    # 시간에 따른 출석 체크 버튼 클릭
    #    시간 대     class_name
    # 00:05~05:55 = btn_11
    # 06:05~11:55 = btn_12
    # 12:05~17:55 = btn_13
    # 18:05~23:55 = btn_14
    hour = datetime.now().hour
    if 0 <= hour & hour < 6:
        driver.find_element_by_class_name('btn_11').click()
    elif 6 <= hour & hour < 11:
        driver.find_element_by_class_name('btn_12').click()
    elif 12 <= hour & hour < 18:
        driver.find_element_by_class_name('btn_13').click()
    else:
        driver.find_element_by_class_name('btn_14').click()
    time.sleep(1)


#####################################################################
a = 1
while a <= 1:
    for Tid in id_list:
        driver = webdriver.Chrome()
        login(Tid.get("id"), Tid.get("pw"))
        print(str(datetime.now()) + ":" + Tid.get("id"))
        driver.quit()
    time.sleep(3600)
