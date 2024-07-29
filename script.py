from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import json
from keys_converter import KeysConverter


class SeleniumController():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.actions = ActionChains(self.driver)
        self.key_converter = KeysConverter()

    def start(self):
        self.driver.get("https://nerdlegame.com/")
        self.actions.send_keys(Keys.ENTER)

    def type_equation(self, equation):
        for char in equation:
            self.actions.send_keys(self.key_converter.map_keys(char))

    def submit_equation(self):
        enter_btn = self.driver.find_element(By.CSS_SELECTOR, "[aria-label='ENTER ']")
        self.actions.click(on_element = enter_btn)
        self.actions.perform()

    def read_result(self, attempt):
        firstRow = self.driver.find_element(By.XPATH, f"//div[@class='pb-grid main-grid z-[9]']//child::div[{attempt}]")
        children = firstRow.find_elements(By.XPATH, "./child::*")

        for idx, entry in enumerate(children):
            aria_label = entry.get_attribute("aria-label")
            self.map_status(aria_label, idx)
        
        print(json.dumps(self.key_converter._keys_map))
        
    def map_status(self, aria_label: str, idx: int):
        text, status = aria_label.split()
        match status:
            case 'present':
                self.key_converter.update_occurence(text, True, position=idx, is_correct=False)
            case 'absent':
                self.key_converter.update_occurence(text, False)
            case 'correct':
                self.key_converter.update_occurence(text, True, position=idx, is_correct=True)

if __name__ == "__main__":
    sc = SeleniumController()
    

    sc.start()

    equation = '9+-4*2=1'
    sc.type_equation(equation)

    sc.submit_equation()

    sc.read_result(attempt=1)

