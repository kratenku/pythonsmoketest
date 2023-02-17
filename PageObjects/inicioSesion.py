import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class inicioSesion():
    table = "//body/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/table[1]"
    registre = "//header/nav[1]/div[1]/div[2]/div[1]/a[2]"
    ##userCredi = "//input[@id='user']"
    userName = "/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[1]/div[3]/form[1]/div[1]/div[1]/input[1]"
    userPass = "/html[1]/body[1]/app-root[1]/app-login[1]/div[1]/div[1]/div[1]/div[3]/form[1]/div[2]/div[1]/input[1]"

    def __init__(self, driver):
        self.driver = driver
        # self.btnLogin=btnLogin

    def seleccionInicio(self, nombreUsuario, passUser):
        user = self.driver.find_element(By.XPATH, self.userName)
        user.send_keys(nombreUsuario)
        passw = self.driver.find_element(By.XPATH, self.userPass)
        passw.send_keys(passUser)

        expectedTitle="Credisoft 2.0"
        assert (expectedTitle)

        """for i in tableSelect:
            print(i.text)
            if i == "Usuario":
                self.driver.find_element(By.CSS_SELECTOR, self.userCredi).click()"""
