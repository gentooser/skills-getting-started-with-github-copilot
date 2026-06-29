import src.app as app_module


def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert response.json() == app_module.activities


def test_get_activities_has_expected_structure(client):
    response = client.get("/activities")
    data = response.json()

    assert data

    for details in data.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
