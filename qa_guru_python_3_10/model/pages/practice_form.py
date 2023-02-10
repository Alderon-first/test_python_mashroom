from selene import be, have
from selene.support.shared import browser


from qa_guru_python_3_10.utils.resource import path_file

from qa_guru_python_3_10.model.data.user import User
from qa_guru_python_3_10.model.controls.datapiker import Birthday
from qa_guru_python_3_10.model.controls.chekboxes import Hobby
from qa_guru_python_3_10.model.controls.dropdown import Drop
from qa_guru_python_3_10.model.controls.radio_bottom import Gender


class PracticePage:
    def __init__(self):
        pass

    # заполнение формы
    def data_fill(self, user: User):
        browser.element('[id="firstName"]').should(be.blank).type(user.first_name)
        browser.element('[id="lastName"]').should(be.blank).type(user.last_name)
        browser.element('[id="userEmail"]').should(be.blank).type(user.email)
        # радиоботом
        g=Gender('[name=gender]', user.gender)
        g.gender()
        browser.element('[id="userNumber"]').should(be.blank).type(user.phone)
        # загрузка картинки
        browser.element('#uploadPicture').set_value(path_file(user.file))
        # календарь
        d = Birthday('#dateOfBirthInput', year=user.year, month=user.month, day=user.day)
        d.datepicker_react_input()
        # выбор из подобранных вариантов
        browser.element('#subjectsInput').type(user.subject).press_enter()
        # чекбокс
        h = Hobby('.custom-checkbox', user.hobby)
        h.hobby()
        # последовательный выбор из выпадающих списокв
        downstate = Drop('3', user.state)
        downstate.select()
        downcity = Drop('4', user.city)
        downcity.select()
        browser.element('#currentAddress').type(user.address)

    def check_info(self, user: User):
        # проверки
        browser.all('.table-responsive').all('tr').element(1).should(have.text(f'{user.first_name} {user.last_name}'))
        browser.all('.table-responsive').all('tr').element(2).should(have.text(user.email))
        browser.all('.table-responsive').all('tr').element(3).should(have.text(user.gender))
        browser.all('.table-responsive').all('tr').element(4).should(have.text(user.phone))
        d = Birthday('#dateOfBirthInput', year=user.year, month=user.month, day=user.day)
        browser.all('.table-responsive').all('tr').element(5).should(have.text(d.datepicker_birthday_format()))
        browser.all('.table-responsive').all('tr').element(6).should(have.text(user.subject))
        browser.all('.table-responsive').all('tr').element(7).should(have.text(user.hobby))
        browser.all('.table-responsive').all('tr').element(8).should(have.text(user.file.split('/')[-1],))
        browser.all('.table-responsive').all('tr').element(9).should(have.text(user.address))
        browser.all('.table-responsive').all('tr').element(10).should(have.text(f'{user.state} {user.city}'))

    def close_form(self):
        browser.element('#closeLargeModal').press_enter()

    def send_form(self):
        browser.element('#submit').press_enter()

    def open_page_practice_form(self):
        browser.open('/automation-practice-form')
