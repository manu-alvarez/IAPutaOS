"""API-key authentication must reject missing configuration and malformed clients."""
from app.core.api_auth import matches_api_key


def test_valid_key():
    assert matches_api_key("server-generated-value", "server-generated-value")


def test_missing_server_key_fails_closed():
    assert not matches_api_key(None, "anything")
    assert not matches_api_key("", "anything")


def test_missing_or_wrong_client_key_fails_closed():
    assert not matches_api_key("server-generated-value", None)
    assert not matches_api_key("server-generated-value", "wrong")


def test_key_is_not_reduced_to_prefix():
    assert not matches_api_key("server-generated-value", "server-generated")
