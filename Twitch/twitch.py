from selenium.common.exceptions import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
from time import sleep

HOUR = 60**2

class Twitch:
    _stream = False
    def __init__(self, driver, user, username, password):
        """Twitch bot

        Args:
            driver (WebDriver): Webdriver Object
            user (str): Channel username
            username (str): Login username
            password (str): User password
        """
        global bot
        self.user = user
        self.username = username
        self.password = password
        bot = driver
        
        self.url = "https://www.twitch.tv/" + user

    def login(self):
        """Login
        Log in into Twitch Account
        """
        login_button = bot.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div')
        login_button.click()
        sleep(2)
        username = bot.find_element_by_id('login-username')
        username.send_keys(self.username)
        sleep(1)
        psswd = bot.find_element_by_id('password-input')
        psswd.send_keys(self.password)
        sleep(1)
        login_button = bot.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div')
        login_button.click()

    def is_loged_in(self):
        """Is loged in

        Returns:
            bool: Return True or False depending on account status
        """
        try:
            WebDriverWait(bot, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div')))
            return False
        except:
            print('Alredy loged in')
            return True

    def enter_stream(self):
        bot.get(self.url)

    def watch_stream(self):
        coin = True
        i = 0
        while True:
            self.__enter_stream()   
            online = self.__is_online()

            if online:
                loged_in = self.__is_loged_in()
                if not loged_in:
                    self.__login()

                while online:
                    if coin:
                        coin = self.__collect_coins()
                    else:
                        print('Waiting...')
                        sleep(15*60)
                        coin = True
                        if not self.__is_online():
                            break
            else:
                self.__close_stream()

    def is_online(self):
        try:
            online_button = '//div[@aria-label="Channel is Live"]'
            WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, online_button)))
            print(f'{self.user} is online, {datetime.now()}')
            return True
        except TimeoutException:
            print(f"{self.user} is not online! {datetime.now()}")
            return False 
    
    def online(self):
        try:
            online_button = '//div[@aria-label="Channel is Live"]'
            WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, online_button)))
            return True
        except TimeoutException:
            return False 
            
    def collect_coins(self):
        button = "//button[@aria-label='Claim Bonus']"
        try:
            try:
                WebDriverWait(bot, 15).until(EC.presence_of_element_located((By.XPATH, button))).click()
            except ElementNotInteractableException:
                pass
            
            print(f'Coin Collected {datetime.now()}')

        except TimeoutException:
            print(f'Coin not available {datetime.now()}')
        return False

    def close_stream(self):
        bot.get("https://google.com")
        sleep(60**2)
    
    def __del__(self):
        print("Stream closed")
        bot.quit()
        sleep(HOUR * 4)

    def exit(self):
        bot.quit()