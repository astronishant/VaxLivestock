import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = """            <div class="launch-banner" style="margin-top: 40px;">
                <h3>Ready to process field data?</h3>
                <p style="color:var(--text-secondary);margin-bottom:24px">Upload your Excel sheets to generate instant fraud and scheduling alerts.</p>
                <button class="btn" style="padding:12px 32px;font-size:16px" onclick="window.navigateTo('tool')">Launch TrackUrVaccine Dashboard</button>
            </div>
        </div>
    </div>"""

replacement = """            <div class="launch-banner" style="margin-top: 40px;">
                <h3>Ready to process field data?</h3>
                <p style="color:var(--text-secondary);margin-bottom:24px">Upload your Excel sheets to generate instant fraud and scheduling alerts.</p>
                <button class="btn" style="padding:12px 32px;font-size:16px" onclick="window.navigateTo('tool')">Launch TrackUrVaccine Dashboard</button>
            </div>
    </div>"""

content = content.replace(target, replacement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
