import platform
#CHROME_PROFILE_PATH = "user-data-dir=Users/jorgelopez/Library/Application Support/Google/Chrome/Wtsp"
#driver_path = '/home/pi/Dev/whatbot/chromedriver'

so = platform.system()

def driverPath():
    if so == 'Darwin':
        driver_path = '/Users/jorgelopez/Developer/Chromedriver/chromedriver'
    elif so == 'Windows':
        driver_path = 'D:\\chromedriver.exe'
    elif so == 'Linux':
        driver_path = '/usr/bin/chromedriver'
    return driver_path

def profile():
    global CHROME_PROFILE_PATH
    if so == 'Darwin':
        CHROME_PROFILE_PATH = "user-data-dir=Users/jorgelopez/Library/Application Support/Google/Chrome/twitch"
    elif so == 'Windows':
        CHROME_PROFILE_PATH = "user-data-dir=C:\\Usuarios\\jluis\\AppData\\Local\\Google\\Chrome\\twitch"
    elif so == 'Linux':
        CHROME_PROFILE_PATH = "user-data-dir=/home/pi/.config/chromium/Twitch"
    return CHROME_PROFILE_PATH    

