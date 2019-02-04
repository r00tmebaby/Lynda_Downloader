'''

Author 	: Zdravko Georgiev (r00tmebaby)
Github 	: https://github.com/r00tmebaby
License : MIT


Copyright (c) 2019 Zdravko Georgiev (r00tmebaby)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''


##############################################
# Lynda Downloading Script
#   by r00tme 26/01/2019
# version: 0.7 Downloading with Pre-Specified List
###############################################
#               Options:
# Creating Category Folder Automatically
# Creating Course Sub-folder Automatically
# Creating Course Difficulty Folder Prefix Automatically
# Creating .php File with a Course Description Automatically - Useful for web development
# Dumping video duration and date added
# Creating a log.txt file to  save the course path, so the .zip archives can be moved later
#############################################

path = r"C:\\chromedriver.exe"  # Specify chrome Driver Path @String
browser = 1  # 1= Chrome, 2= Firefox, 3=Safari, 4=Opera :: Any Other Number is Default Chrome
# Replace r00tme with your username, the script will try to use your Chrome settings
profile_dr = r"C:\\Users\\r00tme\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
page = ""
maxi = False  # Maximize Window @Boolean
load = 30  # PageLoad Time @Integer

save_dir = r"Z:\\F\\Tutorials\\"  # Saving Files Main Directory
finished_list = r"exercise_logs.txt"  # File that will log all downloaded course directories so the .zip archives can be moved later
course_list = r"Z:\\F\\dls_list.txt"  # All courses that we want to be downloaded. Courses list
zip_download = r"Z:\\F\\Download\\"  # Directory that will be used to download zip archives, they will be moved to their folders at the end
show_progress = False

####--- Login Type--#####
login_in = True  # Login in
username = ""  # Login Username
password = ""  # Login Password
usr_field = "username"  # Field Name For Username :: Selected By Name
pas_field = "password"  # Field Name For Password :: Selected By Name
login_btn = "btn-primary"  # Login Button :: Selected By Class Name
#########################
