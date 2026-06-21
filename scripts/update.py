import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_style = """    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>
    <style>
        :root {
            --primary: #2563EB;
            --primary-hover: #1D4ED8;
            --surface: #FFFFFF;
            --background: #F8FAFC;
            --text-main: #1E293B;
            --text-secondary: #64748B;
            --border: #E2E8F0;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --high-risk: #EF4444;
            --warning: #F59E0B;
            --safe: #10B981;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }

        body { background: var(--background); color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; }

        /* ---------- Buttons ---------- */
        .btn {
            background: var(--primary); color: #fff; border: none;
            padding: 10px 20px; font-size: 0.875rem; font-weight: 500;
            border-radius: 6px; cursor: pointer;
            transition: background 0.2s ease, transform 0.1s;
            box-shadow: var(--shadow-sm);
        }
        .btn:hover { background: var(--primary-hover); transform: translateY(-1px); box-shadow: var(--shadow-md); }
        .btn-outline { background: transparent; color: var(--text-main); border: 1px solid var(--border); box-shadow: none; font-weight: 500; }
        .btn-outline:hover { background: #F1F5F9; border-color: #CBD5E1; }

        /* ---------- View Engine ---------- */
        .view-container { display: none; flex: 1; flex-direction: column; width: 100%; animation: fadeIn 0.3s ease; }
        .view-container.active { display: flex; }
        #app-shell { display: flex; flex-direction: column; min-height: 100vh; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

        /* ---------- VIEW A: Login (Hidden by default now) ---------- */
        #view-login { display: none !important; }

        /* ---------- Navbar ---------- */
        nav {
            background: var(--surface); border-bottom: 1px solid var(--border);
            padding: 0 32px; height: 72px; display: flex; align-items: center;
            justify-content: space-between; position: sticky; top: 0; z-index: 1000;
        }
        .nav-brand { font-size: 20px; font-weight: 600; color: var(--text-main); display: flex; align-items: center; gap: 12px; cursor: pointer; letter-spacing: -0.02em; }
        .nav-links { display: flex; gap: 8px; align-items: stretch; height: 100%; }
        .nav-item {
            color: var(--text-secondary); text-decoration: none; font-size: 14px;
            font-weight: 500; cursor: pointer; padding: 0 16px; border-radius: 0;
            display: flex; align-items: center; border-bottom: 2px solid transparent;
            transition: color 0.2s, border-color 0.2s;
        }
        .nav-item:hover { color: var(--text-main); }
        .nav-item.active { color: var(--primary); border-bottom: 2px solid var(--primary); }

        /* ---------- Generic Container ---------- */
        .content-section { max-width: 1200px; margin: 0 auto; padding: 48px 24px; width: 100%; }
        .section-title { font-size: 24px; font-weight: 600; margin-bottom: 32px; letter-spacing: -0.01em; color: var(--text-main); }

        /* ---------- VIEW B: Home ---------- */
        .hero {
            background: var(--surface); padding: 80px 24px; text-align: center;
            border-bottom: 1px solid var(--border); position: relative;
        }
        .hero h1 { font-size: 42px; font-weight: 700; margin-bottom: 20px; letter-spacing: -0.02em; color: var(--text-main); }
        .hero p  { font-size: 18px; color: var(--text-secondary); max-width: 800px; margin: 0 auto; line-height: 1.6; }

        .stats-container {
            max-width: 1200px; margin: -40px auto 40px; padding: 0 24px;
            display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 24px; position: relative; z-index: 10;
        }
        .stat-card {
            background: var(--surface); padding: 32px 24px; border-radius: 12px;
            box-shadow: var(--shadow-md); border: 1px solid var(--border);
            display: flex; align-items: flex-start; gap: 20px; transition: transform 0.2s, box-shadow 0.2s;
        }
        .stat-card:hover { transform: translateY(-4px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }
        .stat-icon {
            width: 56px; height: 56px; border-radius: 12px;
            background: #EFF6FF; color: var(--primary);
            display: flex; align-items: center; justify-content: center; flex-shrink: 0;
        }
        .stat-info h4 { font-size: 32px; font-weight: 700; margin-bottom: 4px; letter-spacing: -0.02em; }
        .stat-info p  { font-size: 14px; color: var(--text-secondary); font-weight: 500; }

        .launch-banner {
            background: var(--surface); border: 1px solid var(--border);
            border-radius: 12px; padding: 48px; text-align: center;
            box-shadow: var(--shadow-sm); margin-top: 24px;
        }
        .launch-banner h3 { font-size: 24px; font-weight: 600; margin-bottom: 16px; color: var(--text-main); }

        /* ---------- Educational Cards ---------- */
        .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; }
        .edu-card {
            background: var(--surface); border: 1px solid var(--border);
            border-radius: 12px; overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s, box-shadow 0.2s;
        }
        .edu-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); }
        .edu-img { height: 180px; background-size: cover; background-position: center; border-bottom: 1px solid var(--border); }
        .edu-content { padding: 24px; }
        .edu-content h3 { font-size: 18px; font-weight: 600; margin-bottom: 12px; color: var(--text-main); }
        .edu-content p  { font-size: 15px; line-height: 1.6; color: var(--text-secondary); }

        /* ---------- VIEW C: Tool ---------- */
        #view-tool .tool-header h2 { font-size: 32px; font-weight: 600; letter-spacing: -0.02em; margin-bottom: 12px; }

        .upload-zone {
            background: var(--surface); border: 2px dashed #CBD5E1;
            border-radius: 12px; padding: 80px 20px; text-align: center;
            cursor: pointer; transition: all 0.2s; margin-bottom: 40px;
        }
        .upload-zone:hover, .upload-zone.dragover { background: #F8FAFC; border-color: var(--primary); }
        .upload-zone svg { width: 64px; height: 64px; fill: var(--primary); margin-bottom: 24px; opacity: 0.9; }
        #file-input { display: none; }

        /* --- Processing Overlay --- */
        .processing-overlay {
            display: none; flex-direction: column; align-items: center; justify-content: center;
            background: var(--surface); border: 1px solid var(--border); border-radius: 12px;
            box-shadow: var(--shadow-md); padding: 80px 40px; text-align: center; margin-bottom: 40px;
        }
        .processing-overlay.active { display: flex; }
        .spinner {
            width: 56px; height: 56px; border: 4px solid var(--border);
            border-top-color: var(--primary); border-radius: 50%;
            animation: spin 0.8s linear infinite; margin-bottom: 32px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        .processing-overlay h3 { font-size: 22px; font-weight: 600; margin-bottom: 16px; color: var(--text-main); }
        .processing-overlay .progress-track {
            width: 320px; max-width: 100%; height: 6px; background: #E2E8F0;
            border-radius: 3px; overflow: hidden; margin-bottom: 32px;
        }
        .processing-overlay .progress-fill {
            height: 100%; width: 0%; background: var(--primary);
            border-radius: 3px; transition: width 0.25s linear;
        }
        .fact-text { font-size: 15px; color: var(--text-secondary); line-height: 1.6; max-width: 540px; min-height: 48px; }

        /* --- Dashboard Results --- */
        .dashboard-results { display: none; gap: 32px; flex-direction: column; }
        .data-panel {
            background: var(--surface); border: 1px solid var(--border);
            border-radius: 12px; box-shadow: var(--shadow-sm); overflow: hidden;
        }
        .panel-header {
            padding: 20px 24px; border-bottom: 1px solid var(--border);
            display: flex; justify-content: space-between; align-items: center; background: var(--surface);
        }
        .panel-header h3 { font-size: 18px; font-weight: 600; color: var(--text-main); }
        .table-responsive { overflow-x: auto; max-height: 500px; }
        table { width: 100%; border-collapse: collapse; text-align: left; white-space: nowrap; }
        th, td { padding: 16px 24px; border-bottom: 1px solid var(--border); font-size: 14px; }
        th {
            font-weight: 600; color: var(--text-secondary); position: sticky; top: 0;
            background: #F8FAFC; box-shadow: 0 1px 0 var(--border); z-index: 10; text-transform: uppercase; font-size: 12px; letter-spacing: 0.05em;
        }
        tr:hover td { background: #F8FAFC; }
        .badge { padding: 6px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; display: inline-block; letter-spacing: 0.02em; }
        .badge.high-risk, .badge.overdue { background: #FEF2F2; color: #DC2626; border: 1px solid #FECACA; }
        .badge.warning, .badge.due-week  { background: #FFFBEB; color: #D97706; border: 1px solid #FDE68A; }
        .badge.safe, .badge.upcoming     { background: #ECFDF5; color: #059669; border: 1px solid #A7F3D0; }

        /* ---------- Footer ---------- */
        footer { background: #0F172A; color: #94A3B8; padding: 60px 24px; margin-top: auto; }
        .footer-content { max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 48px; }
        .footer-section h4 { color: #F8FAFC; font-size: 16px; font-weight: 600; margin-bottom: 20px; letter-spacing: 0.02em; }
        .footer-section p  { font-size: 14px; line-height: 1.6; }
        .footer-section a  { color: #94A3B8; text-decoration: none; display: block; margin-bottom: 12px; font-size: 14px; transition: color 0.2s; }
        .footer-section a:hover { color: #F8FAFC; }
        .dev-credit {
            border-top: 1px solid #1E293B; margin-top: 60px; padding-top: 24px;
            font-size: 13px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 12px;
        }
        .dev-badge { background: #1E293B; color: #F8FAFC; padding: 10px 20px; border-radius: 8px; display: inline-flex; flex-direction: column; align-items: center; }
        .dev-badge strong { color: #38BDF8; font-size: 14px; font-weight: 600; }
    </style>"""

content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Roboto[^>]+>[\s\S]*?</style>', new_style, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
