from qa_guru_python_3_7.model.pages import practice_form
from qa_guru_python_3_7.model.pages.practice_form import check_info, close_form, send_form, open_page_practice_form


def test_practice_form():
    open_page_practice_form()

    # заполнение формы
    practice_form.form_data()

    # отправка формы (нажать на кнопку, проскролив до нее)
    send_form()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    # time.sleep(2)

    check_info()
    # закрыть форму
    close_form()


