import pytest


@pytest.mark.django_db
def test_login_view(client, create_superuser_only):
    response = client.post("/login/", {"email": "a@a.pl", "password": "adminadmin"}, format="json")

    assert response.status_code == 200
    assert "jwt" in response.data
    assert response.cookies.get("jwt")

    response = client.post("/login/", {"email": "a@a.pl", "password": "admin"}, format="json")
    assert response.status_code == 403
    assert "jwt" not in response.data
    assert response.cookies.get("jwt") is None

    response = client.post("/login/", {"email": "aaaa@a.pl", "password": "adminadmin"}, format="json")
    assert response.status_code == 403
    assert "jwt" not in response.data
    assert response.cookies.get("jwt") is None


@pytest.mark.django_db
def test_logout_view(client, create_superuser_only):
    response = client.post("/login/", {"email": "a@a.pl", "password": "adminadmin"}, format="json")

    assert response.status_code == 200
    assert "jwt" in response.data
    assert response.cookies.get("jwt")

    response = client.post("/logout/", {}, format="json")

    assert response.status_code == 200

    assert response.cookies.get("jwt").value == ""
