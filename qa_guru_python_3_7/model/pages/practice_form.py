from selene import be, have
from selene.support.shared import browser

import qa_guru_python_3_7.utils.resouce_1
import tests_demoqa.resouce


# заполнение формы
def form_data():
    browser.element('[id="firstName"]').should(be.blank).type('Имя')
    browser.element('[id="lastName"]').should(be.blank).type('Отчество')
    browser.element('[id="userEmail"]').should(be.blank).type('test@test.ru')
    # радиоботом
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('1234567890')
    # загрузка картинки
    #browser.element('#uploadPicture').set_value(tests_demoqa.resouce.path_file('resource/текст_1920-1080.jpg'))
    browser.element('#uploadPicture').set_value(qa_guru_python_3_7.utils.resouce_1.path_file(
        '/resource/текст_1920-1080.jpg'))
    # календарь
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1990"]').click()
    browser.element('.react-datepicker__month-select [value="11"]').click()
    browser.element('.react-datepicker__day--002').click()
    # выбор из подобранных вариантов
    browser.element('#subjectsInput').type('Arts').press_enter()
    # чекбокс
    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    # последовательный выбор из выпадающих списокв
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#currentAddress').type('currentAddress')


def check_info():
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
