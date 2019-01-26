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
page = "https://login.openathens.net/auth/bbk.ac.uk/o/15022?t=%2Fsaml%2F2%2Fsso%2Fbbk.ac.uk%2Fc%2Fukfed%3FSAMLRequest%3DfVLJboMwEP0V5DsYkEjACkg0OTRS2qJAe%252BilMsYEK8amjGmbvy%252BELumhOY7mzds0K6Ct7Eg6mEbt%252BevAwVgfrVRAzosYDb0imoIAomjLgRhG8vRuR3zHJV2vjWZaIisF4L0RWq21gqHlfc77N8H4434Xo8aYDgjG0IjSkSdVUYfpFufjWGrJTeMAaDyx%252Bjh7yAtkbUYbQtGJ8Pdc6oNQju74uGi4AkdxgyeX2McTQVkeHcqc4YgZHo41r5C13cToJVx4VUDrIAhYFPlVuGBhFdbLmi5dWi2oN8IABr5VYKgyMfJdL7Jdz%252Fb9wveIG5Fg%252BYys7CvrjVCVUIfrxZQzCMhtUWT2nOmJ93DOMwJQspqMk7Nwf1H4dVr63TJK%252FukUfjq1oVvhC5FZsSP3I%252Bt2k2kp2MlKpdTv655Tw2PkIZzMJ3%252F%252FIfkE%26RelayState%3Dcookie%253A1548191397_7706&ctx=sd"
maxi = False  # Maximize Window @Boolean
load = 30  # PageLoad Time @Integer

save_dir = r"C:\\Tutorials\\"  # Saving Files Main Directory
finished_list = r"logs.txt"  # File that will log all downloaded course directories so the .zip archives can be moved later
course_list = r"C:\\courses_list.txt"  # All courses that we want to be downloaded. Courses list
zip_download = r"C:\\Download\\"  # Directory that will be used to download zip archives, they will be moved to their folders at the end

####--- Login Type--#####
login_in = True  # Login in
username = ""  # Login Username
password = ""  # Login Password
usr_field = "username"  # Field Name For Username :: Selected By Name
pas_field = "password"  # Field Name For Password :: Selected By Name
login_btn = "btn-primary"  # Login Button :: Selected By Class Name
#########################
