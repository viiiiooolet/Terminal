import requests
import time
def fetch_vscode_contributors(owner='microsoft', repo='vscode'):
    """
    获取指定 GitHub 仓库的贡献者信息。

    参数:
        owner (str): 仓库拥有者的用户名。
        repo (str): 仓库名称。

    返回:
        list: 包含贡献者信息的字典列表，每个字典包含登录名和贡献次数。
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    contributors = []
    page = 1
    per_page = 100
    headers = {} 
    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
            reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
            wait_time = max(0, reset_time - time.time())
            print(f"Rate limit reached. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            continue

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            break

        data = response.json()
        if not data:
            break

        contributors.extend(data)
        page += 1

    return contributors


def get_top_contributors(owner='microsoft', repo='vscode', top_n=20):
    """
    获取贡献次数排名前 N 的贡献者。

    参数:
        owner (str): 仓库拥有者的用户名。
        repo (str): 仓库名称。
        top_n (int): 前 N 名贡献者。

    返回:
        list: 包含前 N 名贡献者的列表，每个元素为字典，包含登录名和贡献次数。
    """
    contributors = fetch_vscode_contributors(owner, repo)
    top_contributors = sorted(contributors, key=lambda x: x['contributions'], reverse=True)[:top_n]
    return [{'login': contributor['login'], 'contributions': contributor['contributions']} for contributor in top_contributors]
