#!/usr/bin/python3
"""The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to
the script (number or type)"""
import sys
import requests

if __name__ == "__main__":
    repo_owner = sys.argv[2]
    repo_name = sys.argv[1]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)
    result = response.json()
    try:
        for i in range(10):
            print(f"{result[i].get('sha')}: ", end="")
            print(result[i]["commit"]["author"]["name"])
    except IndexError:
        pass
