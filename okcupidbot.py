from selenium import webdriver
import time
from account_details import username, password

class OKCupidBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def open(self):
        self.driver.get("https://www.okcupid.com/home")
        time.sleep(3)

    def sign_in(self):
        email_input = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_input.send_keys(password)

        next_btn = self.driver.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input')
        next_btn.click()

    def pass_dislike(self):
        time.sleep(8)
        pass_btn = self.driver.find_element_by_xpath('//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[1]')
        pass_btn.click()

    def like_like(self):
        time.sleep(8)
        like_btn = self.driver.find_element_by_xpath('//*[@id="quickmatch-wrapper"]/div/div/span/div/div[2]/div/div[2]/span/div/div/div/div[1]/div[2]/button[2]')
        like_btn.click()

    def auto_like(self):
        while True:
            time.sleep(1)
            try:
                self.like_like()
            except Exception:
                    try:
                        self.close_popup()
                    except:
                        self.close_popup2()

    def close_popup(self):
        close_btn = self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
        close_btn.click()

    def close_popup2(self):
        close2_btn = self.driver.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[1]/button')
        close2_btn.click()








bot = OKCupidBot()
bot.open()
bot.sign_in()
bot.auto_like()



