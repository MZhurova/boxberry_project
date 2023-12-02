from pathlib import Path

from selene.support.shared import browser
from selene import have, command

import tests


class RegistrationPage:

    def open(self):
 #       browser.open('/automation-practice-form')
        browser.open('/castnym-klientam/dostavka/otpravit_posylku')

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_email(self, value):
        browser.element('#userEmail').type(value)

    def type_fhone_nomber(self, value):
        browser.element('#userNumber').type(value)

    def type_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('[class="react-datepicker__month-select"]').click().element(f'option[value="{month}"]').click()
        browser.element('[class="react-datepicker__year-select"]').click().element(f'option[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def type_gender(self):
        browser.element('label[for="gender-radio-2"]').click()

    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def type_hobbies(self):
        browser.element('label[for="hobbies-checkbox-1"]').click()

    def type_picture(self, value):
        browser.element('#uploadPicture').set_value(str(Path(tests.__file__).parent.joinpath(f'image/{value}').absolute()
    ))

    def type_address(self, value):
        browser.element('#currentAddress').type(value)

    def type_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def type_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def assert_registred_date(self, full_name, email, gender, fhone_nomber, date_of_birth, subjects, hobbies, picture, address, state_and_city):
        browser.element('.table-responsive').all('td:nth-child(2)').should(
            have.texts(full_name, email, gender, fhone_nomber, date_of_birth, subjects, hobbies,
               picture, address, state_and_city))