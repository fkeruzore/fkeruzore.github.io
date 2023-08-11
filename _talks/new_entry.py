import sys

entry = sys.argv[1]
date = entry[:10]
# print(entry)

with open(f'./{entry}.md', 'w+') as f:
    f.write('---\n')
    f.write('title: ""\n')
    f.write('collection: talks\n')
    f.write('type: "Talk"\n')
    f.write(f'permalink: /talks/{entry}.md\n')
    f.write('venue: ""\n')
    f.write(f'date: {date}\n')
    f.write('location: ""\n')
    f.write('---\n')
    f.write('\n')
    f.write('Description\n')
