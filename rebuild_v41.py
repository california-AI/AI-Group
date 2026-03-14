import json, re

# ============================================================
# 205 members from sorted screenshots (folder 6/排序)
# Exact order as shown in WeChat group member list
# ============================================================
screenshot_order = [
    "Patrick Liu",       # 1
    "颜嵘",              # 2
    "黄铠",              # 3
    "亚当 Adam",         # 4
    "Henry",             # 5
    "Richard",           # 6
    "何宇滔",            # 7  (was 何宇涵)
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
    "南川 Mark",         # 31
    "Tianrun Yang",      # 32
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
    "B2B GTM",           # 53
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
    "Robin",             # 64
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
    "赵寰宇",            # 81  (was 赵富宇Arthur)
    "王文峰",            # 82
    "袁来Steve",         # 83  (was 朱来Steve)
    "陳禹",              # 84  NEW (陈杰退群, 陳禹新人)
    "Allyly",            # 85
    "张蓓-Shanda Growth",# 86  (was 张蕾)
    "贾明华",            # 87  (was 黄明华, already fixed)
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
    "孔蓉Karin",         # 110 (was 孔慕Karin)
    "Lijing Ying",       # 111
    "于伟",              # 112
    "frank",             # 113
    "琼慧啊",            # 114 NEW (琉璃厨退群, 琼慧啊新人)
    "Philip",            # 115
    "郑光辉",            # 116
    "张健",              # 117
    "姜兆恒",            # 118 (was 崇光恒)
    "Yonghui",           # 119
    "郑有成",            # 120 (was 邝有成)
    "李榜主",            # 121
    "蚂蚁战投",          # 122
    "Kelly Peng",        # 123
    "Harrison 姜浩楠",   # 124
    "张靖鹏",            # 125 (was 张镇勰)
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
    "Hao2",              # 142 (沈奕辰 changed name to Hao)
    "Niki Li",           # 143
    "Gil",               # 144
    "yc",                # 145
    "erickfang",         # 146
    "Lilyann",           # 147
    "Vance Chen",        # 148
    "迟小羽",            # 149
    "白强",              # 150 (was 白猫)
    "Zoe兆希",           # 151
    "Jun",               # 152
    "ZK",                # 153
    "jiezhu",            # 154
    "cursor何",          # 155
    "sean",              # 156
    "董挺宇",            # 157 NEW
    "Sarah Pu",          # 158
    "陈建文James",       # 159
    "Albert",            # 160
    "张帆",              # 161
    "杨磊",              # 162
    "WpxRichard",        # 163
    "Jack",              # 164
    "林秋楠Dylan",       # 165
    "A GritPeriod",      # 166
    "Shuyu",             # 167
    "张小圈",            # 168
    "Hongyi Liu",        # 169 NEW
    "Ron",               # 170 NEW
    "Mike H",            # 171 NEW
    "Victor",            # 172 NEW
    "曾昱Dennis",        # 173 (was Dennis Min Zeng)
    "Phil",              # 174 NEW
    "Red",               # 175 NEW
    "Young",             # 176
    "Adrian Liu",        # 177
    "小小",              # 178 NEW
    "Louis",             # 179 NEW
    "Frank Sui",         # 180 NEW
    "Nightwish",         # 181
    "Sandy",             # 182 NEW
    "Chenyu Zhang",      # 183 NEW
    "刘铁锋",            # 184 NEW
    "Hongyu",            # 185
    "jangitpoon",        # 186
    "Shuang Wang",       # 187 NEW
    "H.",                # 188 NEW
    "楷瑞",              # 189 NEW
    "Jason",             # 190 NEW
    "刘旌",              # 191 NEW
    "Jeremy",            # 192 NEW
    "小酒窝",            # 193 NEW
    "赵韬博-Jacob",      # 194 NEW
    "Lisa",              # 195 NEW
    "J",                 # 196 NEW
    "reegan",            # 197 NEW
    "aix",               # 198 NEW
    "David Shao",        # 199 NEW
    "李嘉",              # 200 NEW
    "侯正鹏",            # 201 NEW
    "Leo Fang",          # 202 NEW
    "Shirley",           # 203 NEW
    "GZ",                # 204 NEW
    "Der wulfeit Nicht", # 205 (already added with intro)
]

assert len(screenshot_order) == 205, f"Expected 205, got {len(screenshot_order)}"

# Screenshot name -> existing member record name
match_map = {
    "Patrick Liu": "Patrick Liu (刘勇)",
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
    "Hao2": "沈奕辰",
    "Robin": "Robin 齐彦博",
    "B2B GTM": "B2B 域名",
    "南川 Mark": "南川 WhyMark",
    "袁来Steve": "朱来 Steve",
    "何宇滔": "何宇涵",
    "赵寰宇": "赵富宇Arthur",
    "张蓓-Shanda Growth": "张蕾-Shanda Growth",
    "白强": "白猫",
    "姜兆恒": "崇光恒",
    "郑有成": "邝有成",
    "张靖鹏": "张镇勰",
    "孔蓉Karin": "孔慕Karin",
    "July to Angel": "July to Angel",
    "WpxRichard": "Richard (WpxRichard)",
    "陈建文James": "陈建文James",
    "林秋楠Dylan": "林秋楠Dylan",
    "张小圈": "Chris张小圈",
    "曾昱Dennis": "Dennis（Min Zeng）",
    "Nightwish": "Nightwish（李岩）",
    "Hongyu": "Hongyu（泓宇）",
    "jangitpoon": "jangitpoon（潘振杰）",
    "Adrian Liu": "Adrian Liu（柳奇）",
}

