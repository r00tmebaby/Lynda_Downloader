# Lynda_Downloader
Lynda Downloader is a python script that is capable to download multiple courses, their exercise files and related information. 

The idea of this scrtipt was to be able to download multiple courses with a given list along with their excersize files and information about each course.
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
1. Fill your login credentials in config.py

<code><b><p>login_in = True</p><p>username = "Your username here"</p><p>password ="Your password here" </p></b></code>
 
2. The next step is to fill this part:

<code><b><p>page = "" # Login URL</p><p>save_dir= r"C:\\Tutorials\\" # Saving Files Main Directory</p><p>finished_list = r"logs.txt"# File that will log all downloaded course directories so the .zip archives can be moved later</p><p>course_list   = r"C:\\download_list.txt"  # All courses that we want to be downloaded. Courses list</p><p>zip_download  = r"C:\\Download\\"# Directory that will be used to download zip archives, they will be moved to their folders at the end</p></b></code>

3. You have to create a donwload list manualy with the links to the courses that you want to download
4. Run the script by typing lindi.py and it will do the work for you.

