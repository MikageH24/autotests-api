import pytest


# Фикстура, которая будет автоматически вызываться для каждого теста
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")


# Фикстура для инициализации настроек автотестов на уровне сессии
@pytest.fixture(scope='session')
def settings():
    print("[SESSION] Инициализируем настройки автотестов")


# Фикстура для создания данных пользователя, которая будет выполняться один раз на класс тестов
@pytest.fixture(scope='class')
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


# Фикстура для инициализации API клиента, выполняющаяся для каждого теста
@pytest.fixture(scope='function')
def users_client():
    print("[FUNCTION] Создаем API клиент на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        pass

    def test_user_can_create_course(self, settings, user, users_client):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        pass


@pytest.fixture
def setup_teardown():
    # Это часть Setup — код, который выполняется перед тестом
    print("Setup: Инициализация данных или окружения")
    test_data = {"user": "testuser", "password": "testpass"}

    # Это часть Teardown — код, который выполняется после теста
    yield test_data  # Здесь возвращаем данные для теста, можно ничего не возвращать, тут передается выполняется тест

    print("Teardown: Очистка данных или окружения")
    # Здесь можно закрыть соединения, удалить временные файлы и т.д.
    # Например, удалить созданные записи в базе данных, если таковые были.


def test_login(setup_teardown):
    # Здесь setup_teardown будет содержать возвращённые данные из фикстуры
    assert setup_teardown["user"] == "testuser"
    assert setup_teardown["password"] == "testpass"


# фикстуры могут передаваться в другие фикстуры с сохранением своего scope
# Если передать фикстуру session в фикстуру function, то session отработает один раз за сессию и затем будет
# передавать закешированное значение. Правильно передавать более глобальную фикстуру в более атомарную,
# наоборот - ошибка. Или с одинаковым scope
