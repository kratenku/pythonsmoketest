from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class inicioSesion():
    btnLogin = "//a[contains(@href, 'login')]"

    def __init__(self, driver):
        self.driver = driver
        # self.btnLogin=btnLogin

    def seleccionInicio(self):
        self.driver.find_element(By.XPATH, self.btnLogin).click()
