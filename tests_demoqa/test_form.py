from selene.support.shared import browser

from qa_guru_python_3_7.model.pages import practice_form
from qa_guru_python_3_7.model.pages.practice_form import check_info


def test_practice_form():
    browser.open('/automation-practice-form')

    # заполнение формы
    practice_form.form_data()

    # отправка формы (нажать на кнопку, проскролив до нее)
    browser.element('#submit').press_enter()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    # time.sleep(2)

    check_info()
    # закрыть форму
    browser.element('#closeLargeModal').press_enter()
