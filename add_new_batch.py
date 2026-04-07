"""Add 20 new members (batch after Ethan Li) to extracted_members.json."""
import json
from pathlib import Path

PATH = Path("D:/projects/MIMI/群文件整理/extracted_members.json")

with PATH.open("r", encoding="utf-8") as f:
    members = json.load(f)

# Find max id and order
max_id = max(m.get("id", 0) for m in members)
max_order = max(m.get("order", 0) for m in members)
print(f"Current max id: {max_id}, max order: {max_order}, total: {len(members)}")

# New members in join order
new_members: list[dict] = []

def make_entry(
    name: str,
    invited_by: str,
    city: str = "",
    city_tag: str = "其它",
    ai_profile: str = "",
    tags: list[dict] | None = None,
) -> dict:
    if tags is None:
        tags = [{"category": "city", "label": city_tag}]
    return {
        "name": name,
        "intro": "尚未自我介绍" if not ai_profile else "",
        "bio": "",
        "background": "",
        "skills": [],
        "city": city,
        "tags": tags,
        "id": 0,  # filled below
        "contact": "",
        "ai_profile": ai_profile,
        "order": 0,  # filled below
        "invited_by": invited_by,
    }

# 1. 木铎姐姐 (刘凤芹) - no intro yet
new_members.append(make_entry(
    name="木铎姐姐 (刘凤芹)",
    invited_by="Patrick Liu",
))

# 2. 洪刚 - no intro yet
new_members.append(make_entry(
    name="洪刚",
    invited_by="Patrick Liu",
))

# 3. yq - no intro yet
new_members.append(make_entry(
    name="yq",
    invited_by="Patrick Liu",
))

# 4. 李成喆 - has intro (leecz, 北京)
new_members.append(make_entry(
    name="李成喆",
    invited_by="Patrick Liu",
    city="北京",
    ai_profile=(
        "**昵称**：leecz\n"
        "**坐标**：北京\n"
        "**背景**：20年企业数字化-农牧食品上市公司CIO/Cloud Gaming创业经历/EE背景/Wolfram enthusiast\n"
        "**擅长**：计算机体系架构/开放场景探索与问题分析\n"
        "**关注**：AI行业应用/自动化\n"
        "**一句话**：希望和各位朋友多沟通，互通有无，共同进步～"
    ),
    tags=[
        {"category": "city", "label": "北京"},
        {"category": "career", "label": "CIO"},
        {"category": "industry", "label": "企业数字化"},
        {"category": "industry", "label": "农牧食品"},
        {"category": "interest", "label": "AI行业应用"},
    ],
))

# 5. 施麒 - no intro yet
new_members.append(make_entry(
    name="施麒",
    invited_by="Patrick Liu",
))

# 6. 曹峰 - no intro yet
new_members.append(make_entry(
    name="曹峰",
    invited_by="Patrick Liu",
))

# 7. Mr.z - no intro yet
new_members.append(make_entry(
    name="Mr.z",
    invited_by="Patrick Liu",
))

# 8. ALLInCreateAmind.agi.top 张德祥 - no intro yet
new_members.append(make_entry(
    name="ALLInCreateAmind.agi.top 张德祥",
    invited_by="Patrick Liu",
))

# 9. 混沌有形 - has intro (深圳)
new_members.append(make_entry(
    name="混沌有形",
    invited_by="Patrick Liu",
    city="深圳",
    ai_profile=(
        "**昵称**：混沌有形\n"
        "**坐标**：深圳\n"
        "**背景**：二手房出租管理\n"
        "**擅长**：个人成长，知识管理\n"
        "**关注**：AI，Agent\n"
        "**一句话**：想和各位大佬学习AI方面的知识"
    ),
    tags=[
        {"category": "city", "label": "深圳"},
        {"category": "industry", "label": "房产"},
        {"category": "interest", "label": "知识管理"},
        {"category": "interest", "label": "AI Agent"},
    ],
))

# 10. Royce - has intro (深圳)
new_members.append(make_entry(
    name="Royce",
    invited_by="Patrick Liu",
    city="深圳",
    ai_profile=(
        "**昵称**：Royce\n"
        "**坐标**：深圳\n"
        "**背景**：金融/微众银行/国际发展部\n"
        "**擅长**：金融产品研究设计\n"
        "**关注**：AI agent\n"
        "**一句话**：向大家学习AI共存时期国际业务机会和落地场景"
    ),
    tags=[
        {"category": "city", "label": "深圳"},
        {"category": "industry", "label": "金融"},
        {"category": "company", "label": "微众银行"},
        {"category": "skill", "label": "金融产品设计"},
        {"category": "interest", "label": "AI Agent"},
    ],
))

