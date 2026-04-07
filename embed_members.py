import json, re

# Load members
with open("D:/projects/MIMI/群文件整理/extracted_members.json", "r", encoding="utf-8") as f:
    members = json.load(f)

# Generate compact JSON (single line, no newlines)
compact = json.dumps(members, ensure_ascii=False, separators=(',', ':'))
assert '\n' not in compact, "Compact JSON must be single line!"

print(f"Members: {len(members)}")
print(f"First 5: {[m['name'] for m in members[:5]]}")
print(f"Last 5: {[m['name'] for m in members[-5:]]}")
print(f"Compact length: {len(compact)}")

# Read HTML
with open("D:/projects/MIMI/群文件整理/index (2).html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace DEFAULT_MEMBERS using lambda to prevent \n interpretation
old_pattern = r"const DEFAULT_MEMBERS = \[.*?\];"
new_code = f"const DEFAULT_MEMBERS = {compact};"
html_new = re.sub(old_pattern, lambda m: new_code, html, count=1, flags=re.DOTALL)

if html_new == html:
    print("ERROR: Pattern not found!")
else:
    # Bump version
    html_new = html_new.replace("const DATA_VERSION = '2026-04-05-v73'", "const DATA_VERSION = '2026-04-07-v74'")

    with open("D:/projects/MIMI/群文件整理/index (2).html", "w", encoding="utf-8") as f:
        f.write(html_new)

    print("HTML updated to v74 with 20 new members (237 total)")
