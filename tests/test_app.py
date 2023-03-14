from src.app import create_app

app = create_app()
app.debug = True
app.testing = True
client = app.test_client()


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello World!" in response.data
