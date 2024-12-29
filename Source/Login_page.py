import time

class Login_page_cls:
    def __init__(self,driver):
        self.driver = driver

    def Login_Actions(self, user, pwd):
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(user)
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(pwd)
        self.driver.find_element_by_xpath("//button[normalize-space()='Login']").click()

    def Verify_login_Actions(self,result):

        if result == "Pass":
            assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        else:
            assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com"