# 11. 润海 (佳泽) - has intro (北京)
new_members.append(make_entry(
    name="润海",
    invited_by="Patrick Liu",
    city="北京",
    ai_profile=(
        "**昵称**：佳泽\n"
        "**坐标**：北京\n"
        "**背景**：医疗/精神营养学专家\n"
        "**擅长**：医疗机构+精准营养落地\n"
        "**关注**：AI Agent\n"
        "**一句话**：想与大佬们探讨AI Agent医疗/家庭应用落地场景及AI落地安全保障方案。"
    ),
    tags=[
        {"category": "city", "label": "北京"},
        {"category": "industry", "label": "医疗"},
        {"category": "skill", "label": "精神营养学"},
        {"category": "interest", "label": "AI Agent"},
    ],
))

# 12. Haeron X - has intro (上海)
new_members.append(make_entry(
    name="Haeron X",
    invited_by="Patrick Liu",
    city="上海",
    ai_profile=(
        "**昵称**：Haeron X\n"
        "**坐标**：上海\n"
        "**背景**：微软AI平台GPT，Claude，Image等Token和Agent市场业务负责人，OpenClaw Contributor\n"
        "**擅长**：Building, thinking and ship reality\n"
        "**关注**：the frontier of AI Agents\n"
        "**一句话**：Connect to AGI Builders, not talker"
    ),
    tags=[
        {"category": "city", "label": "上海"},
        {"category": "company", "label": "微软"},
        {"category": "career", "label": "业务负责人"},
        {"category": "skill", "label": "OpenClaw"},
        {"category": "interest", "label": "AI Agents"},
    ],
))

# 13. ♡ Kevin Xu - has intro (深圳)
new_members.append(make_entry(
    name="♡ Kevin Xu",
    invited_by="Patrick Liu",
    city="深圳",
    ai_profile=(
        "**昵称**：Kevin.Xu\n"
        "**坐标**：深圳\n"
        "**背景**：半导体/技术专家\n"
        "**擅长**：端侧AI Agent应用落地\n"
        "**关注**：AI Agent\n"
        "**一句话**：想与大佬们探讨AI Agent应用落地场景及AI落地安全保障方案。"
    ),
    tags=[
        {"category": "city", "label": "深圳"},
        {"category": "industry", "label": "半导体"},
        {"category": "skill", "label": "端侧AI"},
        {"category": "interest", "label": "AI Agent"},
    ],
))

# 14. Yewei - has intro (长沙)
new_members.append(make_entry(
    name="Yewei",
    invited_by="Patrick Liu",
    city="长沙",
    ai_profile=(
        "**昵称**：Yewei\n"
        "**坐标**：长沙\n"
        "**背景**：金融/通信/教育\n"
        "**擅长**：商品期货期权与金融衍生品研究\n"
        "**关注**：AI agent\n"
        "**一句话**：探讨AI发展动向与人的价值"
    ),
    tags=[
        {"category": "city", "label": "长沙"},
        {"category": "industry", "label": "金融"},
        {"category": "skill", "label": "期货衍生品"},
        {"category": "interest", "label": "AI Agent"},
    ],
))

# 15. hehe - has intro (北京)
new_members.append(make_entry(
    name="hehe",
    invited_by="Patrick Liu",
    city="北京",
    ai_profile=(
        "**昵称**：hehe\n"
        "**坐标**：北京\n"
        "**背景**：医疗/院内感染控制/教育\n"
        "**擅长**：全栈（垃圾代码整理）/院感/复杂性科学（一定了解）\n"
        "**关注**：AI agent\n"
        "**一句话**：之前做院内感染agent/目前在用agent做垃圾代码整理/对个体学习agent场景有兴趣。"
    ),
    tags=[
        {"category": "city", "label": "北京"},
        {"category": "industry", "label": "医疗"},
        {"category": "skill", "label": "全栈"},
        {"category": "interest", "label": "院内感染控制"},
        {"category": "interest", "label": "AI Agent"},
    ],
))

# 16-20: placeholder entries (Yuhao, 陈晨, 乱武, 果, Kayden)
for nm in ["Yuhao", "陈晨", "乱武", "果", "Kayden"]:
    new_members.append(make_entry(name=nm, invited_by="Patrick Liu"))

# Assign id / order
for i, m in enumerate(new_members, start=1):
    m["id"] = max_id + i
    m["order"] = max_order + i

members.extend(new_members)

with PATH.open("w", encoding="utf-8") as f:
    json.dump(members, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_members)} new members. Total now: {len(members)}")
print(f"New id range: {max_id+1}-{max_id+len(new_members)}")
print(f"New order range: {max_order+1}-{max_order+len(new_members)}")
