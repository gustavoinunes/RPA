import time
import os
import pyautogui
from tkinter import *
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import base64
import psycopg2

connection = psycopg2.connect(dbname='dwfocco',host='10.1.57.244',port='5432',user='postgres',password='admin')

cursor = connection.cursor()
query = """ SELECT
            TITENS.COD_ITEM || '_' || REPLACE(TRIM(REPLACE(TITENS.DESC_TECNICA,'MODELO ','')),' ','_') ITEM,
            TITENS_EB.COD_ITEM || '_' || REPLACE(REPLACE(TRIM(REPLACE(TITENS_EB.DESC_TECNICA,'MODELO ','')),' ','_'),'/','B') DESC_EB,
            TITENS_CX.COD_ITEM || '_' || REPLACE(TRIM(REPLACE(TITENS_CX.DESC_TECNICA,'MODELO ','')),' ','_') DESC_CX,
            TITENS_CX_EB.COD_ITEM || '_' || REPLACE(REPLACE(TRIM(REPLACE(TITENS_CX_EB.DESC_TECNICA,'MODELO ','')),' ','_'),'/','B') DESC_CX_EB,
            TITENS_IMAGENS.IMAGEM
            FROM TITENS_EMPR
            
            JOIN TITENS ON TITENS.ID = TITENS_EMPR.ITEM_ID
            LEFT JOIN TITENS_IMAGENS ON TITENS_IMAGENS.ITEM_ID = TITENS.ID
            JOIN TITENS_CONTABIL ON TITENS_CONTABIL.ITEMPR_ID = TITENS_EMPR.ID
            JOIN TGRP_INVENT ON TGRP_INVENT.ID = TITENS_CONTABIL.GRP_INVENT_ID
            JOIN TGRP_CLAS_ITE ON TGRP_CLAS_ITE.ID = TITENS_CONTABIL.GRP_CLAS_ID
            LEFT JOIN TMARCAS_PROD ON TMARCAS_PROD.ID = TITENS.MARCA_ID
            
            LEFT JOIN TITENS TITENS_EB ON TITENS_EB.DESC_TECNICA LIKE TITENS.DESC_TECNICA || '%E/' AND TITENS_EB.DESC_TECNICA NOT LIKE TITENS.DESC_TECNICA || '%CAIXA%'
            LEFT JOIN TITENS_IMAGENS TITENS_IMAGENS_EB ON TITENS_IMAGENS_EB.ITEM_ID = TITENS_EB.ID
            
            LEFT JOIN TITENS TITENS_CX ON TITENS_CX.DESC_TECNICA LIKE TITENS.DESC_TECNICA || '%CAIXA'
            LEFT JOIN TITENS_IMAGENS TITENS_IMAGENS_CX ON TITENS_IMAGENS_CX.ITEM_ID = TITENS_CX.ID
            
            LEFT JOIN TITENS TITENS_CX_EB ON TITENS_CX_EB.DESC_TECNICA LIKE TITENS.DESC_TECNICA || '%CAIXA E/'
            LEFT JOIN TITENS_IMAGENS TITENS_IMAGENS_CX_EB ON TITENS_IMAGENS_CX_EB.ITEM_ID = TITENS_CX_EB.ID
            
            
            WHERE TITENS_EMPR.EMPR_ID = 1
            AND TITENS.SIT = 1
            AND TGRP_INVENT.COD_GRP_INVENT = 400
            AND (TGRP_CLAS_ITE.COD_GRP_ITE LIKE '30.100.%'OR TGRP_CLAS_ITE.COD_GRP_ITE LIKE '30.200.%' OR TGRP_CLAS_ITE.COD_GRP_ITE LIKE '30.300.%')
            AND TITENS_IMAGENS.IMAGEM IS NOT NULL
            
            AND TITENS.DESC_TECNICA NOT LIKE '%E/%'
            AND TITENS.DESC_TECNICA NOT LIKE '%CAIXA%'
            AND TITENS.DESC_TECNICA NOT LIKE '%CAPA%'
            AND TITENS.DESC_TECNICA NOT LIKE '%DETALHE%'
            AND TITENS.DESC_TECNICA NOT LIKE '%KIT%'
            
            AND ( 	(TITENS_EB.ID IS NOT NULL AND TITENS_IMAGENS_EB.IMAGEM IS NULL) 
                    OR (TITENS_CX.ID IS NOT NULL AND TITENS_IMAGENS_CX.IMAGEM IS NULL) 
                    OR (TITENS_CX_EB.ID IS NOT NULL AND TITENS_IMAGENS_CX_EB.IMAGEM IS NULL)
                )
                
            ORDER BY TRIM(REPLACE(TITENS.DESC_TECNICA,'MODELO ','')) ASC   """

