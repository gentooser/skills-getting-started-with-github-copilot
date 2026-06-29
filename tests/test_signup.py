def test_signup_adds_new_participant(client):
    email = "new.student@mergington.edu"

    response = client.post("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"

    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_returns_404_for_missing_activity(client):
    response = client.post("/activities/Nonexistent Club/signup", params={"email": "student@mergington.edu"})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    existing_email = "michael@mergington.edu"

    response = client.post("/activities/Chess Club/signup", params={"email": existing_email})

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"


def test_signup_supports_activity_names_with_spaces(client):
    email = "spaces.case@mergington.edu"

    response = client.post("/activities/Programming Class/signup", params={"email": email})

    assert response.status_code == 200

    activities = client.get("/activities").json()
    assert email in activities["Programming Class"]["participants"]


def test_signup_returns_422_when_email_is_missing(client):
    response = client.post("/activities/Chess Club/signup")

    assert response.status_code == 422
