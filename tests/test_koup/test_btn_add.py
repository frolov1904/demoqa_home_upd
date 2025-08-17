from pages.herokuapp import Herokuapp
from pages.herokuapp_add import Herokuapp_add
def test_btn_add(browser):
    herokuapp=Herokuapp(browser)
    herokuapp_add = Herokuapp_add(browser)
    herokuapp.visit()

    assert herokuapp.add_remove_el.get_text()=='Add/Remove Elements'
    herokuapp.add_remove_el.click()
    assert herokuapp_add.equal_url()

    assert herokuapp_add.add_el.get_text()=='Add Element'

    assert herokuapp_add.add_el.get_dom_attribute('onclick')=='addElement()'

    for i in range(4):
        herokuapp_add.add_el.click()

    assert herokuapp_add.btns_del.check_count_elements(count=4)
    #проверка для всех элементов (кнопок)
    for elems in herokuapp_add.btns_del.find_elements():
        assert elems.text=='Delete'
    #проверка только для первого элемента
    assert herokuapp_add.btns_del.get_text()=='Delete'

    #клики на каждую кнопку Delete
    while herokuapp_add.btns_del.exist():
        herokuapp_add.btns_del.click()

    assert not herokuapp_add.btns_del.exist()