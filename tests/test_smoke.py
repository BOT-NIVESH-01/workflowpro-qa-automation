import pytest


@pytest.mark.smoke
def test_framework_initialization(page):
    """
    Smoke test to verify that the Playwright framework
    launches a browser and can interact with a webpage.
    """

    page.goto("https://example.com")

    assert "Example Domain" in page.title()