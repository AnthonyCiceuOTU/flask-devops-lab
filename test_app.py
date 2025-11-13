from app import app, MOTIVATIONAL_QUOTES


def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    # Lab requirement: response contains "DevOps"
    assert b'DevOps' in res.data


def test_motivator_status_and_json():
    client = app.test_client()
    res = client.get('/motivator')
    assert res.status_code == 200

    data = res.get_json()
    # Should be JSON with a "quote" key
    assert "quote" in data
    assert isinstance(data["quote"], str)
    # Quote should be one of our known quotes
    assert data["quote"] in MOTIVATIONAL_QUOTES
