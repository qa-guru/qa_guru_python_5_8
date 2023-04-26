
import pytest


# -------------------------------------------------------------------
# Используем объектный подход работы с данными
# -------------------------------------------------------------------


@pytest.fixture
def users():
    pass


@pytest.fixture
def workers(users):
    pass


def test_workers_are_adults_v3(workers):
    for worker in workers:
        assert worker.is_adult()

