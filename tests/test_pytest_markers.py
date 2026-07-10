import pytest


@pytest.mark.smoke
def test_smoke_case():
    assert 1 + 1 == 2


@pytest.mark.regression
def test_regression_case():
    assert 2 * 2 == 4


# pytest -m smoke
# python -m pytest -m "smoke and regression" должны быть оба названия в маркировке
# python -m pytest -m "smoke or regression" любое из
# python -m pytest -m fast
# pytest -m "regression and not slow"

@pytest.mark.fast
def test_fast():
    pass


@pytest.mark.slow
def test_slow():
    pass


@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        pass

    def test_case2(self):
        pass


@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    pass


@pytest.mark.api
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login(self):
        pass

    @pytest.mark.regression
    def test_forgot_password(self):
        pass

    @pytest.mark.smoke
    def test_signup(self):
        pass


# pytest -m "api and regression"
# regression or api and not critical
# python -m pytest --markers  - показать весь список маркеров
