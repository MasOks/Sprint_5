# Sprint_5
Проект автоматизации тестирования сервиса Stellar Burgers
1. Основа для написания автотестов - фреймворк pytest.
2. Локаторы, используемые в автотестах, описаны в файле locators.py
3. Фикстуры хранятся в файле conftest.py
4. URL сервиса хранится в файле config.py
5. Автотесты:
на регистрацию хранятся в файле test_stellar_registration.py: успешная регистрация в Chrome, в Firefox, некорректный пароль в Chrome; 
на вход в сервис хранятся в файле test_stellar_entrances.py (Chrome);
на переходы Личного кабинета хранятся в файле test_stellar_transfers_in_account.py (Chrome);
на выход из аккаунта хранятся в файле test_stellar_log_out_of_account.py (Chrome);
на переходы внутри раздела Конструктор (без регистрации пользователя) хранятся в файле test_stellar_sections_of_constructor.py (Chrome).
