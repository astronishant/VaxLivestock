import re

with open("part_head.html", "r", encoding="utf-8") as f:
    part_head = f.read()

with open("part_body.html", "r", encoding="utf-8") as f:
    part_body = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    current_html = f.read()

# Grab the app-shell and script from current_html
m = re.search(r'<div id="app-shell".*', current_html, re.DOTALL)
if m:
    app_shell_and_script = m.group(0)
    
    final_html = part_head + "\n" + part_body + "\n" + app_shell_and_script
    
    with open("index.html", "w", encoding="utf-8") as out:
        out.write(final_html)
    print("Fixed!")
else:
    print("Could not find app-shell")
