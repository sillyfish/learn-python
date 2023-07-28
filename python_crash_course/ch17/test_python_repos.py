import pytest


def test_python_repos():
    import requests

    # Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    assert r.status_code == 200

    # Convert the response object to a dictionary
    response_dict = r.json()
    assert response_dict["total_count"] > 100

    # Explore information about the repositories.
    assert len(response_dict["items"]) > 0
