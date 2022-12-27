from selene import be, have
from selene.support.shared import browser

from qa_guru_python_3_7.model.controls.chekboxes import select_chekbox
from qa_guru_python_3_7.model.controls.datapiker import datepicker_react
from qa_guru_python_3_7.model.controls.dropdown import dropdown_react
from qa_guru_python_3_7.utils.resource import path_file
from qa_guru_python_3_7.model.controls.radio_bottom import select_radio


# заполнение формы
def data_fill(firstName, lastName, userEmail, gender, Number,  file, year, month,
              day, Subjects, Hobbies, State, City, Address ):
    browser.element('[id="firstName"]').should(be.blank).type(firstName)
    browser.element('[id="lastName"]').should(be.blank).type(lastName)
    browser.element('[id="userEmail"]').should(be.blank).type(userEmail)
    # радиоботом
    select_radio('[name=gender]', gender)
    browser.element('[id="userNumber"]').should(be.blank).type(Number)
    # загрузка картинки
    browser.element('#uploadPicture').set_value(path_file(file))
    # календарь
    datepicker_react('#dateOfBirthInput', year=year, month=month, day=day)
    # выбор из подобранных вариантов
    browser.element('#subjectsInput').type(Subjects).press_enter()
    # чекбокс
    select_chekbox('.custom-checkbox', Hobbies)
    # последовательный выбор из выпадающих списокв
    dropdown_react('3', State)
    dropdown_react('4', City)
    browser.element('#currentAddress').type(Address)


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


def close_form():
    browser.element('#closeLargeModal').press_enter()


def send_form():
    browser.element('#submit').press_enter()


def open_page_practice_form():
    browser.open('/automation-practice-form')
