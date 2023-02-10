from qa_guru_python_3_10.model.pages.practice_form import PracticePage
from qa_guru_python_3_10.model.data.user import user


def test_practice_form():

    practice_form.open_page_practice_form()

    practice_form.data_fill(user)# заполнение формы

    practice_form.send_form()# отправка формы (нажать на кнопку, проскролив до нее)

    # time.sleep(2)  # ожидание 2 секунды, иначе тест не видл формы и падал

    practice_form.check_info(user)# проверка данных

    practice_form.close_form()# закрыть форму


practice_form = PracticePage()

