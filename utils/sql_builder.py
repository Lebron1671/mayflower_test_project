from selenium.webdriver.chrome.webdriver import WebDriver

from models.customer import Customer


class SqlBuilder:
    def select_customers_by_filter(self, driver: WebDriver, id=None, city=None):
        if id is not None:
            sql_query = f"SELECT * FROM CUSTOMERS WHERE CustomerID = {id}"
        elif city is not None:
            sql_query = f"SELECT * FROM CUSTOMERS WHERE CITY = '{city}'"
        driver.execute_script("window.editor.setValue(arguments[0]);", sql_query)

    def add_customer(self, driver: WebDriver, new_customer: Customer):
        sql_query = "INSERT INTO CUSTOMERS (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) " \
                    f"VALUES ('{new_customer.id}', " \
                    f"'{new_customer.name}', " \
                    f"'{new_customer.contact_name}', " \
                    f"'{new_customer.address}', " \
                    f"'{new_customer.city}', " \
                    f"'{new_customer.postal_code}', " \
                    f"'{new_customer.country}')"
        driver.execute_script("window.editor.setValue(arguments[0]);", sql_query)

    def update_customer(self, driver: WebDriver, id: int, customer: Customer):
        sql_query = f"UPDATE Customers SET CustomerName = '{customer.name}', " \
                    f"ContactName = '{customer.contact_name}', " \
                    f"Address = '{customer.address}', " \
                    f"City = '{customer.city}', " \
                    f"PostalCode = '{customer.postal_code}', " \
                    f"Country = '{customer.country}' " \
                    f"WHERE CustomerID = {id}"
        driver.execute_script("window.editor.setValue(arguments[0]);", sql_query)

    def delete_customer(self, driver: WebDriver, id: int):
        sql_query = f"DELETE FROM Customers WHERE CustomerID = {id}"
        driver.execute_script("window.editor.setValue(arguments[0]);", sql_query)
