import allure
import pytest

from selenium.webdriver.common.by import By

from pages.try_sql_page import TrySqlPage
from utils.data_generator import prepare_new_customer, get_random_customer
from utils.data_comparison import compare_result_text, compare_entries
from utils.sql_builder import SqlBuilder


class TestCustomerSqlOperations:
    sql_builder = SqlBuilder()

    @allure.description("Check that there is the customer with ContactName = 'Giovanni Rovelli' and Address = 'Via Ludovico il Moro 22'")
    @pytest.mark.usefixtures("get_driver")
    def test_get_all_customers(self):
        # Prerequisite part
        expected_customer_name = "Giovanni Rovelli"
        expected_customer_address = "Via Ludovico il Moro 22"

        page = TrySqlPage(self.driver)
        page.open()

        # Action part
        table_rows = page.perform_query_with_table_result()

        found = False
        for row in table_rows[1:]:
            columns = row.find_elements(By.TAG_NAME, "td")
            if columns[2].text == expected_customer_name:
                assert columns[3].text == expected_customer_address
                found = True
                break

        # Assertation part
        assert found, "Desired row not found in the table"

    @allure.description("Check that exist 6 customer from London in the table")
    @pytest.mark.usefixtures("get_driver")
    def test_get_customers_from_london(self):
        # Prerequisite part
        expected_length_of_customers = 6

        page = TrySqlPage(self.driver)
        page.open()

        # Action part
        self.sql_builder.select_customers_by_filter(self.driver, city='London')
        table_rows = page.perform_query_with_table_result()

        # Assertation part
        assert len(table_rows[1:]) == expected_length_of_customers

    @allure.description("Check that we can add new customer to the table")
    @pytest.mark.usefixtures("get_driver")
    def test_add_customer(self):
        # Prerequisite part
        page = TrySqlPage(self.driver)
        page.open()
        generated_customer = prepare_new_customer(page)

        # Action part
        self.sql_builder.add_customer(self.driver, generated_customer)
        page.run_query_button.click()
        compare_result_text('You have made changes to the database. Rows affected: 1', page)
        self.sql_builder.select_customers_by_filter(self.driver, id=generated_customer.id)
        table_rows = page.perform_query_with_table_result()
        added_customer_columns = table_rows[1].find_elements(By.TAG_NAME, "td")

        # Assertation part
        compare_entries(added_customer_columns, generated_customer, check_id=True)

    @allure.description("Check that we can update existed customer in the table")
    @pytest.mark.usefixtures("get_driver")
    def test_update_customer(self):
        # Prerequisite part
        page = TrySqlPage(self.driver)
        page.open()
        generated_customer = prepare_new_customer(page)

        # Action part
        table_rows = page.perform_query_with_table_result()
        random_customer_id = get_random_customer(table_rows)
        self.sql_builder.update_customer(self.driver, random_customer_id, generated_customer)
        page.run_query_button.click()
        compare_result_text('You have made changes to the database. Rows affected: 1', page)
        self.sql_builder.select_customers_by_filter(self.driver, id=random_customer_id)
        table_rows = page.perform_query_with_table_result()
        updated_customer_columns = table_rows[1].find_elements(By.TAG_NAME, "td")

        # Assertation part
        compare_entries(updated_customer_columns, generated_customer, check_id=False)

    @allure.description("Check that we can delete any customer from the table")
    @pytest.mark.usefixtures("get_driver")
    def test_delete_customer(self):
        # Prerequisite part
        page = TrySqlPage(self.driver)
        page.open()

        # Action part
        table_rows = page.perform_query_with_table_result()
        random_customer_id = get_random_customer(table_rows)
        self.sql_builder.delete_customer(self.driver, random_customer_id)
        page.run_query_button.click()
        compare_result_text('You have made changes to the database. Rows affected: 1', page)
        self.sql_builder.select_customers_by_filter(self.driver, id=random_customer_id)
        page.run_query_button.click()

        # Assertation part
        assert compare_result_text('No result.', page), "The values don't match"
