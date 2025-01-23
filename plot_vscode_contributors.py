import matplotlib.pyplot as plt

def plot_top_contributors(contributors, output_file='Result/vscode_contributors.png'):
    """
    绘制贡献者的贡献次数柱状图。

    参数:
        contributors (list): 包含贡献者信息的字典列表，每个字典包含 'login' 和 'contributions' 键。
        output_file (str): 输出图像文件名。
    """
    if not contributors:
        print("贡献者列表为空，无法生成图表。")
        return

    logins = [contributor['login'] for contributor in contributors]
    contributions = [contributor['contributions'] for contributor in contributors]

    plt.figure(figsize=(12, 6))
    plt.bar(logins, contributions, color='skyblue')
    plt.xlabel('Contributors', fontsize=14)
    plt.ylabel('Contributions', fontsize=14)
    plt.title('Top Contributors to VS Code', fontsize=16)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"柱状图已保存到 {output_file}")
