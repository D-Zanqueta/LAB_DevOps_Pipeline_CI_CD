from app import app, tasks


def setup_function():
    tasks.clear()


def test_homepage():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"TaskFlow" in response.data


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/",
        data={"task": "Estudar DevOps"}
    )

    assert response.status_code == 302
    assert "Estudar DevOps" in tasks


def test_empty_task():
    client = app.test_client()

    client.post("/", data={"task": ""})

    assert len(tasks) == 0