import time

import pytest
import pytest_check as check

from pom.fieldreestr_tests_funcs import FieldsReestrFuncs


@pytest.mark.usefixtures('setup')
class Tests:

    def test_reestr_main_func(self):
        self.driver.delete_all_cookies()
        reestr_funcs = FieldsReestrFuncs(self.driver)
        assert reestr_funcs.login() == 0, 'Не удалось загрузить сраницу'
        assert reestr_funcs.reestr_page() != 1, "Не удалось открыть реестр"
        check.equal(reestr_funcs.fields_amount_check(), 0, "Ошибка!")
        check.not_equal(reestr_funcs.find_button(), 1, "Не удалось нажать на кнопку Найти")
        check.not_equal(reestr_funcs.clear_button(), 1, "Не удалось нажать на кнопку Очистить")
        check.not_equal(reestr_funcs.check_box_all(), 1, "Не удалось нажать на кнопку мультичекбокс")
        check.equal(reestr_funcs.check_box_select_all_count(), 0, "Ошибка!")
        print(reestr_funcs.custom_fields_amount_check())
        time.sleep(3)
#        print("\n" + Config().FIELD_REESTR_SEARCHRES_AMOUNT)
#        print(page_nav.get_many_btns(Config().FIELD_REESTR_SEARCHRES_AMOUNT))
    #        page_nav.click_login_btn("isandsadmin", "FRNBuQw*#x*7")
#        self.driver.get('https://beta.isands.ru/zemel-nyj-pasport')
#        print(database_meth.ConnectionToServer().cadastr_fields_count(
#            {
#                'date_': '2023',
#                'isarc': False
#            }
#        ))
#        print(page_nav.get_fields_amount())
#        page_nav.search_btn().click()
#        time.sleep(2)
#        page_nav.id_sub_test()
#        return page_nav




