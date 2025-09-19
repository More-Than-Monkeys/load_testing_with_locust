from __future__ import annotations

from locust import FastHttpUser, task, between
from utils.headers import build_base_headers


class ExampleUser(FastHttpUser):
    """
    A Locust user that repeatedly fetches https://example.com.
    """
    wait_time = between(1, 2)

    def on_start(self) -> None:
        self.client.base_url = "https://example.com"  # type: ignore[attr-defined]
        self.base_headers = build_base_headers()

    @task
    def load_homepage(self) -> None:
        """Fetch the example.com homepage."""
        self.client.get("/", headers=self.base_headers, name="GET /")
