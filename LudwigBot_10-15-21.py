from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from tkinter import *
from threading import *
import threading
import time
import sys
import keyboard
import wikipedia
from googlesearch import search       
import colorama
import os
from colorama import Fore, Back, Style
import keyboard

colorama.init()
os.system("cls")

print(f"""{Fore.GREEN}{Style.BRIGHT}

██╗     ██╗   ██╗██████╗ ██╗    ██╗██╗ ██████╗ 
██║     ██║   ██║██╔══██╗██║    ██║██║██╔════╝ 
██║     ██║   ██║██║  ██║██║ █╗ ██║██║██║  ███╗
██║     ██║   ██║██║  ██║██║███╗██║██║██║   ██║
███████╗╚██████╔╝██████╔╝╚███╔███╔╝██║╚██████╔╝
╚══════╝ ╚═════╝ ╚═════╝  ╚══╝╚══╝ ╚═╝ ╚═════╝ 
                                               
""")

def command():
 try:
 
   if (important[0] == "b'lw_caracol") or (important[1] == "lw_caracol"):
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht wewant to access
     user.send_keys("_Bot:_ ▄▄▄─▄▀░▄░▀▄─█░█▄▀░█─█░▀▄▄▀█▄█▄▀▄▄█▄▄▄▄███▀o")
     user.send_keys(Keys.RETURN)
     time.sleep(1)
  # Random Command
   if (important[0] == "b'Sushi") or (important[1] == "Sushi"):
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]') # The element taht wewant to access
     user.send_keys("_Ludwig:_ Culiao Rico")
     user.send_keys(Keys.RETURN)
     time.sleep(1)
     
  # Testing Messge 
   if (important[0] == "b'lw.test") or (important[1] == "lw.test"):
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht wewant to access
     user.send_keys("_Ludwig:_ activo... ")
     user.send_keys(Keys.RETURN)
     time.sleep(1)
       
  # Send Image (May not work)
   if (important[0] == "b'.gdsdto") or (important[1] == ".gdsdsto"):  
     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div').click()
     driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]').click()
     time.sleep(2)
     keyboard.write(r"C:\Users\Zark\Desktop\Basic\gatico.jpg")
     keyboard.press("enter")
     time.sleep(2)
     mensaje_gat = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]')
     mensaje_gat.send_keys("_Ludwig:_ En efecto, *gato.*")
     driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div/span').click()
     time.sleep(1)   
     
  # Changes group name (Requires admin, Raw text) = lw_titulo.   
   if (raw_member == "b'lw_titulo"):
       group_p = command_raw[1] 
       driver.find_element_by_xpath('//*[@id="main"]/header/div[2]').click()
       driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div[2]/div[1]/span[2]/div/span').click()
       name = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div[2]/div[1]/div/div[2]')
       name.clear()
       name.send_keys(group_p)
       name.send_keys(Keys.RETURN)
  
  # Changes group name (Requires admin, User text) = lw_titulo.       
   elif (group_member == "lw_titulo"): 
       group_p = command_user[1]
       driver.find_element_by_xpath('//*[@id="main"]/header/div[2]').click()
       time.sleep(2) 
       driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div[2]/div[1]/span[2]').click()
       name = driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[1]/div[2]/div[1]/div/div[2]')
       name.clear()
       name.send_keys(group_p)
       name.send_keys(Keys.RETURN)
  
  # Search using Wikipedia (Raw text) = lw_wikipedia.
   if (raw_member == "b'lw_wikipedia"):
     group_p = command_raw[1]
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht we want to access
     answers = wikipedia.summary(group_p)
     user.send_keys(answers)
     user.send_keys(Keys.RETURN)
     time.sleep(1)
   
  # Search using Wikipedia (User text) = lw_wikipedia.   
   elif (group_member == "lw_ikipedia"): 
     group_p = command_user[1]
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht we want to access
     answers = wikipedia.summary(group_p)
     user.send_keys(answers)
     user.send_keys(Keys.RETURN)
     time.sleep(1)
      
  # Search using Google (Raw text) = lw_google.   
   if (raw_member == "b'lw_google"):
     group_p = command_raw[1]
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht wewant to access
     answers = search(group_p)
     user.send_keys(answers)
     user.send_keys(Keys.RETURN)
     time.sleep(1)
 
  # Search using Google (User text) = lw_google.     
   elif (group_member == "lw_google"): 
     group_p = command_user[1]
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht wewant to access
     answers = search(group_p)
     user.send_keys(answers)
     user.send_keys(Keys.RETURN)
     time.sleep(1)  
      
 except InvalidElementStateException:
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht wewant to access
     user.send_keys("_Ludwig:_ Error - No cuento con privilegios de admnistrdor ") 
     user.send_keys(Keys.RETURN)
     time.sleep(1)
 except:
     user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') # The element taht wewant to access
     user.send_keys("_Ludwig:_ Error - Desconocido")
     user.send_keys(Keys.RETURN)
     time.sleep(1)
     
 return

def espera():
 try:
  element = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
 except:
  return False
 return  True 
# ----------------------------------------------------------------------------------------------------------------------
last = ""

print(f"Inicializando...{Fore.WHITE}{Style.DIM}")
  
chrome_options = Options()
chrome_options.add_argument(r'--user-data-dir=C:\\Users\\Zark\\AppData\\Local\\Google\\Chrome\\User Data\\')
path = ("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", options= chrome_options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")

while 1:
    while espera() == True:  
     print(f"{Fore.GREEN}{Style.BRIGHT}Para iniciar el rastreo presione (S)i: {Fore.WHITE}{Style.DIM}")
     start_o = input()
     while start_o == "S" or start_o == "s":  
      try:
          user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]') # The element that we want to access
          user.send_keys("_Ludwig:_ Test ")
          user.send_keys(Keys.RETURN)
          user.send_keys(r"")
          user.send_keys(Keys.RETURN)
          time.sleep(1)
          print(f"{Fore.YELLOW}{Style.BRIGHT}Testeando entrada de texto...{Fore.WHITE}{Style.DIM}")
          
      except:
          print(f"{Fore.RED}{Style.DIM}Error: barra de mensajes no seleccionada")
          time.sleep(2)

      while keyboard.is_pressed('q') == False:
       try:
           text_m = driver.find_elements_by_class_name("_2wUmf")[-1]  #Constntly checks for new mesages
           #text_m = driver.find_elements_by_class_name("_1bR5a")[-1] # Constntly checks for new mesages
           #print(Fore.GREEN + Style.BRIGHT + str(text_m) + Fore.WHITE + Style.DIM)
           actual_mess = str(text_m.text.encode("utf-8"))
           important = actual_mess.split("\\n")
           command_user =  important[1].split(".") # Avoid detecting a username
           group_member = command_user[0]
           command_raw =  important[0].split(".") # Detecting raw text
           raw_member = command_raw[0]
        
       except: 
            user = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            user.send_keys("_Ludwig:_ Error - Cambio de chat!")
            user.send_keys(Keys.RETURN)
            time.sleep(1)
           
       if important != last :
             print(str(important) + " \r")
             command() 
             last = important

      print(f"{Fore.RED}{Style.DIM}Ending")
      break      
     break  
# -------------------------------------------------------


  


# -------------------------------------- 

