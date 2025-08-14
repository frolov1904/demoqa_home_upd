from pages.text_box import TextBox

def test_text_box(browser):
    test_name = "test" #ожидаемые данные для ввода
    test_address = "test"

    text_box_page=TextBox(browser)
    text_box_page.visit()

    text_box_page.name.send_keys('test')
    text_box_page.currentAddress.send_keys('test')
    text_box_page.btn_submit.click_force()

    # Проверяем вывод
    assert test_name==text_box_page.name_output.get_text(), \
        f"В имени ожидалось '{test_name}', но было '{text_box_page.name_output.get_text()}'"

    assert test_address==text_box_page.currentAddress_output.get_text(), \
        f"В адресе ожидалось '{test_address}', но было '{text_box_page.currentAddress_output.get_text()}'"