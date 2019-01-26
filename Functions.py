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


from selenium import webdriver
from pathlib import Path
from tqdm import tqdm
from colorama import init, Fore, Back, Style
import urllib.request, urllib.request, ssl, urllib3, Config, os

class Main:

    # Method Driver Return Driver Object
    # @param  browser_type Integer -> Switch between Different Browsers 1-4
    # @param  driver_path  String -> Path to the driver
    ##################################################
    def driver(self, browser_type=1, driver_path='C:/chromedriver.exe'):
        if browser_type == 1:
            driver = webdriver.Chrome(driver_path, chrome_options=self.build_chrome_options())
        elif browser_type == 2:
            driver = webdriver.Firefox(driver_path)
        elif browser_type == 3:
            driver = webdriver.Safari(driver_path)
        elif browser_type == 4:
            driver = webdriver.Opera(driver_path)
        else:
            driver = webdriver.Chrome(driver_path)
        return driver

    def build_chrome_options (self, profile_dir = Config.profile_dr):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_untrusted_certs = True
        chrome_options.assume_untrusted_cert_issuer = True
        # chrome configuration
        # More: https://github.com/SeleniumHQ/docker-selenium/issues/89
        # And: https://github.com/SeleniumHQ/docker-selenium/issues/87
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
        chrome_options.add_argument("--disable-impl-side-painting")
        chrome_options.add_argument("--user-data-dir=" + os.path.abspath(profile_dir))
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_argument("--disable-seccomp-filter-sandbox")
        chrome_options.add_argument("--disable-breakpad")
        chrome_options.add_argument("--disable-client-side-phishing-detection")
        chrome_options.add_argument("--disable-cast")
        chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
        chrome_options.add_argument("--disable-cloud-import")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-session-crashed-bubble")
        chrome_options.add_argument("--disable-ipv6")
        chrome_options.add_argument("--allow-http-screen-capture")
        return chrome_options
        ##################################################

    # Static Method Download Download File
    ###################################################
    @staticmethod
    def download(url, names):
        urllib3.disable_warnings()

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        if urllib.request.urlretrieve(url, names):
            return True
        else:
            return False

    ##################################################
    #  Progress bar Class tqdm
    ###################################################
    class progress_bar(tqdm):
        def update_to(self, b=1, bsize=1, tsize=None):
            if tsize is not None:
                self.total = tsize
            self.update(b * bsize - self.n)

    def show_progress_bar(self, url, filename, output_path):
        with self.progress_bar(unit='B',smoothing=0.3, unit_scale=True,
                                 miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

    ##################################################
    #  Background and Font Colours
    # Reference => *Nasir Khan (r0ot h3x49)  - **https://github.com/r0oth3x49** ##*
    ###################################################
    class bcolors:
        if os.name == "posix":
            init(autoreset=True)
            # colors foreground text:
            fc = "\033[0;96m"
            fg = "\033[0;92m"
            fw = "\033[0;97m"
            fr = "\033[0;91m"
            fb = "\033[0;94m"
            fy = "\033[0;33m"
            fm = "\033[0;35m"

            # colors background text:
            bc = "\033[46m"
            bg = "\033[42m"
            bw = "\033[47m"
            br = "\033[41m"
            bb = "\033[44m"
            by = "\033[43m"
            bm = "\033[45m"

            # colors style text:
            sd = Style.DIM
            sn = Style.NORMAL
            sb = Style.BRIGHT
        else:
            init(autoreset=True)
            # colors foreground text:
            fc = Fore.CYAN
            fg = Fore.GREEN
            fw = Fore.WHITE
            fr = Fore.RED
            fb = Fore.BLUE
            fy = Fore.YELLOW
            fm = Fore.MAGENTA

            # colors background text:
            bc = Back.CYAN
            bg = Back.GREEN
            bw = Back.WHITE
            br = Back.RED
            bb = Back.BLUE
            by = Fore.YELLOW
            bm = Fore.MAGENTA

            # colors style text:
            sd = Style.DIM
            sn = Style.NORMAL
            sb = Style.BRIGHT

    ##################################################
    #  Method Waits wait time
    # @param  wait Integer
    ###################################################

    def waits(self, wait):
        self.driver().implicitly_wait(wait)

    ##################################################
    #  Method Maximizing Window
    # @param  m_window Boolean -> True by Default
    ###################################################

    def max_window(self, m_window=True):
        if m_window:
            self.driver().maximize_window()

    ##################################################
    #  Method Looking for file existence before downloading
    # @param  m_window Boolean -> True by Default
    ###################################################
    def file_exist(self, path):

        if Path(path).is_file():
            return True
        else:
            return False

    ##################################################
    #  Method checking whether the directory exists or not
    # @param  Directory Path String
    ###################################################
    def dir_exist(self, path):
        if Path(path).is_dir():
            return True
        else:
            return False
