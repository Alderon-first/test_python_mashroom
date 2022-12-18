from selene import be, have
from selene.support.shared import browser

import tests_demoqa.resouce


def form_data():
    browser.element('[id="firstName"]').should(be.blank).type('Имя')
    browser.element('[id="lastName"]').should(be.blank).type('Отчество')
    browser.element('[id="userEmail"]').should(be.blank).type('test@test.ru')
    # радиоботом
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('1234567890')
    # загрузка картинки
    browser.element('#uploadPicture').set_value(
        tests_demoqa.resouce.path_file('resourses/текст_1920-1080.jpg'))
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
