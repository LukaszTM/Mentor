import os

import pytest
from selenium import webdriver


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


@pytest.fixture
def serwer(tmp_path):
    import threading

    from werkzeug.serving import make_server

    from app import create_app
    srv = make_server("127.0.0.1", 0, create_app(tmp_path / "e2e.db"))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{srv.server_port}"
    srv.shutdown()
