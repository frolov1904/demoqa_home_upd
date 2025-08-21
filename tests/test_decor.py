import pytest

from pages.demoqa import Demoqa
@pytest.mark.skip
def test_decor(browser):
    demoqa=Demoqa(browser)
    demoqa.visit()

    assert demoqa.h5.check_count_elements(6)
    for elem in demoqa.h5.find_elements():
        assert elem.text!=''