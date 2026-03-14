import json, re

# ============================================================
# 158 members from WeChat group member list screenshots (folder 6)
# This is the ORDERING reference only
# ============================================================
screenshot_order = [
    "Patrick Liu",       # 1
    "颜嵘",              # 2
    "黄铠",              # 3
    "亚当 Adam",         # 4
    "Henry",             # 5
    "Richard",           # 6
    "何宇涵",            # 7
    "必正",              # 8
    "YT Jia",            # 9
    "FF YQ",             # 10
    "Jim G",             # 11
    "高巍",              # 12
    "Weijia",            # 13
    "金汐",              # 14
    "周自横",            # 15
    "Lucas",             # 16
    "AndyHu",            # 17
    "Nan Luo",           # 18
    "medal",             # 19
    "咕咚波哥",          # 20
    "天晴了",            # 21
    "Trigg-日东",        # 22
    "Nancy 兰馨",        # 23
    "谷雨",              # 24
    "马麟",              # 25
    "Mingke",            # 26
    "17@evomap.ai",      # 27
    "阎志涛",            # 28
    "宇宸",              # 29
    "大铭",              # 30
    "南川 WhyMark",      # 31
    "Tianrun Yang",       # 32
    "skyrim",            # 33
    "黄祯 Zohar",        # 34
    "Jeff",              # 35
    "邓侃",              # 36
    "Alan Li",           # 37
    "lambda",            # 38
    "Aiden Chaoyang He", # 39
    "胡布斯",            # 40
    "江枫",              # 41
    "梁海波",            # 42
    "知县",              # 43
    "伍晓东",            # 44
    "郎瀚威 Will",       # 45
    "Lihang",            # 46
    "Ray",               # 47
    "王Alex",            # 48
    "Charles",           # 49
    "Hao",               # 50
    "杨子超 e/acc",      # 51
    "Beyond the Sky",    # 52
    "B2B 域名",          # 53
    "Sawyer",            # 54
    "TianPan.co",        # 55
    "荃",                # 56
    "Evan Chen",         # 57
    "Leooooooo",         # 58
    "吕一我",            # 59
    "V V",               # 60
    "铁人不需要休息",    # 61
    "王意翔",            # 62
    "目成",              # 63
    "Robin 齐彦博",      # 64
    "致饰",              # 65
    "Corynne",           # 66
    "尤洋",              # 67
    "赵承乾Mike",        # 68
    "杨劲松 Edward",     # 69
    "kevin",             # 70
    "Donny",             # 71
    "Finn",              # 72
    "lr",                # 73
    "Jun Wang",          # 74
    "zwx",               # 75
    "Bill",              # 76
    "新媒沈阳",          # 77
    "李",                # 78
    "Mark@AI",           # 79
    "Elaine",            # 80
    "赵富宇Arthur",      # 81
    "王文峰",            # 82
    "朱来Steve",         # 83
    "陈杰",              # 84
    "Allyly",            # 85
    "张蕾-Shanda Growth",# 86
    "贾明华",            # 87
    "哲",                # 88
    "Peppaca",           # 89
    "蓝珣QiQi",          # 90
    "Chen",              # 91
    "刘卓德",            # 92
    "Qi Deng",           # 93
    "毛华",              # 94
    "Kaitan",            # 95
    "金石",              # 96
    "John",              # 97
    "常识",              # 98
    "Brandon Chen",      # 99
    "ich liebe dich",    # 100
    "Yu",                # 101
    "zhaboller华",       # 102
    "睿",                # 103
    "吴昊",              # 104
    "Lynn",              # 105
    "July to Angel",     # 106
    "Matrix",            # 107
    "PeterXu",           # 108
    "邓天卓Gene",        # 109
    "孔慕Karin",         # 110
    "Lijing Ying",       # 111
    "子伟",              # 112
    "frank",             # 113
    "琉璃厨",            # 114
    "Philip",            # 115
    "郑光辉",            # 116
    "张健",              # 117
    "崇光恒",            # 118
    "Yonghui",           # 119
    "邝有成",            # 120
    "李榜主",            # 121
    "蚂蚁战投",          # 122
    "Kelly Peng",        # 123
    "Harrison 姜浩楠",   # 124
    "张镇勰",            # 125
    "Cobo 云启资本",     # 126
    "Jack Jin",          # 127
    "范策Sheng",         # 128
    "李佳芮",            # 129
    "Apollo",            # 130
    "m",                 # 131
    "一丁",              # 132
    "小明他爸",          # 133
    "ZZ",                # 134
    "Sylvan",            # 135
    "LBF",               # 136
    "Grace",             # 137
    "KS",                # 138
    "Victoria",          # 139
    "Weimo刘未未",       # 140
    "Hanlin",            # 141
    "Hao2",              # 142 (第二个Hao，之前是沈奕辰)
    "Niki Li",           # 143
    "Gil",               # 144
    "yc",                # 145
    "erickfang",         # 146
    "Lilyann",           # 147
    "Vance Chen",        # 148
    "迟小羽",            # 149
    "白猫",              # 150
    "Zoe兆希",           # 151
    "Jun",               # 152
    "ZK",                # 153
    "jiezhu",            # 154
    "cursor何",          # 155
    "sean",              # 156
    "童蓝宇",            # 157
    "Sarah Pu",          # 158
]

