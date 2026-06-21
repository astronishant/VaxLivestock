import re

with open("transcript_grep.txt", "r", encoding="utf-8") as f:
    content = f.read()

# We just need to extract the lines that start with "<number>: "
lines = content.split('\n')
parsed_lines = {}

for line in lines:
    m = re.match(r'^(\d+):\s(.*)$', line)
    if m:
        line_num = int(m.group(1))
        text = m.group(2)
        parsed_lines[line_num] = text

# Sort and reconstruct
html_lines = []
for i in sorted(parsed_lines.keys()):
    html_lines.append(parsed_lines[i])

with open("index.html", "w", encoding="utf-8") as f:
    f.write('\n'.join(html_lines))

print(f"Reconstructed {len(parsed_lines)} lines.")
