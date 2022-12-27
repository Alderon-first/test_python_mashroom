from qa_guru_python_3_7.model.pages import practice_form
from qa_guru_python_3_7.model.pages.practice_form import check_info, close_form, send_form, open_page_practice_form


def test_practice_form():
    practice_form.open_page_practice_form()

    # заполнение формы
    practice_form.form_data()

    # отправка формы (нажать на кнопку, проскролив до нее)
    practice_form.send_form()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    # time.sleep(2)

    practice_form.check_info()
    # закрыть форму
    practice_form.close_form()


