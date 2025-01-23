from fetch_vscode_releases import fetch_vscode_releases
from save_releases_to_csv import save_releases_to_csv
from plot_release_timeline import plot_release_timeline
from calculate_release_intervals import calculate_release_intervals, analyze_release_intervals
from plot_release_intervals import plot_release_intervals
from count_vscode_contributors import get_top_contributors
from plot_vscode_contributors import plot_top_contributors

def analyse_vscode_releases(owner='microsoft', repo='vscode',branch='main'):
    releases = fetch_vscode_releases(owner, repo)

    if not releases:
        print('没有找到发布信息。')
        return

    save_releases_to_csv(releases)
    plot_release_timeline(releases)

    intervals = calculate_release_intervals(releases)
    avg_interval, min_interval, max_interval = analyze_release_intervals(intervals)
    print(f'平均发布间隔: {avg_interval} 天, 最小发布间隔: {min_interval} 天, 最大发布间隔: {max_interval} 天')

    plot_release_intervals(intervals)

    top_contributors = get_top_contributors(owner, repo)
    plot_top_contributors(top_contributors)
   
    
if __name__ == "__main__":
    analyse_vscode_releases()