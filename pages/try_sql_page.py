from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TrySqlPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.XPATH, ".//button[@class = 'ws-btn']")))

    def wait_for_table(self):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//div[@id = 'divResultSQL']//table[@class = 'ws-table-all notranslate']")))

    def perform_query_with_table_result(self):
        self.run_query_button.click()
        self.wait_for_table()
        return self.result_table_rows

    @property
    def result_text(self):
        return self.driver.find_element(By.ID,'divResultSQL')

    @property
    def result_table(self):
        return self.driver.find_element(By.XPATH, "//div[@id = 'divResultSQL']//table[@class = 'ws-table-all notranslate']//tbody")

    @property
    def result_table_rows(self):
        table = self.result_table
        return table.find_elements(By.TAG_NAME, "tr")

    @property
    def query_textarea(self):
        return self.driver.find_element(By.XPATH, "//textarea[@id = 'textareaCodeSQL']")

    @property
    def run_query_button(self):
        return self.driver.find_element(By.XPATH, ".//button[@class = 'ws-btn']")
