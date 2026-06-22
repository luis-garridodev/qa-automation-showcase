from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# A CLASSE: O molde da página (Padrão POM)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def acessar_pagina(self):
        self.driver.get(self.url)

    def fazer_login(self, user, password):
        # Utilizando Espera Explícita para evitar falhas de sincronização
        wait = WebDriverWait(self.driver, 10)
        
        user_element = wait.until(EC.presence_of_element_located(self.username_input))
        user_element.send_keys(user)
        
        pass_element = wait.until(EC.presence_of_element_located(self.password_input))
        pass_element.send_keys(password)
        
        btn_element = wait.until(EC.element_to_be_clickable(self.login_button))
        btn_element.click()

# O TESTE PRÁTICO (Instanciando o Objeto)
def test_login_sucesso():
    driver = webdriver.Chrome()
    tela_login = LoginPage(driver)
    
    tela_login.acessar_pagina()
    tela_login.fazer_login("standard_user", "secret_sauce")
    
    # Validação simples
    assert "inventory.html" in driver.current_url
    driver.quit()