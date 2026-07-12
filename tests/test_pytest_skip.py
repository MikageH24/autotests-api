import pytest

# Маркировка @pytest.mark.skip используется для явного пропуска теста


@pytest.mark.skip(reason="Фича в разработке")
def test_feature_in_development():
    pass
