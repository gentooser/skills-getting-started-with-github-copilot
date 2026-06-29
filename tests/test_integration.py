def test_signup_unregister_signup_flow_is_consistent(client):
    activity = "Science Club"
    email = "flow.test@mergington.edu"

    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert signup_response.status_code == 200

    after_signup = client.get("/activities").json()
    assert email in after_signup[activity]["participants"]

    unregister_response = client.delete(f"/activities/{activity}/participants", params={"email": email})
    assert unregister_response.status_code == 200

    after_unregister = client.get("/activities").json()
    assert email not in after_unregister[activity]["participants"]

    signup_again_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert signup_again_response.status_code == 200

    final_state = client.get("/activities").json()
    assert email in final_state[activity]["participants"]
