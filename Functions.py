from selenium import webdriver
from pathlib import Path
import urllib.request, ssl, urllib3, os


class Main:

    # Method Driver Return Driver Object
    # @param  browser_type Integer -> Switch between Different Browsers 1-4
    # @param  driver_path  String -> Path to the driver
    ##################################################
    def driver(self, browser_type=1, driver_path='C:/chromedriver.exe'):
        if browser_type == 1:
            driver = webdriver.Chrome(driver_path)
        elif browser_type == 2:
            driver = webdriver.Firefox(driver_path)
        elif browser_type == 3:
            driver = webdriver.Safari(driver_path)
        elif browser_type == 4:
            driver = webdriver.Opera(driver_path)
        else:
            driver = webdriver.Chrome(driver_path)
        return driver

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