assert len(screenshot_order) == 158

# Screenshot name -> existing member record name
# Names from chat screenshots are kept (first priority)
# Only group list names used for people who never spoke
match_map = {
    "金汐": "金汐 (Lisa)",
    "周自横": "Joseph (周自横)",
    "AndyHu": "AndyHu@尔湾胡哥",
    "medal": "Medal (黄总)",
    "17@evomap.ai": "17@evomap.ai (吴阳)",
    "阎志涛": "阎志涛 (闵志涛)",
    "Tianrun Yang": "Tianrun Yang (杨天润)",
    "黄祯 Zohar": "黄祯 Zohar e/acc",
    "Aiden Chaoyang He": "Aiden Chaoyang He (何朝阳)",
    "郎瀚威 Will": "郎瀚威 Will @硅谷",
    "FF YQ": "FF YQ (杨永强)",
    "铁人不需要休息": "铁人不需要休息 (Nil)",
    "目成": "目成 (Max)",
    "致饰": "致饰_",
    "赵承乾Mike": "赵承乾 Mike",
    "lr": "李然",
    "李": "李冠霖",
    "朱来Steve": "朱来 Steve",
    "蓝珣QiQi": "蓝珣 QIQI",
    "Brandon Chen": "Brandon Chen 陈春宇",
    "ich liebe dich": "ich liebe dich (Celine)",
    "zhaboller华": "Joshua (zhaboller华)",
    "邓天卓Gene": "邓天卓 Gene",
    "Cobo 云启资本": "Cobo (云启资本)",
    "小明他爸": "Zhiben Chen (小明他爸)",
    "LBF": "方博立 (LBF)",
    "Weimo刘未未": "Weimo 刘未未",
    "伍晓东": "伍晓东 (Jason Wu)",
    "Trigg-日东": "肖日东 (Trigg Shaw)",
    "天晴了": "天晴了 (Henry Yu)",
    "胡布斯": "胡布斯 (胡显刚)",
    "Evan Chen": "Evan Chen (陈一帆)",
    "Grace": "Grace (陈蕾宇)",
    "Hao2": "沈奕辰",  # 第142位，之前是沈奕辰
    "杨子超 e/acc": "杨子超 e/acc",
}

# Load existing member data
with open("D:/projects/MIMI/群文件整理/extracted_members.json", "r", encoding="utf-8") as f:
    members = json.load(f)

by_name = {m["name"]: m for m in members}
used_ids = set()
max_id = max(m["id"] for m in members)

# Build ordered list: match each screenshot position to existing member record
ordered = []
unmatched = []

