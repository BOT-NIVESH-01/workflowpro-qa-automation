from dataclasses import dataclass

from config.settings import (
    BASE_URL,
    BROWSER,
    HEADLESS,
    TIMEOUT,
    ENVIRONMENT,
)


@dataclass(frozen=True)
class Config:
    base_url: str = BASE_URL
    browser: str = BROWSER
    headless: bool = HEADLESS
    timeout: int = TIMEOUT
    environment: str = ENVIRONMENT


config = Config()