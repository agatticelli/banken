from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from .bank import Bank

class MasterConsultas(Bank):

    login_url = ("https://www1.masterconsultas.com.ar/socios/context/"
                 "init_input.action")

    def __init__(self, browserName, username, password):

        super().__init__(browserName)

        self.username = username
        self.password = password


    def login(self):

        dvr = self.driver

        dvr.get(MasterConsultas.login_url)

        dvr.find_element_by_id("usernameId").send_keys(self.username)
        dvr.find_element_by_id("password").send_keys(self.password)

        dvr.find_element_by_id("submitLogin").click()

        # TODO: check if user has logged in successfully


    def logout(self):

        dvr = self.driver
        mouse = ActionChains(dvr)

        dropdown_id = "ROLE_MI_USUARIO"
        btn_id = "ROLE_CERRAR_SESION"

        dropdown = dvr.find_element_by_id(dropdown_id)

        dvr.execute_script("arguments[0].scrollIntoView();", dropdown)

        # Open dropdown
        mouse.move_to_element(dropdown).perform()

        # Click on logout btn
        dvr.find_element_by_id(btn_id).click()

        goodbye = dvr.find_element_by_css_selector('.subtit')

        while goodbye.text != "Gracias por utilizar MasterConsultas.":
            sleep(5)


    def getCards(self):

        dvr = self.driver

        selector = ".bancos tr td a img"

        imgs = dvr.find_elements_by_css_selector(selector)

        return imgs


    def changeToCard(self, card):

        card.click()

        selector = ".ui-widget-content.jqgrow.ui-row-ltr"

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, selector)))


    def getLastConsumptions(self):

        # FIXME: get consumptions of all pages

        dvr = self.driver

        selector = ".ui-widget-content.jqgrow.ui-row-ltr"

        wait = WebDriverWait(dvr, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

        rows = dvr.find_elements_by_css_selector(selector)

        data = []
        for row in rows:

            fields = row.find_elements_by_tag_name('td')
            if len(fields[0].text.strip()):
                yield {
                    'operationDate': fields[0].text,
                    'detail': fields[2].text,
                    'fees': fields[3].text,
                    'pesos': fields[4].text,
                    'dollars': fields[5].text
                }

        next_btn = dvr.find_element_by_id('next_gridtable_pager')
        next_btn_classes = next_btn.get_attribute('class').split(' ')

        if not "ui-state-disabled" in next_btn_classes:
            next_btn.click()

            load_gridtable = dvr.find_element_by_id('load_gridtable')
            while True:
                if load_gridtable.value_of_css_property('display') == "none":
                    break
                sleep(2)

            for d in self.getLastConsumptions():
                yield d









