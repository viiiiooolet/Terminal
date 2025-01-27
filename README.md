# 大连理工大学《开源软件基础》课程大作业
**小组成员**：刘烁杉、韩澳洋、胡进宇、孙颢玮

---
## 文件说明

**calculate_release_intervals.py**：计算 VSCode 发布信息的时间间隔，并分析间隔的统计信息。
* `calculate_release_intervals`：根据发布时间对输入的releases列表排序，计算相邻发布之间的间隔天数并返回间隔列表。
* `analyze_release_intervals`：对输入的间隔列表进行分析，返回平均间隔、最小间隔和最大间隔。
  
**fetch_vscode_releases.py**：从 GitHub API 获取 VSCode 的发布信息。
* `get_info`：通过requests库向指定 URL 发送请求，处理分页，将所有结果合并返回。
* `fetch_vscode_releases`：构建获取 VSCode 发布信息的 URL，调用get_info获取并返回信息。
  
**save_releases_to_csv.py**：将 VSCode 的发布信息保存为 CSV 文件。
* `save_releases_to_csv`，用于将releases列表中的信息保存到Result/vscode_releases.csv文件中。
  
**plot_release_intervals.py**：绘制 VSCode 发布间隔的分布直方图。
* `plot_release_intervals`，绘制发布间隔的直方图，保存为Result/vscode_release_intervals_distribution.png。
  
**plot_release_timeline.py**：绘制 VSCode 发布的时间线图。
* `plot_release_timeline`，统计每年的发布数量，绘制发布时间线图，保存为Result/vscode_release_timeline.png。
  
**main.py**：作为主程序，协调各模块工作，包括获取信息、保存为 CSV、绘制图表、计算间隔统计信息等。
* 主文件，包含函数analyse_vscode_releases，调用其他模块的函数完成获取 VSCode 发布信息、保存到 CSV、绘制时间线图、计算并打印发布间隔信息、绘制间隔分布图等操作。
  
**order.md**：记录大作业的要求和推荐题目类型等信息。

---
## 使用方法
* 运行文件main.py
* 生成的图片和表格会保存在Result文件夹中
