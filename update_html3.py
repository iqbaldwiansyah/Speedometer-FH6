import re

with open('e:/Speedometer-FH6/forza_overlay.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update font imports
font_old = r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Oxanium:wght@500;600;700&family=Rajdhani:wght@500;600;700&display=swap"\s+rel="stylesheet">'
font_new = '<link href="https://fonts.googleapis.com/css2?family=Oxanium:wght@500;600;700&family=Rajdhani:wght@500;600;700&family=Orbitron:wght@500;700&family=Roboto+Mono:wght@500;700&family=Oswald:wght@500;700&family=Teko:wght@500;700&family=Audiowide&display=swap" rel="stylesheet">'
content = re.sub(font_old, font_new, content)

# 2. Update CSS for tick text
tick_text_old = r'''    \.ticks text \{
      fill: var\(--text-dim\);
      font-family: var\(--tick-font, var\(--face\)\);
      font-weight: 600;
      font-size: 11px;
      text-anchor: middle;
      dominant-baseline: middle;
    \}'''
tick_text_new = '''    .ticks text {
      fill: var(--tick-text-color, var(--text-dim));
      font-family: var(--tick-font, var(--face));
      font-weight: 600;
      font-size: 11px;
      text-anchor: middle;
      dominant-baseline: middle;
    }'''
content = re.sub(tick_text_old, tick_text_new, content)

# 3. Update CSS for .value and .unit
val_old = r'''    \.value \{
      font-family: var\(--digital\);
      font-size: 26px;
      color: var\(--text-bright\);
      box-shadow: inset 0 2px 6px rgba\(0, 0, 0, \.6\);
    \}

    \.unit \{
      font-size: 11px;
      letter-spacing: 2px;
      color: var\(--text-dim\);
      margin-top: 3px;
    \}'''
val_new = '''    .value {
      font-family: var(--digital);
      font-size: 26px;
      color: var(--digital-value-color, var(--text-bright));
      box-shadow: inset 0 2px 6px rgba(0, 0, 0, .6);
    }

    .unit {
      font-size: 11px;
      letter-spacing: 2px;
      color: var(--digital-unit-color, var(--text-dim));
      margin-top: 3px;
    }'''
content = re.sub(val_old, val_new, content)

# 4. Update applyConfig
config_old = r'''      root\.style\.setProperty\('--tick-bright', conf\.warna_garis_tebal\);
      root\.style\.setProperty\('--bg', conf\.warna_background_utama\);'''
config_new = '''      root.style.setProperty('--tick-bright', conf.warna_garis_tebal);
      root.style.setProperty('--bg', conf.warna_background_utama);
      
      root.style.setProperty('--tick-text-color', conf.warna_angka_speedo || conf.warna_teks_gelap);
      root.style.setProperty('--digital-value-color', conf.warna_angka_digital || conf.warna_teks_terang);
      root.style.setProperty('--digital-unit-color', conf.warna_label_digital || conf.warna_teks_gelap);'''
content = re.sub(config_old, config_new, content)

with open('e:/Speedometer-FH6/forza_overlay.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done overlay update")
