# tests/conftest.py (fragment) — serwer aplikacji w wątku dla testów E2E
import os
import threading

import pytest
from selenium import webdriver
from werkzeug.serving import make_server

from app import create_app


@pytest.fixture
def klient(tmp_path):
    return create_app(tmp_path / "test.db").test_client()


@pytest.fixture
def serwer(tmp_path):
    app = create_app(tmp_path / "e2e.db")
    srv = make_server("127.0.0.1", 0, app)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_port}"
    srv.shutdown()


@pytest.fixture
def driver():
    if os.environ.get("CI"):
        opcje = webdriver.ChromeOptions()
        opcje.add_argument("--headless=new")
        d = webdriver.Chrome(options=opcje)
    else:
        opcje = webdriver.EdgeOptions()
        opcje.add_argument("--headless=new")
        d = webdriver.Edge(options=opcje)
    yield d
    d.quit()
