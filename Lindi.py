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
# version: 1.0 Downloading with Pre-Specified List
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, re, Config, sys, threading, itertools, datetime

main = Main()  # Calling Main Class
sys.stdout.write(
 "\r%s%s###############################################\n"
     "#     Lynda.com Downloading Script            #\n"
     "#     @author r00tmebaby  26/01/2019          #\n"
     "#     @version: 1.0                           #\n"
     "#     Downloading with Pre-Specified List     #\n"
     "##############################################\n\n" % (
     main.bcolors.sd, main.bcolors.fc))
sys.stdout.flush()
driver = main.driver(Config.browser, Config.path)  # The Driver
done = False

if not main.file_exist(Config.course_list):
    exit("\r%s[%s*%s] ERROR: %sFile %s does not exist in the specified directory. Please check the configuration file!" % (
        main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fr, Config.course_list))

# Animation function
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            sys.stdout.write('\r%s[%s*%s]%s Processing URL: %s' %(
              main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc, driver.current_url))
            sys.stdout.flush()
            break
        sys.stdout.write('\r%s[%s%s%s]%s Loading Lynda.com and signing ' %(
            main.bcolors.bm, main.bcolors.fc, main.bcolors.sb+main.bcolors.fw+c, main.bcolors.sn+main.bcolors.fm, main.bcolors.fc))
        sys.stdout.flush()
        time.sleep(0.1)


threading.Thread(target=animate).start()   # Start threading process to the animate function
driver.set_page_load_timeout(Config.load)  # Using Load Time
main.max_window(Config.maxi)               # Maximize Window
driver.get(Config.page)                    # Starting Url

courses_count = 0       # Courses Counter
total_counter = 0       # Counting the total videos downloaded
prefix = ""             # This prefix will be put on front of every course to mark its difficulty level

# Login attempt, Please replace find_element_by_name if your login url needs different selection

if Config.login_in:
            driver.find_element_by_name(Config.usr_field).send_keys(Config.username)
            driver.find_element_by_name(Config.pas_field).send_keys(Config.password)
            driver.find_element_by_class_name(Config.login_btn).click()


done = True  # Resetting the loading animation

