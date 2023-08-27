# Тестовое задание для компании 'Mayflower'

## Постановка задачи

Требуется создать автотесты на любом языке программирование с использованием Selenium Web Driver, которые должны запускаться в docker контейнере:
1. Вывести все строки таблицы Customers и убедиться, что запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'.
2. Вывести только те строки таблицы Customers, где city='London'. Проверить, что в таблице ровно 6 записей.
3. Добавить новую запись в таблицу Customers и проверить, что эта запись добавилась.
4. Обновить все поля (кроме CustomerID) в любой записи таблицы Customers и проверить, что изменения записались в базу.
5. Придумать собственный автотест и реализовать (тут все ограничивается только вашей фантазией).

### Подсказка: Заполнить поле ввода можно с помощью js кода, используя объект window.editor.

## Запуск
1. Перейти в корень репозитория
2. Собрать образ (в терминале): "docker build -t selenium-tests ."
2. Развернуть и запустить контейнер с тестами (в терминале): "docker run -t selenium-tests"
3. Запустить автотесты (в терминале Docker container): "python3 -m pytest -v -s --alluredir=results/allure/allure-results"
4. Сгенерировать Allure репорт (в терминале Docker container): "allure generate results/allure/allure-results -o results/allure/allure-report"