cursor.execute(query)
lista = cursor.fetchall()
arquivos = []

k=0
for l in range(len(lista)):
    file_binary = lista[l][4].tobytes()
    encoded_data = base64.b64encode(file_binary)
    for c in range(1, 4):
        if str(lista[l][c]) != 'None':
            nome_arquivo = str(lista[l][c]) + ".jpg"
            arquivos.append(nome_arquivo)
            file_binary = lista[l][4].tobytes()
            with open(nome_arquivo, "wb") as image_file:
                 image_file.write(base64.decodebytes(encoded_data))


menu = tk.Tk()
login_box = tk.StringVar()
senha_box = tk.StringVar()
diretorio_box = tk.StringVar()

menu.title("Fotos produtos")
menu.geometry("260x100+450+350")
menu.resizable(width=False, height=False)
#menu.iconbitmap("C:/Users/gustavo.nunes/Desktop/H-sohome-2-Copia.ico")

texto_1 = Label(menu, text="Login:").grid(row=0, column=0)
texto_2 = Label(menu, text="Senha:").grid(row=1, column=0)
box_1 = Entry(menu, textvariable=login_box).grid(row=0, column=1)
box_2 = Entry(menu, textvariable=senha_box, show='*').grid(row=1, column=1)

botao = Button(menu, text="Executar", command= lambda: menu.destroy()).grid(row=1, column=2)
menu.mainloop()

driver = webdriver.Chrome()
driver.get("https://sistema.meucentury.com/PROWeb/Authentication/Login?ReturnUrl=%2FPROWeb%2Ferp")
user = driver.find_element(By.ID, "txtUser")
user.send_keys(login_box.get())
senha = driver.find_element(By.ID, "txtPassword")
senha.send_keys(senha_box.get())
entrar = driver.find_element(By.ID, "btnSignin")
entrar.click()

try:
    exists: driver.find_element(By.ID, "btnSessionAlreadyActiveContinue")
except:
    None
else:
    erro = driver.find_element(By.ID, "btnSessionAlreadyActiveContinue")
    erro.click()

menu = driver.find_element(By.ID, "menu")
menu.click()
time.sleep(1)
lupa = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/input")
lupa.send_keys("FITE0200")
time.sleep(1)
programa = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[2]/div[1]/ul/li/ul/li/ul/li/ul/li/a/div[2]/div/div[1]")
programa.click()
time.sleep(1)
pyautogui.click(x=540, y=250)
time.sleep(7)

cont = 0
inicio = time.time()

for x in range(len(arquivos)):
    item = arquivos[x]
    time.sleep(3)
    pyautogui.press('f7')
    time.sleep(1)
    underline = item.index("_")
    pyautogui.write(item[0:underline])  # so codigo produto
    time.sleep(1)
    pyautogui.press('f8')
    time.sleep(3)
    pyautogui.click(x=1350, y=370)    # aba imagem
    time.sleep(5)
    pyautogui.click(x=1250, y=200)
    time.sleep(1)
    pyautogui.click(x=790, y=820)  # ler imagem
    time.sleep(2)
    pyautogui.click(x=763, y=256)
    pyautogui.click(x=763, y=256)
    pyautogui.click(x=763, y=256)
    pyautogui.click(x=763, y=256)
    pyautogui.click(x=763, y=256)
    pyautogui.click(x=763, y=256)
    pyautogui.write(item) #nome arquivo
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.press('f10')
    time.sleep(6)
    pyautogui.click(x=1000, y=600)
    time.sleep(2)
    cont += 1
    tempo = round(time.time() - inicio, 0)
    hora = int(tempo // 3600)
    minuto = int((tempo % 3600) // 60)
    segundo = int((tempo % 3600) % 60)
    print(f"{hora}h:{minuto}m:{segundo}s - nº {cont}: {item}")
    pyautogui.click(x=1350, y=290)  # aba item

dir = os.listdir()
for file in dir:
    if file in arquivos:
        os.remove(file)

print("Processo finalizado!")