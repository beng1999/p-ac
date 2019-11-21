from selenium import webdriver
from pages.home.loginmethod import Login
from pages.home.autocommenting import AutoCommenting
import time

class PinterestPoster():
    baseURL = "https://www.pinterest.ca/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(baseURL)

    lg = Login(driver)
    comment = AutoCommenting(driver)

    def testPost(self):
        self.lg.loginMethod()
        #self.postimg.ImageAutomation()
        #self.pinner.PinningAutomation()
        #self.follow.FollowingAutomation()
        self.comment.CommentingAutomation()
        time.sleep(2)

ff = PinterestPoster()
ff.testPost()