import requests

# Replace with your GitHub username
username = "name3"

# Replace with your GitHub personal access token (PAT) with the appropriate scope
access_token = "token"

# API endpoint to retrieve repository list
api_endpoint = f"https://api.github.com/user/repos"

# Retrieve repository list using GitHub API
headers = {"Authorization": f"token {access_token}"}
response = requests.get(api_endpoint, headers=headers)
repositories = response.json()

# Prompt user for confirmation
confirm = input("This script will delete all your repositories. Are you sure? (y/n): ")
if confirm.lower() != "y":
    print("Script aborted. No repositories were deleted.")
    exit()

confirm_really = input("Are you REALLY sure? This action cannot be undone. (y/n): ")
if confirm_really.lower() != "y":
    print("Script aborted. No repositories were deleted.")
    exit()

# Delete all repositories
for repo in repositories:
    repo_name = repo["name"]
    repo_url = repo["url"]

    delete_url = f"{repo_url}"
    response = requests.delete(delete_url, headers=headers)

    if response.status_code == 204:
        print(f"Deleted repository '{repo_name}'.")
    else:
        print(f"Failed to delete repository '{repo_name}'.")
        print(response.json())


print("All repositories deleted successfully!")
