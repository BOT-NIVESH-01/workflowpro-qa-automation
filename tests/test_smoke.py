def test_framework(page):
    page.goto("https://example.com")

    assert "Example" in page.title()