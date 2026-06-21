import re

# Read parts
with open("part_head.html", "r", encoding="utf-8") as f:
    part_head = f.read()

with open("part_body.html", "r", encoding="utf-8") as f:
    part_body = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    old_html = f.read()

def extract_section(start_marker, end_marker):
    m = re.search(f"{start_marker}(.*?){end_marker}", old_html, re.DOTALL)
    return m.group(1) if m else ""

# Extract old views
old_security = extract_section('<!-- ==================== VIEW : SECURITY ==================== -->', '<!-- ==================== VIEW : NEWS ==================== -->')
old_news = extract_section('<!-- ==================== VIEW : NEWS ==================== -->', '<!-- ==================== VIEW : TOOL ==================== -->')
old_tool = extract_section('<!-- ==================== VIEW : TOOL ==================== -->', '<!-- ======================== FOOTER ======================== -->')

# Convert old views to Tailwind (basic wrappers)
security_view = f"""
<div id="view-security" class="view-section hidden flex-grow w-full max-w-[1280px] mx-auto px-16 py-8">
    <div class="bg-surface rounded-xl shadow-sm border border-outline-variant p-8">
        {old_security}
    </div>
</div>
"""
news_view = f"""
<div id="view-news" class="view-section hidden flex-grow w-full max-w-[1280px] mx-auto px-16 py-8">
    <div class="bg-surface rounded-xl shadow-sm border border-outline-variant p-8">
        {old_news}
    </div>
</div>
"""
tool_view = f"""
<div id="view-tool" class="view-section hidden flex-grow w-full max-w-[1280px] mx-auto px-16 py-8">
    <div class="bg-surface rounded-xl shadow-sm border border-outline-variant p-8">
        {old_tool}
    </div>
</div>
"""

# The Navbar (from user's snippet)
nav_bar = """
<header class="bg-surface shadow-sm sticky top-0 z-50 w-full transition-all duration-300">
    <div class="flex justify-between items-center px-8 w-full max-w-[1280px] mx-auto h-20">
        <div class="flex items-center gap-2">
            <span class="material-symbols-outlined filled text-primary text-3xl">vaccines</span>
            <span class="font-headline-md text-headline-md font-bold text-primary">VaxLivestock</span>
        </div>
        <nav class="hidden md:flex items-center gap-6">
            <a href="#" onclick="window.navigateTo('home'); return false;" id="nav-home" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md px-2 py-1">Home</a>
            <a href="#" onclick="window.navigateTo('diseases'); return false;" id="nav-diseases" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md px-2 py-1">Diseases</a>
            <a href="#" onclick="window.navigateTo('security'); return false;" id="nav-security" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md px-2 py-1">Security</a>
            <a href="#" onclick="window.navigateTo('news'); return false;" id="nav-news" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md px-2 py-1">News</a>
            <a href="#" onclick="window.navigateTo('tool'); return false;" id="nav-tool" class="text-on-surface-variant hover:text-primary transition-colors font-label-md text-label-md px-2 py-1">Manage Data</a>
        </nav>
        <div class="flex items-center gap-4">
            <div class="relative hidden md:block">
                <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-on-surface-variant">search</span>
                <input type="text" placeholder="Search..." class="bg-surface-container-low border border-outline rounded-full py-2 pl-10 pr-4 text-body-md focus:border-primary focus:ring-2 focus:ring-primary/20 w-64">
            </div>
            <button onclick="window.performLogout()" class="bg-primary-container text-on-primary-container font-label-md text-label-md px-6 py-2 rounded-lg hover:bg-primary-fixed transition-all shadow-sm flex items-center gap-2">
                <span class="material-symbols-outlined">logout</span> Logout
            </button>
        </div>
    </div>
</header>
"""

