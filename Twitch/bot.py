from . import twitch
from time import sleep

class TwitchBot:
    def __init__(self, user,driver, display=False):
        self.user = user
        self.driver = driver
        self.display = display

    def infinite_coin_collector(self):
        bot = twitch.Twitch(
            user=self.user,
            driver_path=self.driver,
            display=self.display
        )

        coin = True
        while True:
            bot.enter_stream()  
            online = bot.is_online()
            if online:
                loged_in = bot.is_loged_in()
                if not loged_in:
                    bot.login()

                while online:
                    if coin:
                        coin = bot.collect_coins()
                    else:
                        print('Waiting...')
                        sleep(15*60)
                        coin = True
                        if not bot.is_online():
                            break
            else:
                del bot
                bot = twitch.Twitch(
                    user=self.user,
                    driver_path=self.driver,
                    display=self.display
                )
    
    def watch_stream(self):
        bot = twitch.Twitch(
                    user=self.user,
                    driver_path=self.driver,
                    display=self.display
                )

        coin = True
        while True:
            bot.enter_stream()   
            online = bot.is_online()

            if online:
                loged_in = bot.is_loged_in()
                if not loged_in:
                    bot.__login()

                while online:
                    if coin:
                        coin = bot.collect_coins()
                    else:
                        print('Waiting...')
                        sleep(15*60)
                        coin = True
                        if not bot.online():
                            break
            else:
                bot.exit()

    
