import random

from faker import Faker
from selenium.webdriver.common.by import By

from models.customer import Customer
from pages.try_sql_page import TrySqlPage


def generate_random_customer(customer_id: int) -> Customer:
    fake = Faker()
    address = fake.address().replace("\n", " ").replace("\r", " ")

    return Customer(
        id=customer_id,
        name=fake.name(),
        contact_name=fake.name(),
        address=address,
        city=fake.city(),
        postal_code=int(fake.postcode()),
        country=fake.country()
    )

def prepare_new_customer(page: TrySqlPage):
    page.run_query_button.click()
    page.wait_for_table()
    customers_table_rows = page.result_table_rows
    last_customer_columns = customers_table_rows[-1].find_elements(By.TAG_NAME, "td")
    max_customer_id = last_customer_columns[0].text
    return generate_random_customer(int(max_customer_id) + 1)

def get_random_customer(table_rows):
    random_customer = random.choice(table_rows[1:])
    random_customer_columns = random_customer.find_elements(By.TAG_NAME, "td")
    return random_customer_columns[0].text