# Opening the course downloading list and reading the urls-s if they exit
for items_for_download in open(Config.course_list, "r"):
    normal_list = items_for_download.split("?")
    driver.get(normal_list[0])
   
    # Searching for a modal message and trying to close it
    try:
       driver.find_element_by_class_name("close").click()
    except:
        pass
     
    cat_name = items_for_download.split("/")[3]
    if len(cat_name) == 0:
        cat_name =  items_for_download.split("/")[4]


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
    if not items_for_download.split("/")[4] == cat_name:
        course_name = prefix + items_for_download.split("/")[4].replace("-", " ")
    else:
        course_name = prefix + items_for_download.split("/")[5].replace("-", " ")

    logs1 = open(Config.save_dir + "logs.txt", "a+")
    logs1.write("%s" % ("\n"+cat_name + r"\\" + course_name))

    # Creating Course directory if it does not exist
    if not main.dir_exist(Config.save_dir + r"\\" + cat_name + r"\\" + course_name):
        os.makedirs(Config.save_dir + r"\\" + cat_name + r"\\" + course_name)
        sys.stdout.write('\n%s[%s*%s]%s Directory %s has been successfully created' % (
            main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc,  cat_name +"\\" + course_name))
        sys.stdout.flush()
    try:
          driver.find_element_by_link_text('Exercise Files').click()
          # Trying to find exercise file if not found just continue to the next operation
          driver.find_element_by_link_text('Exercise Files').click()

          driver.find_element_by_link_text('Exercise Files').click()
          # downloading the exercise files
          sys.stdout.write('\n%s[%s*%s]%s Downloading Exercise Files.... ' % (
              main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc))
          sys.stdout.flush()
          ex_down_link = driver.find_element_by_css_selector('.course-file.clearfix.ga').click()
          driver.find_element_by_link_text('Exercise Files').click()
          driver.find_element_by_link_text('Exercise Files').click()
          tex_down_link = driver.find_element_by_partial_link_text('Ex_Files')
          time.sleep(0.2)
          logs = open(Config.save_dir + Config.finished_list, "a+")
          clean_f_name = re.sub(r'\([^()]*\)', '', tex_down_link.text).replace("_", "")
          logs.write("%s" % (cat_name + r"\\" + course_name + ":" + clean_f_name))

    except:
        driver.get(driver.current_url)  # Refresh the page if excercise files are not found

    # Reading course transcription and information
    elementss2 = driver.find_element_by_id('tab-overview').get_attribute('innerHTML')
    time.sleep(0.2)
    # Saving the information into the course directory as info.php file
    if not main.file_exist(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\info.php") or os.stat(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\info.php").st_size == 0:
       f = open(Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\info.php", "a+", encoding="utf-8")
       f.write(elementss2)

    counter = 0       # Will count the loops - Just for the function
    temp_counter = 0  # Will count only the successfully downloaded videos for the current course
    time.sleep(0.2)

    # Getting the videos by Css selector
    # *Please note that it may differ after time if Lynda update their styles
    course = driver.find_elements_by_css_selector('.item-name.video-name.ga')

    # Will store all video links for the current course as an array
    listsak = []
    for k in course:
        # Adding the links
         listsak.append(k.get_attribute('href'))

    # Going trough every link in the array
    for i in listsak:
        time.sleep(0.5)
        driver.get(i)   # Opening the video link
        counter += 1
        
        # Trying to click on play video button, if that did not work will look for modal close button and click on it
        try:
           WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "banner-play"))).click()
        except:
            # Trying to click on modal closing button
            driver.find_element_by_class_name("close").click()
            time.sleep(0.3)
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "banner-play"))).click()
            
        # 1 seconds waiting time works for my internet connection speed, but may not work with yours
        # If you see an error message url="" (an empty url), increase this sleeping time value
        time.sleep(1)

        # Trying to get the video tag and read the src attribute
        try:
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.TAG_NAME, "video")))
        finally:
            video = driver.find_element_by_tag_name('video')
        time.sleep(0.2)
        url_temp = video.get_attribute('src')

        # Clearing video name Stage 1
        video_name = driver.current_url.split("/")[4].replace("-", " ")
        # Clearing the download link to suits our needs
        dumper = video.get_attribute("data-conviva").replace("}", "").replace("{", "").replace("\"", "").replace(":", "-").split(",")
        # Adding numerated prefix for a proper lexicographic order
        video_name = "%04d_%s_%s_%s" % (counter, video_name, dumper[0].replace("Duration-", ""), dumper[4].replace("ReleaseYear-", ""))
        # Creating variable for the completed saving path
        save_dir   = Config.save_dir + r"\\" + cat_name + r"\\" + course_name + r"\\" + video_name + ".mp4"

        # Trying to download the video file three times
        # Each unsuccessful attempt will increase the sleeping time value
        # I have tested it and it works 100% for me with these delays
        # Keep an eye and increase or decrease the values if they do not work for you

        if not main.file_exist(save_dir):
            time.sleep(0.1)
            try:
                main.download(url_temp, save_dir)
            except:
                time.sleep(0.3)
                try:
                    main.download(url_temp, save_dir)
                except:
                    time.sleep(0.5)
                    try:
                        main.download(url_temp, save_dir)
                    except:
                        continue
            if Config.show_progress:
                 # Formatting and showing downloading procures bar
                 file_display = video_name.split("_")
                 main.show_progress_bar(url_temp, "\r"+file_display[1] + " " +
                                        str(datetime.timedelta(seconds=int(file_display[2]))), save_dir)
            else:
                # Trow a message if the current video file already exist
                sys.stdout.write("\r%s%s File %s successfully downloaded" % (
                    main.bcolors.sb, main.bcolors.fg, video_name + ".mp4"))
                sys.stdout.flush()

            total_counter += 1
            temp_counter += 1

        else:
            # Trow a message if the current video file already exist
            sys.stdout.write("\r%s%s File %s already exist. Skipped!" % (
                   main.bcolors.sb,main.bcolors.fr, video_name + ".mp4"))
            sys.stdout.flush()

        # Show message if all videos from the current course are downloaded
        if counter == len(course):
            courses_count += 1
            sys.stdout.write(
                  "\n%s[%s*%s]%s%sYou have successfully downloaded course %s%s %swith %d videos. Downloaded %d courses and %d videos in total" % (main.bcolors.bm, main.bcolors.fc, main.bcolors.fm, main.bcolors.fc,
                     main.bcolors.sd + main.bcolors.fc, main.bcolors.sb+main.bcolors.fc,course_name,main.bcolors.sd + main.bcolors.fc, temp_counter, courses_count, total_counter)
            )
            sys.stdout.flush()


