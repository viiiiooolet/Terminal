from datetime import datetime


def calculate_release_intervals(releases):
    intervals = []

    # 先按照发布时间排序
    releases.sort(key=lambda x: datetime.strptime(x['published_at'], '%Y-%m-%dT%H:%M:%SZ'))

    for i in range(1, len(releases)):
        prev_date = datetime.strptime(releases[i - 1]['published_at'], '%Y-%m-%dT%H:%M:%SZ')
        curr_date = datetime.strptime(releases[i]['published_at'], '%Y-%m-%dT%H:%M:%SZ')
        interval = (curr_date - prev_date).days  # 确保是 curr_date - prev_date
        intervals.append(interval)

    return intervals


def analyze_release_intervals(intervals):
    avg_interval = sum(intervals) / len(intervals) if intervals else 0
    min_interval = min(intervals) if intervals else 0
    max_interval = max(intervals) if intervals else 0
    return avg_interval, min_interval, max_interval