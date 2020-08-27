import webbrowser
import time
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


captionerBrowser = Chrome() # WebDriver for the API

captionerBrowser.get('http://localhost/projet/')

j = 1

with open("URL_Youtube.txt", "r", encoding='utf-8') as URLs:

    for url in URLs:
        webbrowser.open(url, new=1) # Open your default browser on url
        time.sleep(2) # Every waiting time is here to let time for the browser to load the video and other functions
        captionerBrowser.find_element(By.ID, 'btnStartStop').click()        
        time.sleep(120) # Listen for up to 2 minutes if video is longer 
        captionerBrowser.find_element(By.ID, 'btnStartStop').click()
        time.sleep(5)
        os.system("TASKKILL /F /IM brave.exe") # Close the browser used to read the videos, webbrowser module doesn't have function for it
        captionerBrowser.find_element(By.ID, 'btnDownload').click()
        time.sleep(1)
        captionerBrowser.refresh() # refresh to clear the text area
        os.rename('C:/Users/marti/Downloads/caption.txt','C:/Users/marti/Desktop/INFO/Projet-Stage/Code/Youtube_captions/Entry_' + str(j) + '.txt') 
        entry_path = 'C:/Users/marti/Desktop/INFO/Projet-Stage/Code/Youtube_captions/Entry_' + str(j) + '.txt'
        entry_text = open(entry_path, "rt")
        text = entry_text.read()
        
        if len(text.split()) < 10 :
            entry_text.close()
            os.chmod(entry_path, 0o777)
            if entry_path.find('(inoperable)') == -1:
                os.rename(entry_path,entry_path[:-4] + '(inoperable).txt')
        else:    
            entry_text.close()
        j += 1

captionerBrowser.quit()
