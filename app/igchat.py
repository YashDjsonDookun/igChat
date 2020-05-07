# from tkinter import *
import tkinter.ttk as ttk
# import tk_tools
# import tkinter_nav as tknav
import time
from tkinter.messagebox import showinfo
from selenium import webdriver
#
# win = Tk()
# win.title('IG Chat')
# win.geometry('300x500')
#
# def Login():
#     username_automation = username.get()
#     password_automation = password.get()
#
#     if username_automation == "" or password_automation == "":
#         showinfo("IG Chat", "Username and Password need to be filled!")
#     else:
#         driver = webdriver.Chrome()
#         driver.get("https://www.instagram.com/")
#         time.sleep(3)
#
#         user = driver.find_element_by_xpath(
#             '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
#         user.send_keys(username_automation)
#         time.sleep(3)
#
#         passwd = driver.find_element_by_xpath(
#             '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
#         passwd.send_keys(password_automation)
#
#         login = driver.find_element_by_xpath(
#             '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
#         login.click()
#         time.sleep(3)
#
#         turnOnNotif = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
#         turnOnNotif.click()
#
# username_label = ttk.Label(win, text="Username:", foreground="blue", font=("", 12))
# username_label.grid(row=0, column=0)
# username = ttk.Entry(win, width=20)
# username.grid(row=0, column=1)
#
# password_label = ttk.Label(win, text="Password:", foreground="blue", font=("", 12))
# password_label.grid(row=1, column=0)
# password = ttk.Entry(win, show="*", width=20)
# password.grid(row=1, column=1, padx=15)
#
# button = ttk.Button(win, text="Login", command=Login)
# button.grid(row=2, column=0, columnspan=2)
#
# win.mainloop()

import tkinter as tk

class IgChat(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.win = None

        self.Login()

    def Login(self):
        if self.win == None:
            self.win = tk.Frame(self.master)
            self.win.pack()

            self.username = tk.Label(self.win, text="Username:", foreground="blue", font=("", 12)).pack()
            # self.username_label.grid(row=0, column=0)
            self.username = tk.Entry(self.win, width=20).pack()
            # self.username.grid(row=0, column=1)
            #
            self.password_label = tk.Label(self.win, text="Password:", foreground="blue", font=("", 12)).pack()
            # self.password_label.grid(row=1, column=0)
            self.password = tk.Entry(self.win, show="*", width=20).pack()
            # self.password.grid(row=1, column=1, padx=15)
            #
            # self.button = tk.Button(self.win, text="Login").pack()
            # self.button.grid(row=2, column=0, columnspan=2)

            tk.Button(self.win, text="Destroy all widgets in this frame!", command= self.clear_window).pack()

    def clear_window(self):
        # self.win.destroy()
        # self.win = None

        self.username_automation =  username.get()
        self.password_automation =  passwd.get()

        if self.username_automation == "" or self.password_automation == "":
            showinfo("IG Chat", "Username and Password need to be filled!")
        else:
            driver = webdriver.Chrome()
            driver.get("https://www.instagram.com/")
            time.sleep(3)

            user = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
            user.send_keys(self.username_automation)
            time.sleep(3)

            passwd = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
            passwd.send_keys(self.password_automation)

            login = driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
            login.click()
            time.sleep(3)

            turnOnNotif = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            turnOnNotif.click()

win = tk.Tk()
win.title('IG Chat')
win.geometry('300x500')
ig_chat_app = IgChat(win)
win.mainloop()