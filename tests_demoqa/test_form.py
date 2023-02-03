from qa_guru_python_3_7.model.pages.practice_form import PracticePage
from qa_guru_python_3_7.model.data.user import user


def test_practice_form():

    practice_form.open_page_practice_form()

    # заполнение формы
    practice_form.data_fill(user)

    # отправка формы (нажать на кнопку, проскролив до нее)
    practice_form.send_form()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    # time.sleep(2)

    practice_form.check_info(user)
    # закрыть форму
    practice_form.close_form()


practice_form = PracticePage()

