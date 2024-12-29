import time
import pytest
from Source.Login_page import Login_page_cls
import openpyxl
from utilities.logging import Logs
from selenium.webdriver.common.keys import Keys

#  Code for to generate log files in Logs folder
logger = Logs.Log_Gen()

# Function to read data from Excel file.


def Read_test_data():
    # Code to load the data from Excel file
    workbook = openpyxl.load_workbook(filename=r"C:\Users\shaik\PycharmProjects\pythonProject\4_Keyword_Driven_Framework\Data\keyword_driven_framework.xlsx")
    sheet = workbook["Sheet1"]
    data_list = []  # Creating empty list to add every row of Excel file data as a tuple(row).
    #  Adding data to data_list from excel file.
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password, expected_result, keyword = row
        #  Here two brackets using one is append() method, 2nd bracket if for tuple.
        data_list.append((username, password, expected_result, keyword))
    return data_list
#  Calling function (test_data is 'a' object of Read_test_data function)


test_data = Read_test_data()


@pytest.mark.parametrize("usn, pd, exp_result, key", test_data)
def test_Loginpage(usn, pd, exp_result, key, Login_Setup):
    logger.info("**********  Test_001_Login_Keyword **********")
    driver = Login_Setup  # Driver holding webpage

    login_obj = Login_page_cls(driver)  # This class display user and pwd and login elements
    logger.info(f"Starting Keyword Driven Test with Actions '{key}'.")

    if key == 'Login':
        time.sleep(6)
        login_obj.Login_Actions(usn, pd)
        time.sleep(5)
        login_obj.Verify_login_Actions(exp_result)
        time.sleep(5)
    elif key == 'Add Employee':
        time.sleep(6)
        login_obj.Login_Actions(usn, pd)
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='PIM']").click()
        time.sleep(4)
        # navigating to "Add Employee" tab
        driver.find_element_by_xpath("//a[normalize-space()='Add Employee']").click()
        time.sleep(4)
        # Entering employee details.
        driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Dudekula")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Middle Name']").send_keys("shaik")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("shavali")
        time.sleep(2)
        empid = driver.find_element_by_xpath("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        driver.execute_script("arguments[0].value='';", empid)
        empid.send_keys(Keys.CONTROL + "a")  # Select all text
        empid.send_keys(Keys.BACKSPACE)

        empid.send_keys("7776")

        time.sleep(2)
        driver.find_element_by_xpath("//button[normalize-space()='Save']").click()
        time.sleep(2)

    elif key == "Report":
        time.sleep(6)
        login_obj.Login_Actions(usn, pd)
        time.sleep(5)
        driver.find_element_by_xpath("//a[normalize-space()='PIM']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//a[normalize-space()='Reports']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//input[@placeholder='Type for hints...']").send_keys("PIM Sample Report")
        time.sleep(4)
        driver.find_element_by_xpath("//button[normalize-space()='Search']").click()
    else:
        driver.close()
        print("No actions found!")
