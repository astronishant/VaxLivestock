import re

# Read the full file from the codex folder (which has the bad CSS but full HTML)
with open("vaccince 2.0 codex/index.html", "r", encoding="utf-8") as f:
    full_html = f.read()

# Read the reconstructed partial file (which has the original CSS)
with open("transcript_grep.txt", "r", encoding="utf-8") as f:
    partial_html = f.read()

# Parse partial html to strip the line numbers!
lines = partial_html.split('\n')
parsed_lines = {}
for line in lines:
    m = re.match(r'^(\d+):\s(.*)$', line)
    if m:
        line_num = int(m.group(1))
        text = m.group(2)
        parsed_lines[line_num] = text

html_lines = []
for i in sorted(parsed_lines.keys()):
    html_lines.append(parsed_lines[i])
clean_partial_html = '\n'.join(html_lines)


# Extract the <style> block from clean_partial_html
match_old_style = re.search(r'<style>[\s\S]*?</style>', clean_partial_html)
if match_old_style:
    old_style = match_old_style.group(0)
    print("Found old style!")
else:
    print("Old style not found in partial html")

# Also need to restore the original font link
match_old_font = re.search(r'<link href="https://fonts\.googleapis\.com/css2\?family=Roboto[^>]+>', clean_partial_html)
old_font = match_old_font.group(0) if match_old_font else ""

# Replace the style block in full_html
if match_old_style:
    full_html = re.sub(r'<style>[\s\S]*?</style>', old_style, full_html)
if old_font:
    full_html = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^>]+>', old_font, full_html)

# Now we need to undo the changes made to the HTML (bypassing login)
# Replace active classes to restore login visibility by default
full_html = full_html.replace('<div id="view-login" class="view-container">', '<div id="view-login" class="view-container active">')
full_html = full_html.replace('<div id="view-home" class="view-container active">', '<div id="view-home" class="view-container">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Restoration complete.")
