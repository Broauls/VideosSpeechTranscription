import time
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

captionerBrowser = Chrome() # WebDriver for the API
vimeoPlayerBrowser = Chrome() # WebDriver for Vimeo's video player

captionerBrowser.get('http://localhost/projet/')

j = 1

with open("URL_Vimeo.txt", "r", encoding='utf-8') as URLs:

    for url in URLs:
        vimeoPlayerBrowser.get(url)
        time.sleep(3) # Every waiting time is here to let time for the browser to load the video and other functions
        captionerBrowser.find_element(By.ID, 'btnStartStop').click()   

        if len(vimeoPlayerBrowser.find_elements_by_class_name('play.rounded-box.state-paused')) != 0 : # One way to find if a button exist or not with the function find_elementS
            videoLength = int(vimeoPlayerBrowser.find_element_by_class_name('focus-target').get_attribute('aria-valuemax'))
            print("Video n°" + str(j) + " ____ Length : " + str(videoLength))
            exist = True
            vimeoPlayerBrowser.find_element_by_class_name('play.rounded-box.state-paused').click()

            if videoLength <= 120 :
                time.sleep(videoLength)
            else:
                time.sleep(120) # Listen for up to 2 minutes if video is longer 
        else :
            print("Video n°" + str(j) + " ____ DO not exist anymore")
            exist = False
            time.sleep(1)

        captionerBrowser.find_element(By.ID, 'btnStartStop').click()
        time.sleep(2)
        captionerBrowser.find_element(By.ID, 'btnDownload').click()
        time.sleep(2)
        captionerBrowser.refresh() # refresh to clear the text area

        if not exist :
            os.rename('C:/Users/marti/Downloads/caption.txt','C:/Users/marti/Desktop/INFO/Projet-Stage/Code/Vimeo_captions/Entry_' + str(j) + '(non-existent video).txt')
        else:
            os.rename('C:/Users/marti/Downloads/caption.txt','C:/Users/marti/Desktop/INFO/Projet-Stage/Code/Vimeo_captions/Entry_' + str(j) + '.txt')
            entry_path = 'C:/Users/marti/Desktop/INFO/Projet-Stage/Code/Vimeo_captions/Entry_' + str(j) + '.txt'
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
vimeoPlayerBrowser.quit()