#################################
# Configuration File
# @version 0.3 01/12/2019
# @author r00tme
#################################

path = "C:/chromedriver.exe"    # Specify chrome Driver Path @String
browser = 1                     # 1= Chrome, 2= Firefox, 3=Safari, 4=Opera :: Any Other Number is Default Chrome



page = ""                       # Login URL
maxi = False                    # Maximize Window @Boolean
load = 30                       # PageLoad Time @Integer

save_dir      = r"C:\\Tutorials\\"        # Saving Files Main Directory
finished_list = r"logs.txt"               # File that will log all downloaded course directories so the .zip archives can be moved later
course_list   = r"C:\\download_list.txt"  # All courses that we want to be downloaded. Courses list
zip_download  = r"C:\\Download\\"         # Directory that will be used to download zip archives, they will be moved to their folders at the end

####--- Login Type--#####
login_in  =  True               # Login in
username  = ""          # Login Username
password  = ""     # Login Password
usr_field = "username"          # Field Name For Username :: Selected By Name
pas_field = "password"          # Field Name For Password :: Selected By Name
login_btn = "btn-primary"       # Login Button :: Selected By Class Name
#########################

####--- Using Search Field--#####
se_fld =  False                 # Using Search Field
se_text = "SQL"                 # Typing Text in Search Field
#########################

