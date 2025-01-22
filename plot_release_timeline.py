import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime


def plot_release_timeline(releases):
    year_count = defaultdict(int)

    for release in releases:
        date = datetime.strptime(release['published_at'], '%Y-%m-%dT%H:%M:%SZ')
        year = date.year
        year_count[year] += 1

    years = sorted(year_count.keys())
    counts = [year_count[year] for year in years]

    plt.figure(figsize=(10, 8))
    plt.plot(years, counts, marker='o', linestyle='-')
    plt.title('VSCode Releases by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Releases')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Result/vscode_release_timeline.png')
    plt.close()  # 关闭图形