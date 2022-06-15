#import pytest
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        """Тест проверяет, что страница товара
         содержит кнопку добавления в корзину
        """
        # Открываем страницу товара
        browser.get(link)

        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(5)

        # Проверяем наличие кнопки добавления товара в корзину
        """плохая реализация
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button is not None
        """
        y = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))  # y = длина списка найденных элементов 
        # y = len(browser.find_elements(By.CSS_SELECTOR, ".to-basket"))  # пробуем сломать
        print("количество элементов:", y)  # необязательно - просто вывести на печать значение y
        assert y > 0, 'Cелектор кнопки не найден'
       