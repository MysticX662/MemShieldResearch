import re

with open('MemShield_WhitePaper_Final.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Sophisticated Typography & Styling Update (Anthropic/OpenAI aesthetic)
advanced_css = """
/* RESET & ROOT */
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --white:#ffffff;
  --off:#fafaf9;
  --page-bg:#f3f4f6;
  --ink:#171717;
  --ink2:#404040;
  --ink3:#737373;
  --rule:#e5e5e5;
  --rule2:#f5f5f5;
  --brand:#0f172a;
  --brand2:#3b82f6;
  --brand-light:#eff6ff;
  --brand-mid:#bfdbfe;
  --accent-green:#166534;
  --accent-red:#991b1b;
  --accent-amber:#92400e;
  
  --serif: 'Charter', 'Bitstream Charter', 'Sitka Text', 'Cambria', serif;
  --sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --mono: 'JetBrains Mono', 'Fira Code', 'Menlo', monospace;
}

html{background:var(--page-bg);-webkit-font-smoothing:antialiased; text-rendering: optimizeLegibility;}

body{
  color:var(--ink);
  font-family:var(--serif);
  font-size:10.5pt;
  line-height:1.75;
  max-width:8.5in;
  margin:0 auto;
  background:var(--white);
  box-shadow:0 0 20px rgba(0,0,0,0.05);
}

/* Page Break Utility */
.page-break {
  page-break-before: always;
  break-before: page;
}

/* COVER */
.cover-header{
  background:var(--white);
  padding:1.5in 1.25in 0.5in 1.25in;
  display:flex;align-items:center;justify-content:space-between;
}
.cover-logo{height:48px;}
.cover-header-right{
  font-family:var(--sans);font-size:8.5pt;letter-spacing:.05em;
  text-transform:uppercase;color:var(--ink3);font-weight:600;
}

.cover{height:11in; display:flex;flex-direction:column; page-break-after: always; break-after: page;}
.cover-body{flex:1;padding:0 1.25in 1in 1.25in;display:flex;flex-direction:column; justify-content:center;}

.pill-row{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:2rem}
.pill{
  font-family:var(--sans);font-size:8pt;font-weight:500;
  letter-spacing:.05em;text-transform:uppercase;
  background:var(--off);color:var(--ink2);
  border:1px solid var(--rule);border-radius:4px;
  padding:.25rem .75rem;
}

.cover-title-wrap{margin-bottom:1.5rem}
.cover-title{
  font-family:var(--sans);font-size:32pt;font-weight:700;
  color:var(--brand);line-height:1.1; letter-spacing:-0.02em;
}
.cover-subtitle{
  font-family:var(--serif);font-size:14pt;font-weight:400;
  color:var(--ink2);margin-top:1.5rem; line-height: 1.5;
}

.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:4rem; border-top: 2px solid var(--brand); padding-top: 1.5rem;}
.meta-label{
  font-family:var(--sans);font-size:8pt;font-weight:600;
  letter-spacing:.1em;text-transform:uppercase;color:var(--ink3);margin-bottom:.5rem;
}
.meta-val{font-family:var(--sans);font-size:10pt;color:var(--ink);line-height:1.6}

.abstract-box{
  margin-top: 3rem;
}
.abstract-label{
  font-family:var(--sans);font-size:12pt;font-weight:600;
  color:var(--brand);margin-bottom:1rem; border-bottom: 1px solid var(--rule); padding-bottom: 0.5rem;
}
.abstract-body p{
  font-family:var(--serif);font-size:10.5pt;color:var(--ink2);
  line-height:1.75;text-align:justify;
}

/* MAIN CONTENT */
.paper{padding:0;}
.page-content {
  padding: 1in 1.25in;
  position: relative;
}

.running-head{
  position: absolute;
  top: 0.6in;
  left: 1.25in;
  right: 1.25in;
  display:flex;justify-content:space-between;align-items:center;
  font-family:var(--sans);font-size:8pt;
  letter-spacing:.05em;color:var(--ink3);
  padding-bottom:.5rem;
  border-bottom:1px solid var(--rule);
}

/* TYPOGRAPHY */
.h1-section{
  font-family:var(--sans);font-size:18pt;font-weight:600;
  text-align:left;color:var(--brand);
  letter-spacing:-0.01em;
  margin:0 0 2rem 0;
  page-break-before: always;
  break-before: page;
}

.h1-section::after{ display: none; }

.h2{
  font-family:var(--sans);font-size:14pt;font-weight:600;
  letter-spacing:-0.01em;
  text-align:left;color:var(--brand);
  margin:2.5rem 0 1rem 0;
  page-break-after: avoid;
  break-after: avoid;
}
.h3{
  font-family:var(--sans);font-size:11pt;font-weight:600;
  text-align:left;color:var(--ink);
  margin:2rem 0 0.75rem 0;
  page-break-after: avoid;
  break-after: avoid;
}

p{
  font-family:var(--serif);font-size:10.5pt;
  line-height:1.75;margin-bottom:1.25rem;color:var(--ink);
  text-align:justify;
  orphans: 4; widows: 4;
}
p.lead{
  font-family:var(--serif);font-size:12pt;
  color:var(--ink2);line-height:1.7;text-align:justify;
  margin-bottom:2.5rem;
}

/* BLOCKS */
.figure{margin:3rem 0; break-inside: avoid; page-break-inside: avoid;}
.fig-inner{border:1px solid var(--rule); border-radius: 4px; overflow:hidden;}
.fig-img{width:100%;display:block}
.fig-caption{
  padding:1rem 0 0 0;
  font-family:var(--sans);font-size:9pt;color:var(--ink2);line-height:1.6;
}

.table-wrap{margin:3rem 0; break-inside: avoid; page-break-inside: avoid;}
.tbl{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:9pt}
.tbl caption{
  font-family:var(--sans);font-size:9.5pt;font-weight:600;color:var(--ink);
  text-align:left;padding-bottom:1rem;
}
.tbl th{
  font-weight:600;text-align:left;padding:.75rem 1rem;color:var(--ink);
  border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);
  background: var(--off);
}
.tbl td{padding:.75rem 1rem;color:var(--ink2);border-bottom:1px solid var(--rule)}

.arch-panel{
  background:var(--white);border:1px solid var(--rule); border-radius: 6px;
  padding:2rem;margin:3rem 0; break-inside: avoid; page-break-inside: avoid;
  box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
.arch-layer{
  display:flex;align-items:stretch;margin-bottom:1.5rem;
  border:1px solid var(--rule); border-radius: 6px; overflow:hidden;
}
.arch-layer:last-child{margin-bottom:0}
.arch-badge{
  width:80px;min-width:80px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:1rem;
  background: var(--off); border-right: 1px solid var(--rule);
}
.arch-badge .ln-num{
  font-family:var(--sans);font-size:16pt;font-weight:600;color:var(--brand);
}
.arch-badge .ln-tag{
  font-family:var(--mono);font-size:7pt;letter-spacing:.05em;
  text-transform:uppercase;color:var(--ink3);margin-top:.25rem;
}
.arch-content{padding:1.5rem;background:#fff;flex:1;}

.formula-wrap{
  background:var(--off); border-radius: 6px;
  padding:1.5rem 2rem;margin:2.5rem 0;
  text-align: center;
  break-inside: avoid; page-break-inside: avoid;
}

.code-wrap{
  background: #f8fafc; border: 1px solid var(--rule); border-radius: 6px;
  margin:2.5rem 0; break-inside: avoid; page-break-inside: avoid;
}
.code-head{
  background: #f1f5f9; padding:.75rem 1.25rem; border-bottom: 1px solid var(--rule);
  font-family:var(--sans);font-size:8pt;color:var(--ink3);font-weight:600; text-transform: uppercase; letter-spacing: 0.05em;
}
.code-body{
  padding:1.5rem;font-family:var(--mono);font-size:9pt;line-height:1.6;color:var(--ink);
}

.callout{
  border:1px solid var(--rule); border-left:4px solid var(--brand); border-radius: 0 6px 6px 0;
  background:var(--off);padding:1.5rem 2rem;margin:2.5rem 0;
  break-inside: avoid; page-break-inside: avoid;
}
.callout.finding{border-left-color:var(--accent-green);}
.callout.caution{border-left-color:var(--accent-red);}
.callout p{font-family:var(--sans);font-size:10pt; line-height:1.6; color: var(--ink2);}

.pull-quote{
  margin:3rem 0;padding:2rem;
  border-top: 1px solid var(--brand); border-bottom: 1px solid var(--brand);
  text-align: center;
  break-inside: avoid; page-break-inside: avoid;
}
.pull-quote p{
  font-family:var(--serif);font-size:16pt;font-style:italic;
  color:var(--brand);line-height:1.5; margin:0;
}

/* LISTS */
.numbered-list { margin: 1.5rem 0 2.5rem 2rem; }
.numbered-list li { margin-bottom: 0.75rem; padding-left: 0.5rem; }

/* PRINT RULES */
@page { size: letter; margin: 0; }
@media print {
  body { margin: 0; max-width: 100%; box-shadow: none; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .cover { height: 11in; }
}
"""

# Replace css between <style> and </style>
html = re.sub(r'<style>.*?</style>', f'<style>\n{advanced_css}\n</style>', html, flags=re.DOTALL)

# Inject page wrappers for consistent content flow
# Find all <div class="h1-section"> and split the content to wrap them in page-content pads
html = html.replace('<div class="paper">', '')
html = html.replace('</div><!-- /paper -->', '')

parts = html.split('<div class="h1-section"')
new_html = parts[0]

for i in range(1, len(parts)):
    # The first split will be everything up to the first h1-section
    section_content = '<div class="h1-section"' + parts[i]
    new_html += f'\n<div class="page-break"></div>\n<div class="page-content">\n{section_content}\n</div>\n'

with open('MemShield_WhitePaper_Final.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
