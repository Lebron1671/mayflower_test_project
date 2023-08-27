import time

from assertpy import assert_that, soft_assertions

from models.customer import Customer
from pages.try_sql_page import TrySqlPage


def compare_result_text(expected_result_text: str, page: TrySqlPage):
    attempts = 3
    while attempts > 0:
        if expected_result_text == page.result_text.text:
            return True
        else:
            time.sleep(3)
            attempts -= 1
    if attempts == 0:
        raise TimeoutError("The expected text did not have time to appear in the allotted time")

# def compare_entries(actual_customer, expected_customer: Customer, check_id: bool):
#     return actual_customer[0].text == str(expected_customer.id) if check_id else actual_customer[0].text \
#             and actual_customer[1].text == expected_customer.name \
#             and actual_customer[2].text == expected_customer.contact_name \
#             and actual_customer[3].text == expected_customer.address \
#             and actual_customer[4].text == expected_customer.city \
#             and actual_customer[5].text == str(expected_customer.postal_code) \
#             and actual_customer[6].text == expected_customer.country

def compare_entries(customer_data, customer: Customer, check_id: bool):
    with soft_assertions():
        assert_that(customer_data[0].text).is_equal_to(str(customer.id) if check_id else customer_data[0].text)
        assert_that(customer_data[1].text).is_equal_to(customer.name)
        assert_that(customer_data[2].text).is_equal_to(customer.contact_name)
        assert_that(customer_data[3].text).is_equal_to(customer.address)
        assert_that(customer_data[4].text).is_equal_to(customer.city)
        assert_that(customer_data[5].text).is_equal_to(str(customer.postal_code))
        assert_that(customer_data[6].text).is_equal_to(customer.country)