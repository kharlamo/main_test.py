import time

from selenium.webdriver import Keys

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from typing import List

from pom import database_meth

from base.dataconfing import Config

class PageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__log_label_link: str = '#_58_login'
        self.__pass_label_link: str = '#_58_password'
        self.__btn_login_class_name: str = 'button.btn.btn-primary'
        self.__settings_pl: str = 'li#layout_111.lfr-nav-item.dropdown.lfr-nav-deletable.lfr-nav-sortable.lfr-nav-updateable.yui3-dd-drop'
        self.__date_from_el: str = '#_settings_WAR_lpportlet_copy_fields_year_from'
        self.__date_for_el: str = '#_settings_WAR_lpportlet_copy_fields_year_to'
        self.__raion_filter: str = '//input[@id="_settings_WAR_lpportlet_raionCode_display"]'  #//select[@class="combobox_select"] //input[@id="_settings_WAR_lpportlet_raionCode_display"]
        self.__tag_name_op: str = 'option'
        self.__reg_names: str = '//div[@id = "_settings_WAR_lpportlet_raionCode_dropdown"]//label[*]'

        self.__search_btn: str = '//button[@id="_landpassport_WAR_lpportlet_filter"]'
        self.__clear_btn: str = '//button[@id="_landpassport_WAR_lpportlet_clear"]'

        self.__id_sub_data: str = '//td[@class = "table-cell first"]'
        self.__id_sub_filter: str = '//input[@id = "_landpassport_WAR_lpportlet_NUMBER"]'

#        self.__fields_amount: str = '//small[@class = "search-results"]'
        self.__fields_amount: str = 'small.search-results'

        self.__tologin_btn: str = '//*[@class = "sign-in "]'
        self.__login_field: str = '//*[@id = "_58_login"]'
        self.__password_field: str = '//*[@id = "_58_password"]'
        self.__login_btn: str = '//*[@class = "btn btn-primary"]'



    def login(self):
        if Config().SERVER_NAME == 'omega':
            try:
                self.is_visible('xpath', self.__tologin_btn, 'Go to login panel').click()
                self.is_visible('xpath', self.__login_field, 'Login field input').send_keys(Config().SERVER_USER_LOGIN)
                self.is_visible('xpath', self.__password_field, 'Password field input').send_keys(Config().SERVER_USER_PASSWORD)
                self.is_visible('xpath', self.__login_btn, 'Click login btn').click()
                return 0
            except EOFError as e:
                return e

    def go_to_page(self, url: str):
        try:
            return self.driver.get(url)
        except EOFError as e:
            print(e)
            return 1

    def get_element(self, xpath: str):
        try:
            return self.is_visible('xpath', xpath, 'Click login btn')
        except EOFError as e:
            print(e)
            return 1

    def click_element(self, xpath: str):
        try:
            return self.is_visible('xpath', xpath, 'Click login btn').click()
        except EOFError as e:
            print(e)
            return 1

    def get_many_elements(self, xpath: str):
        try:
            return self.are_present('xpath', xpath, 'Click login btn')
        except EOFError as e:
            print(e)
            return 1

    def get_text_from_many_elements(self, xpath):
        try:
            elements = self.are_present('xpath', xpath, 'Text elements')
            return [element.text for element in elements]
        except EOFError as e:
            print(e)
            return 1


   # def get_element_by_links(self) -> WebElement:
   #     return self.is_visible('css', self.__log_label_link, 'Login link')

    def login_field(self):
        return self.is_visible('css', self.__log_label_link, 'Login link')

    def password_field(self):
        return self.is_visible('css', self.__pass_label_link, 'Password link')

    def login_btn(self):
        return self.is_visible('css', self.__btn_login_class_name, 'Log btn')

    def click_login_btn(self, login: str, password: str):
        self.login_field().send_keys(login)
        self.password_field().send_keys(password)
        return self.login_btn().click()

    def settings_pl(self):
        return self.is_visible('css', self.__settings_pl, 'Settings passport land').click()

    def date_from(self):
        return self.is_visible('css', self.__date_from_el, 'Chose date from')

    def date_for(self):
        return self.is_visible('css', self.__date_for_el, 'Chose date for')

    def reg_names(self):
        return self.is_visible('xpath', self.__raion_filter, 'Chose reg')

    def get_raion_names(self):
        regs = self.are_visible('xpath', self.__reg_names, 'Chose reg')
        return [reg.tag_name for reg in regs]

    def get_raions(self):
        return self.are_visible('xpath', self.__reg_names, 'Chose reg')

    def get_fields_amount(self):
        result = self.is_visible('css', self.__fields_amount, 'Сторка с количеством полей в реестре').text
        return str(result.rsplit('из ')[1])

    def correct_date(self):
        select_from = Select(self.date_from())
        select_from.select_by_visible_text('2022')
        select_for = Select(self.date_for())
        select_for.select_by_visible_text('2023')
        el = self.reg_names()
        el.click()
#        el2 = self.is_visible('xpath', self.__test_el_path, 'Password link2')
#        el2.click()
#        time.sleep(1)
#        print(",".join(self.get_raion_names()))
        for raion in self.get_raions():
            try:
                raion.click()
#                path: str = '//label[text()=" ' + str(reg_names) + ' "]'
#                self.is_visible('xpath', path, 'Password link2').click()
            except Exception:
                print("Не удалось нажать на район " + raion.text)
        #select_reg = Select(el)
      #  select_reg = self.select_el('xpath', self.__raion_filter)
       # select_reg.select_by_index(3)
        return print("Done!")

    def search_btn(self):
        return self.is_visible('xpath', self.__search_btn, 'Search btn')

    def clear_btn(self):
        return self.is_visible('xpath', self.__search_btn, 'Clear btn')

    def get_id_subs(self):
        return self.are_visible('xpath', self.__id_sub_data, 'id_sub from reestr')

    def get_id_sub_filter(self):
        return self.is_visible('xpath', self.__id_sub_filter, 'id_sub filter')

    def id_sub_test(self):
        id_subs = [id_sub.text for id_sub in self.get_id_subs()]
        for id_sub in id_subs:
            self.get_id_sub_filter().send_keys(str(id_sub))
            self.search_btn().click()
            if id_sub in [id_sub.text for id_sub in self.get_id_subs()]:
                print("correct with " + str(id_sub))
            else:
                print("wrong with " + str(id_sub))
            self.get_id_sub_filter().clear()
        print("Done!")










