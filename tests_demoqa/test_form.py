from selene.support.shared import browser
from selene import have

from qa_guru_python_3_7.model.pages import practice_form


def test_practice_form():
    browser.open('/automation-practice-form')

    # заполнение формы
    practice_form.form_data()

    # отправка формы (нажать на кнопку, проскролив до нее)
    browser.element('#submit').press_enter()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    #time.sleep(2)

    # проверки
    browser.all('.table-responsive').all('tr').element(1).should(have.text('Имя Отчество'))
    browser.all('.table-responsive').all('tr').element(2).should(have.text('test@test.ru'))
    browser.all('.table-responsive').all('tr').element(3).should(have.text('Female'))
    browser.all('.table-responsive').all('tr').element(4).should(have.text('1234567890'))
    browser.all('.table-responsive').all('tr').element(5).should(have.text('02 December,1990'))
    browser.all('.table-responsive').all('tr').element(6).should(have.text('Arts'))
    browser.all('.table-responsive').all('tr').element(7).should(have.text('Sports'))
    browser.all('.table-responsive').all('tr').element(8).should(have.text('текст_1920-1080.jpg'))
    browser.all('.table-responsive').all('tr').element(9).should(have.text('currentAddress'))
    browser.all('.table-responsive').all('tr').element(10).should(have.text('NCR Delhi'))
    # закрыть форму
    browser.element('#closeLargeModal').press_enter()
