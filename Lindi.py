##############################################
# Lynda Downloading Script
#   by r00tme 12/01/2019
# version: 0.3 Downloading with Pre-Specified List
###############################################
#               Options:
# Creating Category Folder Automatically
# Creating Course Sub-folder Automatically
# Creating Course Difficulty Folder Prefix Automatically
# Creating .php File with a Course Description Automatically - Useful for web development
# Dumping video duration and date added
# Creating a log.txt file to  save the course path, so the .zip archives can be moved later
#############################################

from Functions import Main
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, re, Config


main = Main()  # Calling Main Class
driver = main.driver(Config.browser, Config.path)  # The Driver
driver.set_page_load_timeout(Config.load)  # Using Load Time
main.max_window(Config.maxi)  # Maximize Window
driver.get(Config.page)  # Starting Url
courses_count = 0 # Courses Counter
total_counter = 0  # Counting the total videos downloaded
prefix = ""  # This prefix will be put on front of every course to mark its difficulty level

print(
r"%s     \ ########################################### \
     \      Lynda.com Downloading Script           \
     \     @author r00tme  12/01/2019              \
     \     @version: 0.3                           \
     \     Downloading with Pre-Specified List     \
     \############################################## %s" % (
    main.bcolors.OKBLUE + main.bcolors.BOLD, main.bcolors.ENDC), flush=True)
print("%s The Program Has Been Started... %s" % (
    main.bcolors.HEADER + main.bcolors.BOLD, main.bcolors.ENDC), flush=True)


# Logging with username password using the given in the main config
if Config.login_in:
    driver.find_element_by_name(Config.usr_field).send_keys(Config.username)
    driver.find_element_by_name(Config.pas_field).send_keys(Config.password)
    driver.find_element_by_class_name(Config.login_btn).click()

if Config.se_fld:
    # Typing in Search field if in Config is True
    driver.find_element_by_id('header-search-field').send_keys(Config.se_text)
    driver.find_element_by_id('header-search-field').send_keys(Keys.RETURN)

for items_for_download in open(Config.course_list, "r"):

    # Looping all links in the download list
    normal_list = items_for_download.split("?")
    driver.get(normal_list[0])
    time.sleep(1)
    # Remove underscores from the zipped files
    print(r"%s %s Processing URL:  %s  %s" % (main.bcolors.BOLD, main.bcolors.HEADER, driver.current_url, main.bcolors.ENDC), flush=True)

    cat_name = items_for_download.split("/")[3]

    # Opening Overview TAB To inspect the Content - It is bit buggy sometimes and need couple of clicks
    driver.find_element_by_css_selector('.tab-overview.ga').click()
    driver.find_element_by_css_selector('.tab-overview.ga').click()
    driver.find_element_by_css_selector('.tab-overview.ga').click()
    driver.find_element_by_css_selector('.tab-overview.ga').click()

    # Selecting Course Difficulty Text
    elementss = driver.find_element_by_css_selector(
        "#course-info > div > div.col-sm-3.col-md-3.col-lg-2 > div:nth-child(1) > h6 > strong").text

    # Setting Course Name Prefix to mark the course difficulty - Useful for further developments
    if elementss == "Intermediate":
        prefix = "1-"
    elif elementss == "Advanced":
        prefix = "2-"
    else:
        prefix = "0-"

    # Stripping the course name from the course link
    course_name = prefix + items_for_download.split("/")[4].replace("-", " ")

    # Creating Course directory if it does not exist
    if not main.dir_exist(Config.save_dir + r"\\" + cat_name + r"\\" + course_name):
        os.makedirs(Config.save_dir + r"\\" + cat_name + r"\\" + course_name)
        print("%s Directory %s has been successfully created %s" % (
            main.bcolors.OKGREEN, Config.save_dir + r"\\" + cat_name, main.bcolors.ENDC), flush=True)
    try:
          driver.find_element_by_link_text('Exercise Files').click()
          # Trying to find exercise file if not found just continue to the next operation
          driver.find_element_by_link_text('Exercise Files').click()

          driver.find_element_by_link_text('Exercise Files').click()
          # downloading the exercise files
          ex_down_link = driver.find_element_by_css_selector('.course-file.clearfix.ga').click()
          driver.find_element_by_link_text('Exercise Files').click()
          driver.find_element_by_link_text('Exercise Files').click()
          tex_down_link = driver.find_element_by_partial_link_text('Ex_Files')
          time.sleep(0.2)
          logs = open(Config.save_dir + Config.finished_list, "a+")
          clean_f_name = re.sub(r'\([^()]*\)', '', tex_down_link.text).replace("_", "")
          logs.write("%s" % (cat_name + r"\\" + course_name + ":" + clean_f_name))
    except:
        driver.get(driver.current_url)


    elementss2 = driver.find_element_by_id('tab-overview').get_attribute('innerHTML')
    time.sleep(0.2)

    if not main.file_exist(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\info.php") or os.stat(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\info.php").st_size == 0: 
       f = open(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\info.php", "a+", encoding="utf-8")
       f.write(elementss2)

    counter = 0  # Will count the loops - Just for the function
    temp_counter = 0  # Will count only the successfully downloaded videos for the current course
    time.sleep(0.2)
    # Stripping only the videos
    course = driver.find_elements_by_css_selector('.item-name.video-name.ga')

    # Will store all video links for the current course as an array
    listsak = []
    for k in course:
        # Adding the links
        listsak.append(k.get_attribute('href'))

    for i in listsak:

        counter +=1
        driver.get(i)

        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "banner-play"))).click()
        # 2 seconds waiting time *It works in my internet connection speed, but may not work with yours
        # If you see an error message url="" (an empty url), increase the sleeping time value
        time.sleep(1)
        try:
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.TAG_NAME, "video")))
        finally:
            video = driver.find_element_by_tag_name('video')
        time.sleep(0.5)
        video_name = driver.current_url.split("/")[4].replace("-", " ")
        url_temp = video.get_attribute('src')
        dumper = video.get_attribute("data-conviva").replace("}", "").replace("{", "").replace("\"", "").replace(":", "-").split(",")
        # print(base64.b64encode(bytes(dumper, 'utf-8')))
        #Video name fix *Adding more information

        video_name = "%04d_%s_%s_%s" % (counter, video_name, dumper[0].replace("Duration-", ""), dumper[4].replace("ReleaseYear-", ""))


        if not main.file_exist(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\\" + video_name + ".mp4"):
              main.download(url_temp,
                            Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\\" + video_name + ".mp4")
              print("%s  %s Successfully Downloaded %s" % (main.bcolors.OKGREEN,
                           Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\\" + video_name + r".mp4",
                           main.bcolors.ENDC), flush=True)
              total_counter += 1
              temp_counter += 1
        else:
                    print("%s File %s already exist. Skipped! %s" % (
                     main.bcolors.FAIL, video_name + ".mp4", main.bcolors.ENDC), flush=True)

        # If all videos are downloaded continue to next step
        if counter == len(course):
            courses_count += 1
            print(
                  "%s You have successfully downloaded course %s with %d videos."
                  "\n Downloaded %d courses and %d videos in total %s" % (
                     main.bcolors.BOLD +
                     main.bcolors.OKBLUE,
                     course_name, temp_counter, courses_count, total_counter,
                     main.bcolors.ENDC), flush=True
                  )
