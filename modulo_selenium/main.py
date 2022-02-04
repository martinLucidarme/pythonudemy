from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

'''
para achar o lugar dos elementos: clic direito, inspecionar.
para CSS selector: clic direito: copy - selector

'''


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            r'user-data-dir=C:\Users\Martin Lucidarme\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )  # até agora: só para instanciar toda a abertura do Chrome

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.CSS_SELECTOR, '[href="/login"]')
            btn_sign_in.click()

        except Exception as e:
            print(f'Deu esse erro ao clicar: {e}')

    def verifica_usuario(self, usuario):
        perfil_link = self.chrome.find_element(By.CSS_SELECTOR, '#app > div.bLayout.flex__scroll.js-scroll > div.bLayout__content > div > div > div.bSection__scroll > div > div > div > div > div > div > div > div.aligner__fluid > div > div:nth-child(1) > h2')
        html_perfil_link = perfil_link.get_attribute('innerHTML')  # pega o nome do usuario
        assert usuario in html_perfil_link

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'email')
            input_password = self.chrome.find_element(By.ID, 'password')
            input_login.send_keys('mlucidarme@myeasyfarm.com')
            input_password.send_keys('*****')
            sleep(2)
            submit = self.chrome.find_element(By.CSS_SELECTOR, '[data-test-id="login-login-button"]')
            submit.click()

        except Exception as e:
            print('Erro ao fazer login: ', e)

    def clica_selecionado(self, css_selector):
        try:
            selecionado = self.chrome.find_element(By.CSS_SELECTOR, css_selector)
            selecionado.click()

        except Exception as e:
            print('Nao clicou porque', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://app.myeasyfarm.com/register?continue_url=/')

    sleep(2)
    chrome.clica_sign_in()
    chrome.faz_login()
    chrome.clica_selecionado('#app > div.bLayout.flex__scroll.js-scroll > div.bSidebar.bSidebar_expanded > div.bSidebar__nav > a:nth-child(6) > span')
    sleep(3)
    chrome.clica_selecionado('#app > div.bLayoutHeader > div.bLayoutHeader__nav > div > a:nth-child(4) > div > svg')
    sleep(3)
    chrome.verifica_usuario('Martin Lucidarme')
    sleep(3)
    chrome.clica_selecionado('#app > div.bLayout.flex__scroll.js-scroll > div.bLayout__content > div > div > div.bSection__scroll > div > div > div > div > div > div > div > div.aligner__fluid > div > div.aligner__right > div > div.formItemInline.formItemInline_sm > button')
    sleep(3)

    sleep(2)
    chrome.sair()