for i, sname in enumerate(screenshot_order):
    pos = i + 1

    # Try match_map first
    mapped = match_map.get(sname)
    if mapped and mapped in by_name:
        m = by_name[mapped]
        if m["id"] not in used_ids:
            m["screenshot_order"] = pos
            ordered.append(m)
            used_ids.add(m["id"])
            continue

    # Try exact match
    if sname in by_name:
        m = by_name[sname]
        if m["id"] not in used_ids:
            m["screenshot_order"] = pos
            ordered.append(m)
            used_ids.add(m["id"])
            continue

    # Try fuzzy match
    found = False
    clean_s = sname.replace(" ", "").lower()
    for name, m in by_name.items():
        if m["id"] in used_ids:
            continue
        clean_n = name.replace(" ", "").lower()
        if len(clean_s) >= 3 and len(clean_n) >= 3:
            if (clean_s[:4] == clean_n[:4] or
                (len(clean_s) >= 4 and clean_s in clean_n) or
                (len(clean_n) >= 4 and clean_n in clean_s)):
                m["screenshot_order"] = pos
                ordered.append(m)
                used_ids.add(m["id"])
                found = True
                break
    if found:
        continue

    # New member
    max_id += 1
    new_member = {
        "name": sname if sname != "Hao2" else "Hao",
        "bio": "", "background": "", "skills": [], "city": "",
        "tags": [], "id": max_id, "contact": "", "intro": "",
        "time": "2026-03-10", "ai_profile": "",
        "screenshot_order": pos
    }
    ordered.append(new_member)
    used_ids.add(max_id)
    unmatched.append(f"  #{pos} {sname}")

# Add members not in screenshot_order (new members added after initial 158)
new_additions = []
for m in members:
    if m.get("id") not in used_ids and "id" in m:
        m["screenshot_order"] = 999 + m.get("order", 0)
        new_additions.append(m)
        used_ids.add(m["id"])
    elif "id" not in m and m["name"] not in [o["name"] for o in ordered]:
        max_id += 1
        m["id"] = max_id
        m["screenshot_order"] = 999 + len(ordered)
        new_additions.append(m)

# Sort original 158: has_intro first (by screenshot_order), no_intro last (by screenshot_order)
has_intro = sorted([m for m in ordered if m.get("intro") and "尚未自我介绍" not in m.get("intro","")], key=lambda m: m["screenshot_order"])
no_intro = sorted([m for m in ordered if not m.get("intro") or "尚未自我介绍" in m.get("intro","")], key=lambda m: m["screenshot_order"])

# New members: keep exact order as given, no sorting
final = has_intro + no_intro + new_additions

# Set display order and clean up temp field
for i, m in enumerate(final):
    m["order"] = i + 1
    if "screenshot_order" in m:
        del m["screenshot_order"]

print(f"Total: {len(final)}")
print(f"With intro: {len(has_intro)}, Without intro: {len(no_intro)}")
if unmatched:
    print(f"Unmatched: {unmatched}")

print(f"\nFirst 10 (有简介, 群列表顺序):")
for m in final[:10]:
    print(f"  #{m['order']} {m['name']}")

print(f"\nLast 10 (无简介, 群列表顺序):")
for m in final[-10:]:
    print(f"  #{m['order']} {m['name']}")

# Save JSON
with open("D:/projects/MIMI/群文件整理/extracted_members.json", "w", encoding="utf-8") as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

# ============================================================
# Embed into HTML (using lambda to avoid \n interpretation!)
# ============================================================
compact = json.dumps(final, ensure_ascii=False, separators=(',', ':'))
assert '\n' not in compact

with open("D:/projects/MIMI/群文件整理/index (2).html", "r", encoding="utf-8") as f:
    html = f.read()

new_code = f"const DEFAULT_MEMBERS = {compact};"
html_new = re.sub(
    r"const DEFAULT_MEMBERS = \[.*?\];",
    lambda m: new_code,  # lambda prevents \n interpretation!
    html, count=1, flags=re.DOTALL
)

# Bump version
html_new = re.sub(
    r"const DATA_VERSION = '.*?'",
    "const DATA_VERSION = '2026-03-13-v37'",
    html_new, count=1
)

with open("D:/projects/MIMI/群文件整理/index (2).html", "w", encoding="utf-8") as f:
    f.write(html_new)

# Verify single-line
for line in html_new.split('\n'):
    if 'DEFAULT_MEMBERS' in line:
        print(f"\nHTML: DEFAULT_MEMBERS is single line, length={len(line)}")
        break

print("Done! v15")