# Name corrections: after matching, rename these members
name_corrections = {
    "何宇涵": "何宇滔",
    "赵富宇Arthur": "赵寰宇 Arthur Zhao",
    "朱来 Steve": "袁来 Steve",
    "张蕾-Shanda Growth": "张蓓-Shanda Growth",
    "Robin 齐彦博": "Robin 乔彦博",
    "白猫": "白强",
    "崇光恒": "姜兆恒",
    "邝有成": "郑有成",
    "张镇勰": "张靖鹏",
    "孔慕Karin": "孔蓉 Karin",
    "Dennis（Min Zeng）": "曾昱 Dennis",
    "B2B 域名": "B2B GTM 秦赢之光",
    "南川 WhyMark": "南川 Mark@lovstudio.ai",
    "沈奕辰": "Hao",  # changed display name
    "Chris张小圈": "张小圈-C-cr7",
}

# Load existing member data
with open("D:/projects/MIMI/群文件整理/extracted_members.json", "r", encoding="utf-8") as f:
    members = json.load(f)

by_name = {m["name"]: m for m in members}
used_ids = set()
max_id = max(m["id"] for m in members)

# Build ordered list
ordered = []
unmatched = []

for i, sname in enumerate(screenshot_order):
    pos = i + 1

    # Try match_map first
    mapped = match_map.get(sname, sname)

    if mapped in by_name and by_name[mapped]["id"] not in used_ids:
        m = by_name[mapped]
        m["order"] = pos
        ordered.append(m)
        used_ids.add(m["id"])
        continue

    # Try exact match with screenshot name
    if sname in by_name and by_name[sname]["id"] not in used_ids:
        m = by_name[sname]
        m["order"] = pos
        ordered.append(m)
        used_ids.add(m["id"])
        continue

    # No fuzzy matching - only exact + match_map to avoid wrong matches
    # New member - create placeholder
    max_id += 1
    new_member = {
        "name": sname if sname != "Hao2" else "Hao",
        "intro": "",
        "bio": "", "background": "", "skills": [], "city": "",
        "tags": [{"category": "city", "label": "其它"}],
        "id": max_id, "contact": "", "ai_profile": "",
        "order": pos
    }
    ordered.append(new_member)
    used_ids.add(max_id)
    unmatched.append(f"  #{pos} {sname}")

# Apply name corrections
for m in ordered:
    old = m["name"]
    if old in name_corrections:
        m["name"] = name_corrections[old]

# Report
print(f"Total: {len(ordered)}")
print(f"Unmatched (new members): {len(unmatched)}")
for u in unmatched:
    print(u)

# Check for members that were in old data but not in new order (left group)
dropped = []
for m in members:
    if m["id"] not in used_ids:
        dropped.append(f"  {m['name']} (order={m.get('order')})")
print(f"\nDropped (left group): {len(dropped)}")
for d in dropped:
    print(d)

# Count stats
has_intro = sum(1 for m in ordered if m.get("intro") and "尚未自我介绍" not in m.get("intro", ""))
no_intro = len(ordered) - has_intro
print(f"\nWith intro: {has_intro}, Without intro: {no_intro}")
print(f"\nFirst 10:")
for m in ordered[:10]:
    intro_flag = "✓" if m.get("intro") and "尚未自我介绍" not in m.get("intro", "") else "✗"
    print(f"  #{m['order']} {m['name']} [{intro_flag}]")
print(f"\nLast 10:")
for m in ordered[-10:]:
    intro_flag = "✓" if m.get("intro") and "尚未自我介绍" not in m.get("intro", "") else "✗"
    print(f"  #{m['order']} {m['name']} [{intro_flag}]")

# Save JSON
with open("D:/projects/MIMI/群文件整理/extracted_members.json", "w", encoding="utf-8") as f:
    json.dump(ordered, f, ensure_ascii=False, indent=2)

# ============================================================
# Embed into HTML
# ============================================================
compact = json.dumps(ordered, ensure_ascii=False, separators=(',', ':'))
assert '\n' not in compact

with open("D:/projects/MIMI/群文件整理/index (2).html", "r", encoding="utf-8") as f:
    html = f.read()

new_code = f"const DEFAULT_MEMBERS = {compact};"
html_new = re.sub(
    r"const DEFAULT_MEMBERS = \[.*?\];",
    lambda m: new_code,
    html, count=1, flags=re.DOTALL
)

# Bump version
html_new = re.sub(
    r"const DATA_VERSION = '.*?'",
    "const DATA_VERSION = '2026-03-14-v41'",
    html_new, count=1
)

with open("D:/projects/MIMI/群文件整理/index (2).html", "w", encoding="utf-8") as f:
    f.write(html_new)

# Verify single-line
for line in html_new.split('\n'):
    if 'DEFAULT_MEMBERS' in line:
        print(f"\nHTML: DEFAULT_MEMBERS is single line, length={len(line)}")
        break

print("Done! v41")
