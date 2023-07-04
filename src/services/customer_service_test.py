import pytest
from src.domain.entities.customer import Customer
from datetime import datetime

@pytest.fixture
def in_memory_database():
    return []

def test_create_customer(in_memory_database):
    now = datetime.now()
    customer = Customer(
        login = "login",
        password = "hashed",
        email = "email",
        subscription_id = 1,
        created_at = now,
        modified_at = now
    )
    customer.id = 1
    
    in_memory_database.append(customer)

    assert len(in_memory_database) == 1
    assert customer.id == 1
    assert customer.login == "login"
    assert customer.password == "hashed"
    assert customer.email == "email"
    assert customer.subscription_id == 1
    assert customer.created_at == now
    assert customer.modified_at == now

def test_update_customer(in_memory_database):
    customer = Customer(
        login = "login",
        password = "hashed",
        email = "email",
        subscription_id = 1,
        created_at = datetime.now(),
        modified_at = datetime.now()
    )
    in_memory_database.append(customer)
    
    customer.login = "nigol"
    customer.password = "dehsah"
    customer.email = "liame"
    customer.subscription_id = 2
    
    assert len(in_memory_database) == 1
    assert customer.login == "nigol"
    assert customer.password == "dehsah"
    assert customer.email == "liame"
    assert customer.subscription_id == 2
    
def test_delete_customer(in_memory_database):
    customer = Customer(
        login = "login",
        password = "hashed",
        email = "email",
        subscription_id = 1,
        created_at = datetime.now(),
        modified_at = datetime.now()
    )
    in_memory_database.append(customer)
    
    in_memory_database.remove(customer)
    
    assert len(in_memory_database) == 0
    
def test_get_customer_by_id(in_memory_database):
    first_customer = Customer(
        login = "login",
        password = "hashed",
        email = "email",
        subscription_id = 1,
        created_at = datetime.now(),
        modified_at = datetime.now()
    )
    first_customer.id = 1
    second_customer = Customer(
        login = "login2",
        password = "hashed2",
        email = "email2",
        subscription_id = 2,
        created_at = datetime.now(),
        modified_at = datetime.now()
    )
    second_customer.id = 2
    in_memory_database.extend([first_customer, second_customer])
    
    retrieved_customer = next((c for c in in_memory_database if c.id == 2), None)
    
    assert len(in_memory_database) == 2
    assert retrieved_customer.login == "login2"
    assert retrieved_customer.password == "hashed2"
    assert retrieved_customer.email == "email2"
    assert retrieved_customer.subscription_id == 2
    
def test_get_all_musics(in_memory_database):
    first_customer = Customer(
        login = "login",
        password = "hashed",
        email = "email",
        subscription_id = 1,
        created_at = datetime.now(),
        modified_at = datetime.now()
    )
    second_customer = Customer(
        login = "login2",
        password = "hashed2",
        email = "email2",
        subscription_id = 2,
        created_at = datetime.now(),
        modified_at = datetime.now()
    )
    in_memory_database.extend([first_customer, second_customer])

    all_customers = in_memory_database

    assert len(all_customers) == 2
    assert first_customer in all_customers
    assert second_customer in all_customers 