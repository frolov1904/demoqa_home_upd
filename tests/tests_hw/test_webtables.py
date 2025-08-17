from pages.webtables import Webtables
import time
from selenium.webdriver.common.keys import Keys
def test1(browser):
    page_webtables = Webtables(browser)
    page_webtables.visit()

    # Очистка всех записей
    while page_webtables.btn_delete_row.exist():
        page_webtables.btn_delete_row.click()
    assert page_webtables.no_data.exist(), "Таблица должна быть пустой после удаления всех записей"

    # Тест пустого заполнения - открыть диалог
    page_webtables.btn_add.click()
    time.sleep(1)
    assert page_webtables.btn_submit.exist(), "Диалог добавления записи должен открыться"

    # Попытка отправить пустую форму
    page_webtables.btn_submit.click()
    time.sleep(1)
    # Диалог не должен закрыться
    assert page_webtables.btn_submit.exist(), "Форма не должна закрыться при пустой отправке"

    # Закрываем диалог клавишей ESC
    page_webtables.btn_submit.send_keys(Keys.ESCAPE)
    time.sleep(1)

    # Тест заполнения формы
    page_webtables.btn_add.click()
    time.sleep(1)
    page_webtables.firstname.send_keys('test')
    page_webtables.lastname.send_keys('testerov')
    page_webtables.email.send_keys('test@test.ru')
    page_webtables.age.send_keys('21')
    page_webtables.salary.send_keys('9999')
    page_webtables.department.send_keys('Dev')
    time.sleep(1)
    page_webtables.btn_submit.click()
    time.sleep(1)

    # Проверяем, что диалог закрыт
    assert not page_webtables.btn_submit.exist(), "Диалог должен закрыться после успешной отправки"


    # Тест редактирования
    page_webtables.btn_edit_row.click()
    time.sleep(1)
    assert page_webtables.firstname.exist(), "Диалог редактирования должен открыться"
    assert page_webtables.firstname.get_dom_attribute("value") == "test", "Имя должно быть заполнено верно"

    # Изменяем имя и сохраняем
    page_webtables.firstname.send_keys(Keys.CONTROL + 'a')
    page_webtables.firstname.send_keys(Keys.DELETE)
    page_webtables.firstname.send_keys('edited')
    time.sleep(1)
    page_webtables.btn_submit.click()
    time.sleep(1)


    # Удаляем запись
    page_webtables.btn_delete_row.click()
    time.sleep(1)

def test2(browser):
    page_webtables=Webtables(browser)
    page_webtables.visit()
    page_webtables.rows.scroll_to_element()
    page_webtables.rows.click()
    time.sleep(2)
    page_webtables.rows.send_keys(Keys.ARROW_UP)
    page_webtables.rows.send_keys(Keys.ENTER)
    time.sleep(2)
    #кликаем по заблокированным эллементам
    try:
        page_webtables.btn_prev.click()
        page_webtables.btn_next.click()
    except Exception:
        pass

    assert page_webtables.btn_next.get_dom_attribute('disabled'), "Кнопка Next должна быть заблокирована"
    assert page_webtables.btn_prev.get_dom_attribute('disabled'), "Кнопка Previous должна быть заблокирована"
    #создаем 3 доп пользователя
    for i in range(3):
        page_webtables.btn_add.click()
        time.sleep(2)
        page_webtables.firstname.send_keys(f'First{i}')
        page_webtables.lastname.send_keys(f'Last{i}')
        page_webtables.email.send_keys(f'test{i}@example.com')
        page_webtables.age.send_keys('30')
        page_webtables.salary.send_keys('1000')
        page_webtables.department.send_keys('QA')
        time.sleep(2)
        page_webtables.btn_submit.click()
        time.sleep(2)
    assert page_webtables.total_pages.get_text()=='2'
    assert not page_webtables.btn_next.get_dom_attribute('disabled'), "Кнопка Next разблокирована"
    page_webtables.btn_next.click()
    assert not page_webtables.btn_prev.get_dom_attribute('disabled'), "Кнопка Previous разблокирована"
    time.sleep(2)
    page_webtables.btn_prev.click()

