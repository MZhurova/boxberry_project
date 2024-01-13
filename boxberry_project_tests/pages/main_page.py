from selene import browser, have


class MainPage:

    def open(self):
        browser.open('')
        browser.element('.modal-new-year__btn_cancel').click()

    def select_city(self, city):
        browser.element('.town__link').click()
        browser.all('.town-popup__item').element_by(have.text('Россия')).click()
        browser.element('[placeholder = "Поиск города"]').type(city)
        browser.element('.town-popup__item-city').click()

    def assert_city(self, city):
        browser.element('.town__link').should(have.text(city))

    def view_list_personal_account(self):
        browser.element('.header__profile').click()

    def verification_city(self):
        browser.element('[type = "button"]').click()

    def choose_im(self):
        browser.all('.personal-accounts__text').element_by(have.text('Для интернет-магазинов')).click()
        browser.switch_to_previous_tab()

    def assert_personal_account(self):
        browser.element('.login-reg__tab').should(have.text('Вход в личный кабинет'))

    def open_page_im(self):
        browser.open('https://account.boxberry.ru/')

    def input_login_im(self):
        browser.element('#authorizationform-email').type('ЛОГИН')

    def forgot_password(self):
        browser.element('.login-reg__fc').click()

    def assert_open_page_password_recovery(self):
        browser.element('.password-recovery__h').should(have.text('Восстановление пароля'))

    def parsel_tracking(self, nomber_parcel):
        browser.element('.field-input__inner.form-bar-desktop__input').type(nomber_parcel)
        browser.element('[aria-label="Поиск"]').click()

    def status_parcel(self):
        browser.element('.track-details-item__body').should(
            have.text('Получена информация о заказе. Отправление еще не передано на доставку в Boxberry'))


main_page = MainPage()
