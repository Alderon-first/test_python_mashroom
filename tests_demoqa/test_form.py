import time

from selene.support.shared import browser
from selene import be, have, command
import os

def test_practice_form():
    # заполнение формы
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.window_height = 1300
    browser.element('[id="firstName"]').should(be.blank).type('Name1')
    browser.element('[id="lastName"]').should(be.blank).type('LastName1')
    browser.element('[id="userEmail"]').should(be.blank).type('test@test.ru')
    # радиоботом
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('1234567890')
    # календарь
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1990"]').click()
    browser.element('.react-datepicker__month-select [value="11"]').click()
    browser.element('.react-datepicker__day--002').click()
    # выбор из подобранных вариантов
    browser.element('#subjectsInput').type('Arts').press_enter()
    # чекбокс
    browser.all('.custom-checkbox').element_by(have.exact_text('Sports')).click()
    # загрузка картинки
    browser.element('#uploadPicture').send_keys(os.path.abspath('/resourses/текст_1920-1080.jpg'))

    browser.element('#currentAddress').type('currentAddress')
    # последовательный выбор из выпадающих списокв
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    # отправка формы (нажать на кнопку, проскролив до нее)
    browser.element('#submit').press_enter()

    # ожидание 2 секунды, иначе тест не видл формы и падал
    time.sleep(2)


    # проверки
    browser.all('.table-responsive').all('tr').element(1).should(have.text('Имя Отчество'))
    browser.all('.table-responsive').all('tr').element(2).should(have.text('test@test.ru'))
    browser.all('.table-responsive').all('tr').element(3).should(have.text('Other'))
    browser.all('.table-responsive').all('tr').element(4).should(have.text('7777777777'))
    browser.all('.table-responsive').all('tr').element(5).should(have.text('02 December,1990'))
    browser.all('.table-responsive').all('tr').element(6).should(have.text('Arts'))
    browser.all('.table-responsive').all('tr').element(7).should(have.text('Sports'))
    browser.all('.table-responsive').all('tr').element(8).should(have.text('4.jpg'))
    browser.all('.table-responsive').all('tr').element(9).should(have.text('currentAddress'))
    browser.all('.table-responsive').all('tr').element(10).should(have.text('NCR Delhi'))

    browser.element('#closeLargeModal').press_enter()


