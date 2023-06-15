import os
import requests
#important note that it only clones public repos
# Replace with your GitHub username
username = "ur name"

# Replace with the desired clone directory
clone_directory = r"C:\example\directory\Github"

# API endpoint to retrieve repository list
api_endpoint = f"https://api.github.com/users/{username}/repos"

# Clone all repositories
os.makedirs(clone_directory, exist_ok=True)
os.chdir(clone_directory)

# Retrieve repository list using GitHub API
response = requests.get(api_endpoint)
repositories = response.json()

# Clone each repository
for repo in repositories:
    repo_name = repo["name"]
    clone_url = repo["clone_url"]
    target_folder = os.path.join(clone_directory, repo_name)

    if os.path.exists(target_folder):
        print(f"Repository '{repo_name}' is already cloned. Skipping...")
        continue

    clone_command = f"git clone {clone_url}"

    exit_code = os.system(clone_command)
    if exit_code != 0:
        print(f"Failed to clone repository '{repo_name}'.")

print("All repositories cloned successfully!")
