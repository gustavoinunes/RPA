import time
import pyautogui
from tkinter import *
import tkinter as tk
import tkinter.ttk as TTK
import clipboard
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.by import By

menu = tk.Tk()

opcoes = ["Código item","Texto máscara"]
opcoes_box = tk.StringVar()
pesquisa_box = tk.StringVar()
login_box = tk.StringVar()
senha_box = tk.StringVar()

menu.title("Excluir máscaras")
menu.geometry("255x120+450+350")
menu.resizable(width=False, height=False)
#menu.iconbitmap("C:/Users/gustavo.nunes/Desktop/H-sohome-2-Copia.ico")

texto_0 = Label(menu, text="Tipo:").grid(row=0, column=0)
texto_1 = Label(menu, text="Pesquisa:").grid(row=1, column=0)
texto_2 = Label(menu, text="Login:").grid(row=2, column=0)
texto_3 = Label(menu, text="Senha:").grid(row=3, column=0)

box_0 = TTK.Combobox(menu,values=opcoes, textvariable=opcoes_box).grid(row=0, column=1)
box_1 = Entry(menu, textvariable=pesquisa_box).grid(row=1, column=1)
box_2 = Entry(menu, textvariable=login_box).grid(row=2, column=1)
box_3 = Entry(menu, textvariable=senha_box, show='*').grid(row=3, column=1)

botao = Button(menu, text="Executar", command= lambda: menu.destroy()).grid(row=4, column=1)
menu.mainloop()


conexao = create_engine('postgresql://postgres:admin@10.1.57.244:5432/dwfocco')
script_dados = """    SELECT g_exclusao_mascara.id FROM g_exclusao_mascara where g_exclusao_mascara.data_inclusao < current_date-1 ORDER BY id   """
dados = pd.read_sql_query(sql=script_dados, con=conexao)
dados = dados['id'].tolist()
print(dados)


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
lupa.send_keys("FENG0257")
time.sleep(1)
programa = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[2]/div[1]/ul/li/ul/li/ul/li/ul/li/a/div[2]/div/div[1]")
programa.click()
time.sleep(1)
pyautogui.click(x=540, y=250)
time.sleep(6)

inicio = time.time()
cont = 0
var_2 = 0

if opcoes_box.get() == "Código item":
    script_linhas = """   SELECT tmasc_item.id FROM tmasc_item JOIN titens_empr ON titens_empr.id = tmasc_item.itempr_id WHERE titens_empr.empr_id = 1 and titens_empr.cod_item = '""" + pesquisa_box.get() + """'   """
    linhas = pd.read_sql_query(sql=script_linhas, con=conexao)
    linhas = linhas['id'].tolist()

    pyautogui.press('f7')
    pyautogui.write(pesquisa_box.get())
    pyautogui.press('f8')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)

    for x in range(len(linhas)):
        pyautogui.press('tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('ctrl', 'c')
        var = int(clipboard.paste())

        if var != var_2:
            if (var in dados):
                pyautogui.hotkey('ctrl', 'a')
                cont += 1
                tempo = round(time.time() - inicio, 0)
                hora = int(tempo // 3600)
                minuto = int((tempo % 3600) // 60)
                segundo = int((tempo % 3600) % 60)
                print(f"{hora}h:{minuto}m:{segundo}s - nº {cont}: id {var}")
                var_2 = var
            else:
                var_2 = var
                pyautogui.press('down')

        if cont != 0 and cont % 10 == 0:
            pyautogui.press('f10')
            time.sleep(2)


elif opcoes_box.get() == "Texto máscara":
    script_linhas = """   SELECT tmasc_item.id FROM tmasc_item WHERE tmasc_item.mascara LIKE '""" + pesquisa_box.get().replace("%", "%%") + """'   """
    linhas = pd.read_sql_query(sql=script_linhas, con=conexao)
    linhas = linhas['id'].tolist()

    pyautogui.press('tab')
    pyautogui.press('f7')
    pyautogui.press('tab')
    pyautogui.write(pesquisa_box.get())
    pyautogui.press('f8')
    time.sleep(2)

    for x in range(len(linhas)):
        pyautogui.press('tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('ctrl', 'c')
        var = int(clipboard.paste())

        if var != var_2:
            if (var in dados):
                pyautogui.hotkey('ctrl', 'a')
                cont += 1
                tempo = round(time.time() - inicio, 0)
                hora = int(tempo // 3600)
                minuto = int((tempo % 3600) // 60)
                segundo = int((tempo % 3600) % 60)
                print(f"{hora}h:{minuto}m:{segundo}s - nº {cont}: id {var}")
                var_2 = var
            else:
                var_2 = var
                pyautogui.press('down')

        if cont != 0 and cont % 10 == 0:
            pyautogui.press('f10')
            time.sleep(2)


else:
    pyautogui.press('tab')
    for x in range(len(dados)):
        pyautogui.press('f7')
        pyautogui.write(str(dados[x]))
        pyautogui.press('f8')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.hotkey('shift', 'tab')
        pyautogui.hotkey('ctrl', 'c')
        var = int(clipboard.paste())
        pyautogui.hotkey('ctrl', 'a')
        cont += 1
        tempo = round(time.time() - inicio, 0)
        hora = int(tempo // 3600)
        minuto = int((tempo % 3600) // 60)
        segundo = int((tempo % 3600) % 60)
        print(f"{hora}h:{minuto}m:{segundo}s - nº {cont}: id {var}")
        pyautogui.press('f10')
        time.sleep(2)


pyautogui.press('f10')
time.sleep(2)

print("Processo finalizado!")
print(f"Máscaras apagadas: {cont}")