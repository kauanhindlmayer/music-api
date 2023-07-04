import pytest
from src.domain.entities.subscription import Subscription

@pytest.fixture
def in_memory_database():
    return []

def test_create_subscription(in_memory_database):
    subscription = Subscription(description='Monthly Plan', value=10, limit=100)
    subscription.id = 1
    in_memory_database.append(subscription)

    assert len(in_memory_database) == 1
    assert subscription.id == 1
    assert subscription.description == 'Monthly Plan'
    assert subscription.value == 10
    assert subscription.limit == 100

def test_update_subscription(in_memory_database):
    subscription = Subscription(description='Monthly Plan', value=10, limit=100)
    in_memory_database.append(subscription)

    subscription.description = 'Yearly Plan'
    subscription.value = 100
    subscription.limit = 1000

    assert subscription.description == 'Yearly Plan'
    assert subscription.value == 100
    assert subscription.limit == 1000

def test_delete_subscription(in_memory_database):
    subscription = Subscription(description='Monthly Plan', value=10, limit=100)
    in_memory_database.append(subscription)

    in_memory_database.remove(subscription)

    assert len(in_memory_database) == 0

def test_get_subscription_by_id(in_memory_database):
    first_subscription = Subscription(description='Monthly Plan', value=10, limit=100)
    first_subscription.id = 1
    second_subscription = Subscription(description='Yearly Plan', value=100, limit=1000)
    second_subscription.id = 2
    in_memory_database.extend([first_subscription, second_subscription])

    retrieved_subscription = next((s for s in in_memory_database if s.id == 2), None)

    assert retrieved_subscription.description == 'Yearly Plan'
    assert retrieved_subscription.value == 100
    assert retrieved_subscription.limit == 1000

def test_get_all_subscriptions(in_memory_database):
    first_subscription = Subscription(description='Monthly Plan', value=10, limit=100)
    second_subscription = Subscription(description='Yearly Plan', value=100, limit=1000)
    in_memory_database.extend([first_subscription, second_subscription])

    all_subscriptions = in_memory_database

    assert len(all_subscriptions) == 2
    assert first_subscription in all_subscriptions
    assert second_subscription in all_subscriptions