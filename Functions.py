from selenium import webdriver
from pathlib import Path
import urllib.request, ssl, urllib3, os
import Config
from selenium.webdriver.chrome.options import Options


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
    ###################################################
    # Background Color Function
    ###################################################
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

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

    def getSize(self, filename):
            st = os.stat(filename)
            return st.st_size
    ##################################################

    #  Method checking whether the directory exists or not
    # @param  Directory Path String
    ###################################################
    def dir_exist(self, path):
        if Path(path).is_dir():
            return True
        else:
            return False
