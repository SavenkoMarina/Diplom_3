# Diplom_3

Чтобы запустить все тесты нужно выполнить команду:
```bash
PYTHONPATH=. pytest tests/*
```

Восстановление пароля (recover_page.py)
1. test_recover_link - Переход на страницу восстановления пароля
2. test_request_password_recover - Ввод почты и клик по кнопке «Восстановить»
3. test_show_password - Показать/скрыть пароль

Личный кабинет (account_page.py)
1. test_account_link - Переход в личный кабинет
2. test_order_history - Переход в историю заказов
3. test_logout - Выход из системы

Проверка основного функционала (main_page.py)
1. test_constructor_link - Переход по клику на 'Конструктор'
2. test_orders_feed - Переход в ленту заказов
3. test_ingredient_modal - Открыть всплывающее окно ингредиентов
4. test_close_modal - Закрыть всплывающее окно
5. test_ingredients_counter - Проверка сетчика ингредиентов
6. test_create_order - Проверка создания заказа

Раздел "Лента заказов" (feed_page.py)
1. test_open_order - Проверка открытия заказа
2. test_users_order_in_order_feed - Заказы пользователя отображаются в ленте заказов
3. test_total_counter - Проверка увелечения счетчика за всё время
4. test_daily_counter - Проверка увелечения счетчика за сегодня
5. test_order_in_progress - Проверка номера оформленного заказа в разделе В работе