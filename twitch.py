import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import driverPath, profile
from datetime import datetime
from time import sleep, time

import secret

class TwitchBot():
    _stream = False
    def __init__(self, user):
        self.user = user
        option = webdriver.ChromeOptions()
        #option.add_argument('--headless')  
        option.add_argument(profile())
        self.bot = webdriver.Chrome(executable_path=driverPath() ,options=option)
        global bot
        bot = self.bot
        self.url = "https://www.twitch.tv/" + user

    def __login(self):
        login_button = bot.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div')
        login_button.click()

        sleep(2)
        user = bot.find_element_by_id('login-username')
        user.send_keys(secret.usr)
        sleep(1)
        psswd = bot.find_element_by_id('password-input')
        psswd.send_keys(secret.psswd)
        sleep(1)
        login_button = bot.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div')
        login_button.click()

    def __is_loged_in(self):
        try:
            WebDriverWait(bot, 4).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div')))
            return False
        except:
            print('Alredy loged in')
            return True

    def __enter_stream(self):
        bot.get(self.url)
        #bot.find_element_by_class_name('tw-channel-status-text-indicator')

    def watch_stream(self):
        coin = True
        i = 0
        #self.__enter_stream()
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
                        print('hola')
                        sleep(15*60)
                        coin = True

                    i+=1
                    if i > 5:
                        i = 0
                        online = self.__is_online()
            else:
                self.__close_stream()

    def __is_online(self):
        try:
            login_button = '//*[@id="root"]/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/a/div[2]/div/div/div'
            WebDriverWait(bot, 4).until(EC.presence_of_element_located((By.XPATH, login_button)))
            print(f'{self.user} is online, {datetime.now()}')
            return True
            
        except TimeoutException:
            print(f"{self.user} is not online! {datetime.now()}")
            return False 
            
    def __collect_coins(self):
        button = '/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button/span'
        try:
            WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, button))).click()
            #bot.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button/span').click()
            print(f'Coin Collected {datetime.now()}')
            return False
        except TimeoutException:
            return True

        """ reward_button = bot.find_element_by_xpath(button)
        reward_button.click()
        return False """
            



    def __close_stream(self):
        bot.get("https://google.com")
        sleep(60*120)
    

if __name__ == "__main__":
    twitch = TwitchBot("mym_alkapone")
    #twitch = TwitchBot("esl_csgo")

    twitch.watch_stream()
    
