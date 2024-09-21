import sys
import time
import pyautogui
import pandas as pd
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.common.by import By

conexao = create_engine('postgresql://postgres:admin@10.1.57.244:5432/dwfocco')
script_dados = """    SELECT g_exclusao_mascara.id FROM g_exclusao_mascara where g_exclusao_mascara.data_inclusao < current_date-1 ORDER BY id   """
dados = pd.read_sql_query(sql=script_dados, con=conexao)
dados = dados['id'].tolist()
print(dados)

driver = webdriver.Chrome()
driver.get("https://sistema.meucentury.com/PROWeb/Authentication/Login?ReturnUrl=%2FPROWeb%2Ferp")
user = driver.find_element(By.ID, "txtUser")
user.send_keys("AUTOMACAO")
senha = driver.find_element(By.ID, "txtPassword")
senha.send_keys("f3ipro")
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
pyautogui.press('tab')

for x in range(len(dados)):
    pyautogui.press('f7')
    pyautogui.write(str(dados[x]))
    pyautogui.press('f8')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('f10')
    time.sleep(1)

pyautogui.hotkey('alt', 'f4')
driver.quit()
sys.exit()