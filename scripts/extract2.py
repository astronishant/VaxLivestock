import json
import re

log_path = r"C:\Users\Thoro\.gemini\antigravity\brain\352dabd9-f800-46b0-b2f6-a42be7c4a8b9\.system_generated\logs\transcript_full.jsonl"
html_content = ""
with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        # Look for the first complete read of index.html or the first time I edited it.
        # It's better to look for my "update.py" before I overwrote it.
        # Actually, in the log, the previous agent probably called `view_file` on `index.html`.
        content = data.get("content", "")
        if "The following code has been modified to include a line number before every line" in content and "index.html" in content and "Roboto" in content:
            # this is a view_file output.
            html_content += content + "\n"

with open("transcript_grep.txt", "w", encoding="utf-8") as out:
    out.write(html_content)
