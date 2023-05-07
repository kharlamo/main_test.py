from base.dataconfing import Config
from pom.database_meth import ConnectionMethods
from pom.page_nav import PageNav
import datetime
import random
#import timeit

class FieldsReestrFuncs(PageNav):

    def __init__(self, driver):
        self.driver = driver
        self.page_nav = PageNav(self.driver)

    def login(self):
        return self.page_nav.login()

    def reestr_page(self):
        try:
#            timer = timeit.timeit(self.page_nav.get_many_elements('//div'), number=1)
#            print(timer)
            return self.page_nav.go_to_page(Config().FIELD_REESTR_MAINLINK)
        except EOFError as e:
            print(e)
            return 1

    def fields_amount_check(self):
        try:
            interface_value = str(self.page_nav.get_text_from_many_elements(Config().FIELD_REESTR_SEARCHRES_AMOUNT)[1]).rsplit('из ')[1][:-1]
        except Exception:
            return "Не удалось получить значение из страницы"
        try:
            database_value = str(ConnectionMethods().cadastr_fields_count(
                {
                    'year': int(datetime.date.today().year),
                    'remove': False
                }))
        except EOFError as e:
            print(e)
            return "Не удалось получить количество полей из БД"

        if interface_value == database_value:
            print(interface_value + " = " + database_value)
            return 0
        else:
            print(interface_value + "\n")
            print(database_value)
            return "Количество полей не совпадает с БД!!!"

    def find_button(self):
        try:
            btn = self.page_nav.click_element(Config().FIELD_REESTR_FINDBTN)
            return btn
        except Exception:
            return 1

    def clear_button(self):
        try:
            btn = self.page_nav.click_element(Config().FIELD_REESTR_CLEARBTN)
            return btn
        except Exception:
            return 1

    def check_box_all(self):
        return self.page_nav.click_element(Config().FIELD_REESTR_CHECKBOX_ALL)

    def check_boxes_get(self):
        return self.page_nav.get_many_elements(Config().FIELD_REESTR_CHECKBOXES)


    def check_box_select_all_count(self):
        try:
            checkboxes = self.check_boxes_get()
            count = 0
            for checkbox in checkboxes:
                checkbox.click()
                count += 1
                if count == 3:
                    break
        except EOFError as e:
            print(e)
            return "Не удалось прокликнуть по чекбоксам"

        try:
            interface_value_all = str(self.page_nav.get_text_from_many_elements(Config().FIELD_REESTR_CHECKBOX_SELECTED)[0]).rsplit('из ')[1]
            interface_value_selected = str(self.page_nav.get_text_from_many_elements(Config().FIELD_REESTR_CHECKBOX_SELECTED)[0]).rsplit('полей ')[1].replace(interface_value_all, '')[:-4]
        except EOFError as e:
            print(e)
            return "Не удалось получить значение из страницы"

        try:
            database_value = str(ConnectionMethods().cadastr_fields_count(
                {
                    'year': int(datetime.date.today().year),
                    'remove': False
                }))
        except EOFError as e:
            print(e)
            return "Не удалось получить количество полей из БД"

        if interface_value_all == database_value:
            if interface_value_selected == str(int(interface_value_all) - 3):
                print(interface_value_all + " = " + database_value)
                print(interface_value_selected + " из " + interface_value_all)
                return 0
            else:
                print(interface_value_all)
                print(interface_value_selected)
                return "Количество выбранных полей неактуально"
        else:
            print(interface_value_all + "\n")
            print(database_value)
            return "Количество полей не совпадает с БД!!!"

    def __custom_fields_amount(self):
        input = self.page_nav.get_element(Config().FIELD_REESTR_CUSTOM_FIELDS_AMOUNT_INPUT)
        input.clear()
        input.send_keys('6')
        return self.page_nav.get_element(Config().FIELD_REESTR_CUSTOM_FIELDS_AMOUNT_BTN).click()

    def custom_fields_amount_check(self):
        self.__custom_fields_amount()
        return str(self.page_nav.get_text_from_many_elements(Config().FIELD_REESTR_SEARCHRES_AMOUNT)[0]).rsplit(' из')[0][:30]