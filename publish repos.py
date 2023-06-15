import os
import requests
import shutil

# Replace with the path to your GitHub username
username = "usrname"

# Replace with your GitHub personal access token
access_token = "urtoken"

# Replace with the directory where your repository folders are located
repos_directory = "C:/example/directory/Github"

# API endpoint to create a repository
api_endpoint = f"https://api.github.com/user/repos"

# Get the list of repository folders
repository_folders = [
    folder
    for folder in os.listdir(repos_directory)
    if os.path.isdir(os.path.join(repos_directory, folder))
]

# Publish each repository
for folder in repository_folders:
    repo_name = folder
    repo_path = os.path.join(repos_directory, folder)
    
    # Delete the .git folder if it exists
    git_folder = os.path.join(repo_path, ".git")
    if os.path.exists(git_folder):
        shutil.rmtree(git_folder)

    # Create a repository on GitHub
    payload = {
        "name": repo_name,
        "private": False,
        "auto_init": False  # Disable auto initialization
    }
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(api_endpoint, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Created repository '{repo_name}' on your GitHub account.")
    else:
        print(f"Failed to create repository '{repo_name}'.")
        continue

    # Change to the repository directory
    os.chdir(repo_path)

    # Initialize the repository and add all files
    os.system("git init")
    os.system("git add .")

    # Commit the changes
    os.system('git commit -m "Initial commit"')

    # Set the origin remote URL
    repo_url = f"https://github.com/{username}/{repo_name}.git"
    os.system(f"git remote add origin {repo_url}")

    # Push the repository to GitHub
    os.system("git push -u origin main")

    print(f"Published repository '{repo_name}' to your GitHub account.")

print("All repositories published successfully!")