# The Home View (from user's snippet)
home_view = """
<div id="view-home" class="view-section hidden">
<section class="hero-bg py-20 lg:py-32 relative px-4 sm:px-6 lg:px-8 border-b border-outline-variant">
<div class="max-w-7xl mx-auto relative z-10 flex flex-col lg:flex-row items-center gap-12">
<div class="flex-1 text-center lg:text-left">
<h1 class="text-headline-lg-mobile lg:text-headline-lg text-on-surface mb-6">
          Govt. of Karnataka Veterinary Dept.
        </h1>
<p class="text-body-lg text-on-surface-variant mb-12 max-w-2xl mx-auto lg:mx-0">
          Ensuring transparency, combating fraud, and securing the health of rural livestock through automated, intelligent monitoring systems.
        </p>
<div class="grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-3xl mx-auto lg:mx-0">
<div class="bg-surface p-6 rounded-xl shadow-sm border border-outline-variant flex flex-col items-start gap-2">
<div class="w-10 h-10 rounded-full bg-primary-container flex items-center justify-center flex-shrink-0 mb-2">
<svg class="w-5 h-5 text-on-primary-container" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
</div>
<div>
<p class="text-headline-md text-on-surface">14,208</p>
<p class="text-label-sm text-on-surface-variant">Records Verified Today</p>
</div>
</div>
<div class="bg-surface p-6 rounded-xl shadow-sm border border-outline-variant flex flex-col items-start gap-2">
<div class="w-10 h-10 rounded-full bg-secondary-container flex items-center justify-center flex-shrink-0 mb-2">
<svg class="w-5 h-5 text-on-secondary-container" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5 13l4 4L19 7" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
</div>
<div>
<p class="text-headline-md text-on-surface">98.2%</p>
<p class="text-label-sm text-on-surface-variant">Compliance Rate</p>
</div>
</div>
<div class="bg-surface p-6 rounded-xl shadow-sm border border-outline-variant flex flex-col items-start gap-2">
<div class="w-10 h-10 rounded-full bg-error-container flex items-center justify-center flex-shrink-0 mb-2">
<svg class="w-5 h-5 text-on-error-container" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
</div>
<div>
<p class="text-headline-md text-on-surface">241</p>
<p class="text-label-sm text-on-surface-variant">Anomalies Flagged</p>
</div>
</div>
</div>
</div>
</div>
</section>

<section class="bg-surface-container py-16 px-4 sm:px-6 lg:px-8 text-center border-t border-outline-variant">
<div class="max-w-3xl mx-auto">
<h2 class="text-headline-md text-primary mb-4">
          Ready to process field data?
        </h2>
<p class="text-on-surface-variant mb-8 text-body-lg">
          Upload your Excel sheets to generate instant fraud and scheduling alerts.
        </p>
<button onclick="window.navigateTo('tool')" class="bg-primary hover:bg-on-primary-fixed-variant text-on-primary font-bold py-4 px-8 rounded-xl shadow-md transition-colors duration-200 uppercase tracking-wide text-label-md">
          Launch Manage Data Tool
        </button>
</div>
</section>
</div>
"""

# The Diseases View (from user's snippet)
diseases_view = """
<div id="view-diseases" class="view-section hidden w-full max-w-[1280px] mx-auto px-16 py-8">
<section class="flex flex-col md:flex-row justify-between items-start md:items-end gap-4 mb-8">
<div class="flex flex-col gap-2 max-w-2xl">
<h1 class="font-headline-lg text-headline-lg text-primary">Disease Directory</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant">Comprehensive database of common livestock diseases, complete with clinical signs, preventative measures, and official vaccination protocols.</p>
</div>
</section>

<div class="flex flex-col lg:flex-row gap-6">
<div class="flex-grow flex flex-col gap-8 lg:w-2/3 xl:w-3/4">
<section class="bg-primary-container text-on-primary-container rounded-xl p-8 flex flex-col md:flex-row gap-8 items-center shadow-sm">
<div class="flex-1 flex flex-col gap-2">
<span class="font-label-sm text-label-sm bg-primary text-on-primary px-3 py-1 rounded-full w-max mb-2">Featured Spotlight</span>
<h2 class="font-headline-lg text-headline-lg">Bovine Viral Diarrhea (BVD)</h2>
<p class="font-body-md text-body-md max-w-lg">A complex viral infection causing respiratory and reproductive issues in cattle. Early detection, biosecurity measures, and routine vaccination are critical for maintaining overall herd health and productivity.</p>
</div>
</section>

<section class="grid grid-cols-1 md:grid-cols-2 gap-6">
<article class="bg-surface border border-outline rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col p-4">
    <h2 class="font-headline-md text-headline-md text-on-surface mb-2">Foot and Mouth Disease (FMD)</h2>
    <p class="font-body-md text-body-md text-on-surface-variant">A highly contagious viral disease affecting cloven-hoofed animals. Characterized by fever and blister-like lesions on the tongue, lips, mouth, teats, and between the hooves.</p>
</article>
<article class="bg-surface border border-outline rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col p-4">
    <h2 class="font-headline-md text-headline-md text-on-surface mb-2">Brucellosis</h2>
    <p class="font-body-md text-body-md text-on-surface-variant">A bacterial infection causing reproductive failures, including abortions and infertility in livestock. Highly significant due to its zoonotic potential affecting human health.</p>
</article>
<article class="bg-surface border border-outline rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow flex flex-col p-4">
    <h2 class="font-headline-md text-headline-md text-on-surface mb-2">Anthrax</h2>
    <p class="font-body-md text-body-md text-on-surface-variant">An acute infectious disease caused by spore-forming bacteria. It can cause rapid death in livestock and poses severe risks to humans handling infected animals or products.</p>
</article>
</section>
</div>
</div>
</div>
"""

