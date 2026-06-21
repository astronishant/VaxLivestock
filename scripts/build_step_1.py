import re

with open("index.html", "r", encoding="utf-8") as f:
    old_html = f.read()

# Extract old views and JS
def extract_section(start_marker, end_marker):
    m = re.search(f"{start_marker}(.*?){end_marker}", old_html, re.DOTALL)
    return m.group(1) if m else ""

login_content = extract_section('<!-- ======================== VIEW A : LOGIN ======================== -->', '<!-- ==================== VIEW B : HOME ==================== -->')
if not login_content: # Fallback if markers changed
    # Actually, we can just rewrite the login view in Tailwind
    login_view = """
<div id="view-login" class="view-section active flex items-center justify-center min-h-screen w-full bg-surface">
    <div class="bg-surface-container-lowest p-8 rounded-xl shadow-lg border border-outline-variant w-full max-w-md text-center">
        <span class="material-symbols-outlined filled text-primary text-5xl mb-4">vaccines</span>
        <h2 class="text-headline-md text-on-surface mb-2">VaxLivestock Login</h2>
        <p class="text-body-md text-on-surface-variant mb-6">Enter department credentials to access the system.</p>
        
        <div class="space-y-4">
            <input type="text" id="login-email" placeholder="Email (admin@trackvax.in)" class="w-full bg-surface-container-low border border-outline rounded-lg px-4 py-3 text-body-md focus:border-primary focus:ring-2 focus:ring-primary/20">
            <input type="password" id="login-pwd" placeholder="Password (admin123)" class="w-full bg-surface-container-low border border-outline rounded-lg px-4 py-3 text-body-md focus:border-primary focus:ring-2 focus:ring-primary/20">
            <button onclick="window.performLogin()" class="w-full bg-primary hover:bg-primary-fixed-variant text-on-primary font-bold py-3 px-4 rounded-lg shadow-md transition-colors text-label-md mt-4">LOGIN</button>
        </div>
    </div>
</div>
"""
else:
    login_view = """<div id="view-login" class="view-section active min-h-screen flex items-center justify-center bg-surface">""" + login_content + """</div>"""


# Extract JS
js_logic = re.search(r'<!-- ======================== JAVASCRIPT ======================== -->(.*)</body>', old_html, re.DOTALL)
if js_logic:
    js_content = "<!-- JAVASCRIPT -->" + js_logic.group(1)
else:
    # Try another regex
    js_match = re.search(r'<script>(.*?)</script>\s*</body>', old_html, re.DOTALL)
    js_content = "<script>" + js_match.group(1) + "</script>" if js_match else ""

# Create part_body.html
with open("part_body.html", "w", encoding="utf-8") as f:
    f.write(login_view)
