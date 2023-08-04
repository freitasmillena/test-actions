# add_comment.py
import os
import requests
import json

def add_comment(pr_number, repo, token, comment_filepath):
    with open(comment_filepath, 'r') as file:
        comment_body = file.read()
        print(comment_body)

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    payload = {"body": comment_body}

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 201:
        print("Failed to add comment")
        print("Response:", response.text)

if __name__ == "__main__":
    pr_number = os.getenv('PR_NUMBER')
    repo = os.getenv('GITHUB_REPOSITORY')
    token = os.getenv('GITHUB_TOKEN')
    print("token", token)
    comment_filepath = os.getenv('FILE_PATH')
    add_comment(pr_number, repo, token, comment_filepath)
