import json

log_path = r"C:\Users\Thoro\.gemini\antigravity\brain\352dabd9-f800-46b0-b2f6-a42be7c4a8b9\.system_generated\logs\transcript_full.jsonl"
with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("type") == "TOOL_RESPONSE" and "index.html" in data.get("content", "") and "<style>" in data.get("content", ""):
            content = data["content"]
            # Look for Roboto font link
            if "Roboto" in content:
                print("FOUND IT!")
                with open("old_css_dump.txt", "w", encoding="utf-8") as out:
                    out.write(content)
                break
