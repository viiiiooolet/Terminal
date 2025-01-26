import requests
import time
from datetime import datetime
import matplotlib.pyplot as plt

def fetch_commit_activity(owner='microsoft', repo='vscode'):
    
    #获取指定仓库的提交历史信息。
    
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {}
    commits = []
    page = 1
    per_page = 100

    while True:
        params = {'page': page, 'per_page': per_page}
        response = requests.get(url, headers=headers, params=params)
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
        commits.extend(data)
        page += 1

    return commits

def analyze_commit_activity(commits):
    
    #分析提交活跃度。

    commit_dates = [datetime.strptime(commit['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ') for commit in commits]
    commit_days = [date.strftime('%Y-%m-%d') for date in commit_dates]
    commit_counts = {}
    for day in commit_days:
        if day in commit_counts:
            commit_counts[day] += 1
        else:
            commit_counts[day] = 1

    # 按日期排序
    sorted_dates = sorted(commit_counts)
    sorted_counts = [commit_counts[date] for date in sorted_dates]

    return sorted_dates, sorted_counts

def plot_commit_activity(dates, counts, output_file='Result/vscode_commit_activity.png'):
    
    #绘制提交活跃度折线图。
    plt.figure(figsize=(12, 6))
    plt.plot(dates, counts, color='blue', marker='o', linewidth=1.5)
    plt.title('Commit Activity Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Number of Commits', fontsize=14)
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"提交活跃度图已保存到 {output_file}")