# Extract JS from part_body.html
js_logic = extract_section('<!-- JAVASCRIPT -->', '')
if not js_logic:
    # Read JS logic from original file
    js_match = re.search(r'<!-- ======================== JAVASCRIPT ======================== -->(.*)</body>', old_html, re.DOTALL)
    js_logic = js_match.group(1) if js_match else ""

# Modify JS navigateTo to use Tailwind classes
# Old: v.classList.remove('active'); ...
# New: v.classList.remove('active', 'block'); v.classList.add('hidden');
js_logic = js_logic.replace(
    "document.querySelectorAll('.view-container').forEach(function (v) { v.classList.remove('active'); });",
    "document.querySelectorAll('.view-section').forEach(function (v) { v.classList.remove('active', 'block'); v.classList.add('hidden'); });"
)
js_logic = js_logic.replace(
    "document.getElementById('view-' + viewName).classList.add('active');",
    "document.getElementById('view-' + viewName).classList.remove('hidden'); document.getElementById('view-' + viewName).classList.add('active', 'block');"
)
js_logic = js_logic.replace(
    "document.querySelectorAll('.nav-item').forEach(function (n) { n.classList.remove('active'); });",
    ""
)

# Also fix the login bypass logic in JS
js_logic = js_logic.replace(
    "document.getElementById('view-login').style.display = 'none';",
    "document.getElementById('view-login').classList.remove('flex', 'active'); document.getElementById('view-login').classList.add('hidden');"
)
js_logic = js_logic.replace(
    "document.getElementById('app-shell').style.display = 'flex';",
    "document.getElementById('app-shell').classList.remove('hidden'); document.getElementById('app-shell').classList.add('flex');"
)

# And logout logic
js_logic = js_logic.replace(
    "document.getElementById('app-shell').style.display = 'none';",
    "document.getElementById('app-shell').classList.remove('flex', 'active'); document.getElementById('app-shell').classList.add('hidden');"
)
js_logic = js_logic.replace(
    "document.getElementById('view-login').style.display = 'flex';",
    "document.getElementById('view-login').classList.remove('hidden'); document.getElementById('view-login').classList.add('flex', 'active');"
)


final_html = part_head + "\n" + extract_section('', '<!-- JAVASCRIPT -->') + f"""
<div id="app-shell" class="hidden flex-col w-full min-h-screen">
    {nav_bar}
    <main class="flex-grow w-full">
        {home_view}
        {diseases_view}
        {security_view}
        {news_view}
        {tool_view}
    </main>
</div>
<script>{js_logic}</script>
</body></html>
"""

# Replace custom old CSS vars with tailwind colors in old_tool, old_security, old_news
final_html = final_html.replace('color:var(--text-secondary)', 'class="text-on-surface-variant"')
final_html = final_html.replace('color:var(--primary)', 'class="text-primary"')
final_html = final_html.replace('class="btn"', 'class="bg-primary text-on-primary px-4 py-2 rounded-lg"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Build complete.")
