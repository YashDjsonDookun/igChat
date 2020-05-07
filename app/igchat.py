from tkinter import *
import tkinter.ttk as ttk
import time
from tkinter.messagebox import showinfo
from selenium import webdriver

win = Tk()
win.title('IG Chat')
win.geometry('300x500')

def automation():
    username_automation = username.get()
    password_automation = passwd.get()

    if username_automation == "" or password_automation == "":
        showinfo("IG Chat", "Username and Password need to be filled!")
    else:
        driver = webdriver.Chrome()
        driver.get("https://www.instagram.com/")

        time.sleep(3)
        username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        username.send_keys(username_automation)

        password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password.send_keys(password_automation)
        time.sleep(2)

        login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        login.click()
        time.sleep(3)

        turnOnNotif = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        turnOnNotif.click()

username_label = ttk.Label(win,text="Username:", foreground="blue", font=("",12))
username_label.grid(row=0,column=0)
username = ttk.Entry(win, width=20)
username.grid(row=0,column=1)

password_label = ttk.Label(win,text="Password:", foreground="blue", font=("",12))
password_label.grid(row=1,column=0)
password = ttk.Entry(win,show="*",width=20)
password.grid(row=1,column=1,padx=15)

button = ttk.Button(win, txt="Login", command=automation)
button.grid(row=2,column=0,columnspan=2)

win.mainloop()