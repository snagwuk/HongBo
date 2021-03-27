import time
import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import smtplib
from email.mime.text import MIMEText


def mail_send():
    # 세션 생성
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # TLS 보안 시작
    s.starttls()

    # 로그인 인증
    s.login('snagwuk940@gmail.com', 'xochrkjtohuvxbpx')

    # 보낼 메시지 설정
    msg = MIMEText('네이버 카페 홍보 실패!')
    msg['Subject'] = '[실패] 탕템 홍보 오류'

    # 메일 보내기
    s.sendmail("snagwuk940@gmail.com", "tkddnrdlsp@naver.com", msg.as_string())

    # 세션 종료
    s.quit()


id_file_nm = 'id_list.ini'
id_list = []

article_file_nm = 'article_list.ini'
article_list = []

job_file_nm = 'job_list.ini'
job_list = []

# id_list 불러오기
file = open(id_file_nm, 'r')
line = file.readline()
while line != '':
    temp = line.split('/')
    tmp_dic = {}
    tmp_dic.setdefault('id', temp[0])
    tmp_dic.setdefault('pw', temp[1])
    tmp_dic.setdefault('nic', temp[2])
    tmp_dic.setdefault('group', temp[3])
    id_list.append(tmp_dic)
    line = file.readline()
file.close()
#print(id_list)

# article_list 불러오기
file = open(article_file_nm, 'r')
line = file.readline()
while line != '' or line == '\n':
    temp = line.split('/')
    tmp_dic = {}
    tmp_dic.setdefault('job_id', temp[0])
    tmp_dic.setdefault('menu_id', temp[1])
    sub = file.readline()
    tmp_dic.setdefault('subject', sub)
    content = file.readline()
    tmp_dic.setdefault('content', content)
    article_list.append(tmp_dic)
    line = file.readline()
file.close()
#print(article_list)

# article_list 불러오기
file = open(job_file_nm, 'r')
line = file.readline()
while line != '' or line == '\n':
    temp = line.split('/')
    tmp_dic = {}
    tmp_dic.setdefault('id', temp[0])
    tmp_dic.setdefault('job_id', temp[1])
    job_list.append(tmp_dic)
    line = file.readline()
file.close()
#print(job_list)

# 네이버 로그인
global driver


def login(login_id, login_pw):
    # 네이버 로그인 열기
    driver.get('https://nid.naver.com/nidlogin.login')

    # id, pw 입력할 곳을 찾습니다.
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
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
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()

    # 슬립을 꼭 넣어줘야 한다.
    # 그렇지 않으면 로그인 끝나기도 전에 다음 명령어가 실행되어 제대로 작동하지 않는다.
    time.sleep(3)


def duple_chk(my_nic):
    write_yn = 0

    driver.get(f'https://cafe.naver.com/ArticleList.nhn?search.clubid=26447544&search.boardtype=L')
    time.sleep(2)

    driver.switch_to.frame('cafe_main')
    for i in range(1, 16):
        nickname = driver.execute_script(
            f'return document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_name > div > table > tbody > tr > td > a").innerText')
        #print(nickname)
        if my_nic == nickname:
            write_yn = 1
            #print('★이미게시물존재')
            return write_yn
    return write_yn


def write_article(menu_id, subject, img_link):
    time.sleep(3)

    # 게시판 등록 화면 이동
    driver.get('https://cafe.naver.com/ca-fe/cafes/26447544/menus/' + menu_id + '/articles/write?boardType=L')
    time.sleep(4)

    t1 = driver.find_element_by_class_name('textarea_input')
    t1.clear()
    t1.send_keys(subject)

    driver.find_element_by_class_name('se-popup-close-button').click()

    #####################################################################
    img_tag = driver.find_element_by_css_selector('.se-toolbar-item-oglink')
    time.sleep(0.5)
    img_tag.click()
    time.sleep(3)

    tag_id = driver.find_element_by_class_name('se-popup-oglink-input')
    tag_id.clear()
    time.sleep(1)
    tag_id.click()
    pyperclip.copy(img_link)
    tag_id.send_keys(Keys.CONTROL, 'v')

    driver.find_element_by_class_name('se-popup-oglink-button').click()
    time.sleep(5)

    driver.find_element_by_class_name('se-popup-button-text').click()
    time.sleep(3)

    driver.find_element_by_class_name('BaseButton__txt').click()
    time.sleep(8)


#####################################################################

# coptions = webdriver.ChromeOptions()
# coptions.add_argument('headless')
# coptions.add_argument('window-size=1920x1080')
# coptions.add_argument("disable-gpu")
# coptions.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36")
# coptions.add_argument("lang=ko_KR")
# driver = webdriver.Chrome('chromedriver', options=coptions)


# driver = webdriver.Chrome()
# jf0304 = id_list[3]
# print(jf0304)
# login(jf0304.get('id'), jf0304.get('pw'))
# chk = duple_chk(jf0304.get('nic'))
# tail = article_list[1]
# write_article(tail.get('menu_id'), tail.get('subject'), tail.get('content'))
# driver.quit()


group = 'B'
try:
    
    size = 200
    i = 0
    while i < size:
        if '18' <= datetime.now().time().strftime("%H") <= '24':
            group = 'A'
        for temp_id in id_list:
            if group == temp_id.get('group'):
                nid = temp_id.get('id')
                for job in job_list:
                    if nid == job.get('id'):
                        job_id = job.get('job_id')
                        for art in article_list:
                            if job_id == art.get('job_id'):
                                driver = webdriver.Chrome()
                                #driver.set_window_position(-1920, 0)
                                #driver.set_window_size(800, 900)
                                if duple_chk(temp_id.get('nic')) == 0:
                                    login(nid, temp_id.get('pw'))
                                    write_article(art.get('menu_id'), art.get('subject'), art.get('content'))
                                    if duple_chk(temp_id.get('nic')):
                                        b=1
                                    else:
                                        mail_send()
                                        i=200
                                driver.quit()
        print('Loop : ' + str(i) + '[' + str(datetime.now()) + ']')
        time.sleep(300)
        i = i + 1
except:
    mail_send()
