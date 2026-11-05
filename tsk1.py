import requests

usernames = ["octocat", "torvalds", "TheOcto"]

for username in usernames:
    response = requests.get(
        f"https://api.github.com/users/{username}",
        timeout=10,
    )
    if response.status_code != 200:
        raise RuntimeError(
            f"GitHub API request for {username} failed "
            f"with status {response.status_code}"
        )

    user = response.json()
    print(f"{user['login']}: {user['public_repos']} public repositories")