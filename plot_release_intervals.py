import matplotlib.pyplot as plt

def plot_release_intervals(intervals):
    plt.figure(figsize=(10, 6))
    plt.hist(intervals, bins=20, color='blue', alpha=0.7)
    plt.title('Distribution of Release Intervals')
    plt.xlabel('Interval (days)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('Result/vscode_release_intervals_distribution.png')
    plt.close()  # 关闭图形