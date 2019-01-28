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
page = "https://lynda.com"
maxi = False  # Maximize Window @Boolean
load = 30  # PageLoad Time @Integer

save_dir = r"C:\\Tutoria\\"  # Saving Files Main Directory
finished_list = r"logs.txt"  # File that will log all downloaded course directories so the .zip archives can be moved later
course_list = r"C:\\d_list.txt"  # All courses that we want to be downloaded. Courses list
zip_download = r"C:\\Download\\"  # Directory that will be used to download zip archives, they will be moved to their folders at the end

####--- Login Type--#####
login_in = False  # Login in
username = ""  # Login Username
password = ""  # Login Password
usr_field = "username"  # Field Name For Username :: Selected By Name
pas_field = "password"  # Field Name For Password :: Selected By Name
login_btn = "btn-primary"  # Login Button :: Selected By Class Name
#########################
