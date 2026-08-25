from backend.app.core.config import settings


def test_settings():
    assert settings.app_name == "ai_assessment_platform"
    assert settings.app_version == "0.1.0"
    assert settings.api_port == 8000