from qa_guru_python_3_7.model.pages import practice_form
from qa_guru_python_3_7.model.pages.practice_form import check_info, close_form, send_form, open_page_practice_form


def test_practice_form():
    practice_form.open_page_practice_form()

    # заполнение формы
    practice_form.data_fill(firstName='Имя', lastName='Отчество',
                            userEmail='test@test.ru', gender='Female', Number='1234567890',
                            file='resource/текст_1920-1080.jpg', year='1990', month='11', day='02',
                            Subjects='Arts', Hobbies='Sports', State='NCR', City='Delhi', Address='currentAddress')

    # отправка формы (нажать на кнопку, проскролив до нее)
    practice_form.send_form()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    # time.sleep(2)

    practice_form.check_info(firstName='Имя', lastName='Отчество', userEmail='test@test.ru', gender='Female',
                             Number='1234567890', file='текст_1920-1080.jpg',
                             date='02 December,1990', Subjects='Arts', Hobbies='Sports', State='NCR',
                             City='Delhi', Address='currentAddress')
    # закрыть форму
    practice_form.close_form()


