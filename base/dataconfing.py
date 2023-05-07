import xmltodict
import codecs
import configparser

config = configparser.ConfigParser()
config.readfp(codecs.open("C:/Users/kharlamov/Desktop/Работа/files/server_config.ini", "r", "utf8"))

handle = codecs.open(str(config["server"]["config_path"]) + str(config["server"]["config_name"]), "r", "utf_8_sig")
content = handle.read()
data = xmltodict.parse(content)['server']


class Config():

    def __init__(self):
        self.SERVER_NAME = 'omega'

        self.SERVER_SSH_HOST = str(data[self.SERVER_NAME]['ssh']['host'])
        self.SERVER_SSH_PORT = str(data[self.SERVER_NAME]['ssh']['port'])
        self.SERVER_SSH_USER = str(data[self.SERVER_NAME]['ssh']['user'])
        self.SERVER_SSH_PASSWORD = str(data[self.SERVER_NAME]['ssh']['password'])

        self.SERVER_DATABASE_NAME = str(data[self.SERVER_NAME]['db']['dbname'])
        self.SERVER_DATABASE_USER = str(data[self.SERVER_NAME]['db']['user'])
        self.SERVER_DATABASE_PASSWORD = str(data[self.SERVER_NAME]['db']['password'])

        self.SERVER_USER_LOGIN = str(data[self.SERVER_NAME]['login']['admin'])
        self.SERVER_USER_PASSWORD = str(data[self.SERVER_NAME]['password']['admin'])

        self.SERVER_LINKS_MAINPAGE = str(data[self.SERVER_NAME]['links']['main_page'])

        self.FIELD_REESTR_MAINLINK = str(config["fields_reestr"]["reestr_main_link"])
        self.FIELD_REESTR_FINDBTN = str(config["fields_reestr"]["reestr_find_btn"])
        self.FIELD_REESTR_CLEARBTN = str(config["fields_reestr"]["reestr_clear_btn"])
        self.FIELD_REESTR_SEARCHRES_AMOUNT = str(config["fields_reestr"]["search_results_amount"])
        self.FIELD_REESTR_CHECKBOX_ALL = str(config["fields_reestr"]["checkbox_all"])
        self.FIELD_REESTR_CHECKBOX_SELECTED = str(config["fields_reestr"]["selected_checkbox_amount"])
        self.FIELD_REESTR_CHECKBOXES = str(config["fields_reestr"]["select_all_checkboxes"])
        self.FIELD_REESTR_CUSTOM_FIELDS_AMOUNT_INPUT = str(config["fields_reestr"]["custom_field_am_input"])
        self.FIELD_REESTR_CUSTOM_FIELDS_AMOUNT_BTN = str(config["fields_reestr"]["custom_field_am_show_btn"])
