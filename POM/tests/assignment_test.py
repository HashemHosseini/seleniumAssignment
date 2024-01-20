from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from POM.pages.pomClass import POM
from POM.pages.testData import testData


@pytest.fixture()
def driver ():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30)
    yield driver
    driver.close()
    driver.quit()

def test_TC01(driver):
    pom= POM(driver)
    user=testData()

    #Scenario A starts form here:
    pom.enterURL()
    pom.scrolling()
    pom.navigateElement()
    time.sleep(1)

    pom.scrolling()
    pom.clickOnWebTable()
    pom.clickOnAdd()
    time.sleep(1)

    pom.enterFirstName(user.firstName)
    pom.enterLastName(user.lastName)
    pom.enterAge(user.age)
    pom.enterEmail(user.email)
    pom.enterSalary(user.salary)
    pom.enterDepartment(user.department)
    pom.clickOnSubmit()
    time.sleep(1)
    pom.scrolling()
    time.sleep(1)

    #Assertion:
    rows = pom.TC01Assertion()
    new_row_data = [user.firstName, user.lastName, str(user.age), user.email, str(user.salary), user.department]
    new_row_added = any(all(data in row.text for data in new_row_data) for row in rows)
    assert new_row_added, "New row was not added or data did not match"


    #Scenario B starts form here:

    pom.scrolling()
    pom.clickOnEditButton()
    pom.clearFirstName()
    pom.enterFirstName(user.editedFirstName)
    pom.clearLasttName()
    pom.enterLastName(user.editedLastName)
    pom.clickOnSubmit()
    time.sleep(1)

    # Assertion:
    rows = pom.TC01Assertion()
    new_row_data = [user.editedFirstName, user.editedLastName, str(user.age), user.email, str(user.salary), user.department]
    new_row_added = any(all(data in row.text for data in new_row_data) for row in rows)
    assert new_row_added, "New row was not added or data did not match"

def test_TC02(driver):
    pom = POM(driver)
    user = testData()

    pom.enterURL()
    pom.scrolling()
    time.sleep(1)

    pom.selectNavigateWidget()
    pom.scrolling()
    time.sleep(1)

    pom.selectProgressBar()
    pom.clickOnStartButton()
    time.sleep(20)

    #Assertion
    progress = pom.progressAssertion()
    assert progress == "100", f"It is not 100%"
    color = pom.progressColorAssertion()
    expected_color = 'rgba(40, 167, 69, 1)'
    assert color == expected_color, f"Color is not green"
