import os
import csv

def save_releases_to_csv(releases):
    os.makedirs('Result', exist_ok=True)
    with open('Result/vscode_releases.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['tag_name', 'published_at', 'name', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for release in releases:
            writer.writerow({
                'tag_name': release['tag_name'],
                'published_at': release['published_at'],
                'name': release['name'],
                'body': release['body']
            })