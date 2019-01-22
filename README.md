# Lynda_Downloader
<img src="https://i.gyazo.com/18774847678fd60490f939f662ed2f9b.png"></img>

Lynda Downloader is a python script that uses Selenium Driver and is capable to download multiple courses at once, their exercise files and related information from Lynda.com. 

The idea of this scrtipt was to be able to download multiple courses with a given list along with their excersize files and information about each course and then to display them directly on a private library website, without the need of touching anything else.

The script will create categgory and course name folders automatically and download the video files inside it. That is very helpfull if you want to create a private library or to build similar like Lynda.com website.</br>


# Requirements
1. Python 3+ installed </br>
2. Selenium driver installed. </br>
3. PIP Installed
4. Chrome browser installed and chromedriver downloaded</br>

# Installation
1. You need to download and install python version 3 or higher</br>
2. You can then install selenium driver by typing <code><b>pip install selenium</b></code> in the command prompt</br>
3. Now is the time to download and install Chrome Browser and Chrome driver
4. Install Chromedriver

# Configuration
1. Specify your login credentials in config.py, login url, courses list file destination, chromedriver destination and main download folder
2. You have to create a donwload list manualy with the links to the courses that you want to download
3. Run the script by typing lindi.py and it will do the work for you.

