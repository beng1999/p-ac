from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.keys import Keys
import time

class AutoCommenting(BasePage):

    def __init__(self, driver):
        super().__init__(self)
        self.driver = driver
        self.sl = SeleniumDriver(driver)

    #Locator
    _comment_tab_1 = "//a[@aria-selected='false']"
    _comment_tab_2 = "//button[@aria-label='Show more']"
    _comment_input = "//div[@role='textbox']"
    _comment_send_button = "//div[contains(text(), 'Done')]//parent::button"

    def inputSearch(self, search="Save the bees"):
        element = self.sl.getElement(self._search_bar, locatorType="xpath")
        element.send_keys(search)
        element.send_keys(Keys.ENTER)

    def pressCommentTab(self):
        commentTab1 = self.elementPresenceCheck(self._comment_tab_1, byType="xpath")
        commentTab2 = self.elementPresenceCheck(self._comment_tab_2, byType="xpath")

        if commentTab1:
            self.elementClick(self._comment_tab_1, locatorType="xpath")
        elif commentTab2:
            self.elementClick(self._comment_tab_2, locatorType="xpath")
        else:
            self.inputSearch()

    def inputComment(self, comment="Awesome picture! "):
        self.sendKeys(comment, self._comment_input, locatorType="xpath")

    def sendComment(self):
        self.elementClick(self._comment_send_button, locatorType="xpath")

    def imageCommenting(self, username = "Save The Bees"):
        for i in range(1, 11):
            _images = "//*[@id='__PWS_ROOT__']/div[1]/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div[" + str(i) + "]/div/div/div/div/div/div/div[1]/a"

            self.elementClick(_images, locatorType="xpath")
            time.sleep(2)
            self.pressCommentTab()
            time.sleep(1)

            userMessage = "//img[@alt='" + str(username) + "']"
            didIMessage = self.elementPresenceCheck(username, byType="xpath")

            if didIMessage is not True:
                self.inputComment()
                time.sleep(1)
                self.sendComment()
                time.sleep(1)
                self.inputSearch()
                time.sleep(2)
            else:
                self.inputSearch()

    def CommentingAutomation(self):
        self.inputSearch()
        self.imageCommenting()