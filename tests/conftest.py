from core.locator import *
from core.config import *
import pytest
from core.checkpoint import CheckPoint
from core.locator import Locator
from core import config
import allure


@pytest.fixture()
def check():
    return CheckPoint()


@pytest.fixture()
def get_visit_result():
    return int(VISIT_RESULT)


@pytest.fixture(scope="function")
def locator(request):
    def close_browser():
        l.close

    request.addfinalizer(close_browser)
    l = Locator()
    l.go_to(TEST_URL[0])
    l.maximize_the_window
    l.wait(2)
    return l


