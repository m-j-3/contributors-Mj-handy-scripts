import requests

# Replace with your GitHub username
username = "name"

# Replace with your GitHub personal access token (PAT) with the appropriate scope
access_token = "token"

# API endpoint to retrieve repository list
api_endpoint = f"https://api.github.com/user/repos"

# Retrieve repository list using GitHub API
headers = {"Authorization": f"token {access_token}"}
response = requests.get(api_endpoint, headers=headers)
repositories = response.json()

# Change public repositories to private
for repo in repositories:
    repo_name = repo["name"]
    repo_url = repo["url"]
    payload = {"private": True}

    response = requests.patch(repo_url, headers=headers, json=payload)

    if response.status_code == 200:
        print(f"Changed repository '{repo_name}' to private.")
    else:
        print(f"Failed to change repository '{repo_name}' to private.")

print("All public repositories changed to private successfully!")
