# Video Speech Transcription

This project follows a previous one, made by Maxime Gomes Correia.
The goal is to extract the textual content in order to complete the datatsets already elaborated. 

You will find in this repository :
* One HTML file to be put inside www directory of WampServer
* One Python script to extract URLs from the previous project
* Two Python scripts to gather text content of videos

link to previous project : https://github.com/MaximeGomesCorreia/COVID-19_Datasets_OnlineVideos

## Requirements

* Download and install WampServer or anything similar : https://www.wampserver.com/
* Download and install Selenium WebDriver : https://www.selenium.dev/
* Download and install VB-Cable or anything else to redirect audio output to audio input : https://www.vb-audio.com/Cable/
* Download and install Google Chrome ( and Brave if you plan to use Youtube )

## Protocol

* Start WampServer
* Run chromdriver from your shell
* Redirect audio output into audio input
* Launch either one of the script ( Youtube_caption_gatherer.py or Vimeo_caption_gatherer.py )
* Allow Google Chrome to use your microphone
