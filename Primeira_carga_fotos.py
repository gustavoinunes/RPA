import time
import pyautogui
from os import chdir, listdir
from tkinter import *
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By

# menu = tk.Tk()
# login_box = tk.StringVar()
# senha_box = tk.StringVar()
# diretorio_box = tk.StringVar()
#
# menu.title("Fotos produtos")
# menu.geometry("260x100+450+350")
# menu.resizable(width=False, height=False)
# #menu.iconbitmap("C:/Users/gustavo.nunes/Desktop/H-sohome-2-Copia.ico")
#
# texto_1 = Label(menu, text="Login:").grid(row=0, column=0)
# texto_2 = Label(menu, text="Senha:").grid(row=1, column=0)
# box_1 = Entry(menu, textvariable=login_box).grid(row=0, column=1)
# box_2 = Entry(menu, textvariable=senha_box, show='*').grid(row=1, column=1)
#
# botao = Button(menu, text="Executar", command= lambda: menu.destroy()).grid(row=1, column=2)
# menu.mainloop()

chdir('Z:/Tecnologia da Informação/Imagens/Produtos')
arquivos = listdir()
print(arquivos)

# driver = webdriver.Chrome()
# driver.get("https://sistema.meucentury.com/PROWeb/Authentication/Login?ReturnUrl=%2FPROWeb%2Ferp")
# user = driver.find_element(By.ID, "txtUser")
# user.send_keys(login_box.get())
# senha = driver.find_element(By.ID, "txtPassword")
# senha.send_keys(senha_box.get())
# entrar = driver.find_element(By.ID, "btnSignin")
# entrar.click()
#
# try:
#     exists: driver.find_element(By.ID, "btnSessionAlreadyActiveContinue")
# except:
#     None
# else:
#     erro = driver.find_element(By.ID, "btnSessionAlreadyActiveContinue")
#     erro.click()
#
# menu = driver.find_element(By.ID, "menu")
# menu.click()
# time.sleep(1)
# lupa = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/input")
# lupa.send_keys("FITE0200")
# time.sleep(1)
# programa = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[2]/div[1]/ul/li/ul/li/ul/li/ul/li/a/div[2]/div/div[1]")
# programa.click()
# time.sleep(1)
# pyautogui.click(x=540, y=250)
#time.sleep(30)

cont = 0
inicio = time.time()

for x in range(len(arquivos)):
    item = arquivos[x]
    time.sleep(4)
    pyautogui.press('f7')
    time.sleep(1)
    pyautogui.write(item[0:5])  # so codigo produto
    time.sleep(1)
    pyautogui.press('f8')
    time.sleep(4)
    pyautogui.click(x=1350, y=370)    # aba imagem
    time.sleep(8)
    pyautogui.click(x=790, y=820)  # ler imagem
    time.sleep(4)
    pyautogui.write(item) #nome arquivo
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8)
    pyautogui.press('f10')
    time.sleep(8)
    pyautogui.click(x=1000, y=600)
    time.sleep(8)
    cont += 1
    tempo = round(time.time() - inicio, 0)
    hora = int(tempo // 3600)
    minuto = int((tempo % 3600) // 60)
    segundo = int((tempo % 3600) % 60)
    print(f"{hora}h:{minuto}m:{segundo}s - nº {cont}: {item}")
    pyautogui.click(x=1350, y=290)  # aba item

print("Processo finalizado!")