import unittest
from selenium.webdriver.common.by import By
import time
import PageObjects.inicioSesion
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriver
from webdriver_manager.microsoft import EdgeChromiumDriver
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from PageObjects.inicioSesion import inicioSesion
from behave import *


##https://www.opencart.com/
##http://190.66.12.51:20126/CrediSoft2/Front/#/

class PruebaUno(unittest.TestCase):
    urlAcceso = "http://190.66.12.51:20126/CrediSoft2/Front/#/"
    nombreUsuario= 'admon'
    passUser='admin123'
    driver = webdriver.Chrome(r"C:\Users\Administrador\PycharmProjects\pythonProject\drivers\chrome\chromedriver.exe")

    @classmethod
    def setUp(cls):
        cls.driver.get(cls.urlAcceso)
        cls.driver.maximize_window()


    def test_botonLogin(self):
        bl = inicioSesion(self.driver)
        bl.seleccionInicio(self.nombreUsuario, self.passUser)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print("prueba completa")


if __name__ == "__main__":
    unittest.main()
