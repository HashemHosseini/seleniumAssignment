from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

class POM :
    def __init__(self,driver):

        #All element selectors(can be identified from their variable name):
        self.driver=driver
        self.url="https://demoqa.com/"
        self.scroll="window.scrollTo(400,400)"
        self.elementSelector=(By.CSS_SELECTOR, ".card:nth-child(1) svg")
        self.webTableSelector = (By.ID, "item-3")
        self.addSelector =(By.ID, "addNewRecordButton")
        self.firstNameSelector = (By.ID, "firstName")
        self.lastNameSelector = (By.ID, "lastName")
        self.ageSelector = (By.ID, "age")
        self.emailSelector = (By.ID, "userEmail")
        self.salarySelector = (By.ID, "salary")
        self.departmentSelector = (By.ID, "department")
        self.submitSelector = (By.ID, "submit")
        self.editButtonSelector = (By.CSS_SELECTOR, "#edit-record-4 path")
        self.widgetSelector = (By.CSS_SELECTOR, ".card:nth-child(4) svg")
        self.progressBarSelector = (By.CSS_SELECTOR, ".show #item-4 > .text")
        self.startButtonSelector = (By.ID, "startStopButton")

        self.assertions= (By.CSS_SELECTOR, ".rt-tbody .rt-tr-group")
        self.progressBarAssertionSelector = (By.CSS_SELECTOR, ".progress-bar")
        self.progressBarAttribute= 'aria-valuenow'
        self.greenColorAssertionSelector = 'background-color'

    # Web elements(can be identified from their name):

    def enterURL(self):
        self.driver.get(self.url)

    def scrolling (self):
        self.driver.execute_script(self.scroll)

    def navigateElement(self):
        self.driver.find_element(*self.elementSelector).click()

    def clickOnWebTable(self):
        self.driver.find_element(*self.webTableSelector).click()

    def clickOnAdd(self):
        self.driver.find_element(*self.addSelector).click()

    def enterFirstName(self,firstName):
        self.driver.find_element(*self.firstNameSelector).send_keys(firstName)

    def enterLastName(self,lasttName):
        self.driver.find_element(*self.lastNameSelector).send_keys(lasttName)

    def enterAge(self,age):
        self.driver.find_element(*self.ageSelector).send_keys(age)

    def enterEmail(self,email):
        self.driver.find_element(*self.emailSelector).send_keys(email)

    def enterSalary(self,salary):
        self.driver.find_element(*self.salarySelector).send_keys(salary)

    def enterDepartment(self,department):
        self.driver.find_element(*self.departmentSelector).send_keys(department)

    def clickOnSubmit(self):
        self.driver.find_element(*self.submitSelector).click()

    def clickOnEditButton(self):
        self.driver.find_element(*self.editButtonSelector).click()

    def clearFirstName(self):
        self.driver.find_element(*self.firstNameSelector).clear()

    def clearLasttName(self):
        self.driver.find_element(*self.lastNameSelector).clear()

    def selectNavigateWidget(self):
        self.driver.find_element(*self.widgetSelector).click()

    def selectProgressBar(self):
        self.driver.find_element(*self.progressBarSelector).click()

    def clickOnStartButton(self):
        self.driver.find_element(*self.startButtonSelector).click()

    def TC01Assertion(self):
        rows= self.driver.find_elements(*self.assertions)
        return rows

    def progressAssertion(self):
        progress_bar = self.driver.find_element(*self.progressBarAssertionSelector)
        return progress_bar.get_attribute(self.progressBarAttribute)

    def progressColorAssertion(self):
        progress_bar = self.driver.find_element(*self.progressBarAssertionSelector)
        return progress_bar.value_of_css_property(self.greenColorAssertionSelector)

