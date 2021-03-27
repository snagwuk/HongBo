import time
from tkinter import *

import pyperclip
from listAll import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 로그인 창
win = Tk()
win.geometry('200x160')
win.title('Login')

# ID 입력창
idLabel = Label(win, text="ID")
idLabel.pack()
idEntry = Entry(win)
idEntry.pack()

# password 입력
pwLabel = Label(win, text="Password")
pwLabel.pack()
pwEntry = Entry(win, show='*')
pwEntry.pack()

# page 입력
pageLabel = Label(win, text="Pages")
pageLabel.pack()
pageEntry = Entry(win)
pageEntry.pack()


def login():
    # 네이버 로그인 열기
    driver = webdriver.Chrome()
    driver.get('https://nid.naver.com/nidlogin.login')

    # id, pw 입력할 곳을 찾습니다.
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    time.sleep(1)

    # id 입력
    tag_id.click()
    # pyperclip.copy(idEntry.get())
    pyperclip.copy("tkddnr701")
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # pw 입력
    tag_pw.click()
    # pyperclip.copy(pwEntry.get())
    pyperclip.copy("1q2w3e4r")
    tag_pw.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)

    # 로그인 버튼을 클릭합니다
    login_btn = driver.find_element_by_id('log.login')
    login_btn.click()

    # 슬립을 꼭 넣어줘야 한다.
    # 그렇지 않으면 로그인 끝나기도 전에 다음 명령어가 실행되어 제대로 작동하지 않는다.
    time.sleep(3)

    driver.get( f'https://cafe.naver.com/ArticleList.nhn?search.clubid=26447544&search.boardtype=L')
    time.sleep(2)

    mynicname = '테일문상'
    duple_chk = 0

    driver.switch_to.frame('cafe_main')
    for i in range(1, 16):
        nickname = driver.execute_script(
            f'return document.querySelector("#main-area > div:nth-child(6) > table > tbody > tr:nth-child({i}) > td.td_name > div > table > tbody > tr > td > a").innerText')
        print(nickname)
        if mynicname == nickname:
            duple_chk = 1
            break

    print(duple_chk)

    #driver.find_element_by_class_name('_rosRestrict').click()
    # t1 = driver.find_element_by_class_name('prfl_info')
    # print(t1.get_attribute('strong'))


    time.sleep(20000)


#####################################################################


    #driver.quit()


# login 버튼
loginButton = Button(win, text="Login", command=login)
loginButton.pack()

login()

#win.mainloop()
