#!/usr/bin/env python3
"""
直接解析缓存中的 SoulChatCorpus JSON 文件。
绕过 modelscope/datasets 版本不兼容问题。
"""
import json
from collections import Counter

CACHE_FILE = r"C:\Users\HBDXcjj\.cache\modelscope\hub\datasets\downloads\34e7fec2c1acdf9ec4aaeab5c71ee603732e7e6b10bd93eb6b5e9bb728d58e0e"

print("Loading JSON (907MB, may take 10-30s)...")
with open(CACHE_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total dialogues: {len(data):,}")

# Topic distribution
topics = [d["topic"] for d in data]
topic_counts = Counter(topics)
print(f"\nTopic distribution ({len(topic_counts)} topics):")
for topic, count in topic_counts.most_common():
    pct = count / len(data) * 100
    print(f"  {topic}: {count:,} ({pct:.1f}%)")

# Turn statistics
turn_counts = [len(d["messages"]) for d in data]
avg_turns = sum(turn_counts) / len(turn_counts)
max_turns = max(turn_counts)
min_turns = min(turn_counts)
print(f"\nTurn statistics:")
print(f"  Average turns per dialogue: {avg_turns:.1f}")
print(f"  Min turns: {min_turns}")
print(f"  Max turns: {max_turns}")

# Total utterances
total_utterances = sum(turn_counts)
print(f"  Total utterances: {total_utterances:,}")

# Sample first dialogue from each topic
print("\n" + "="*60)
print("Sample dialogues (first from each topic):")
seen_topics = set()
for d in data:
    t = d["topic"]
    if t not in seen_topics:
        seen_topics.add(t)
        msgs = d["messages"]
        print(f"\n--- [{t}] (id={d['id']}, turns={len(msgs)}) ---")
        for i, m in enumerate(msgs[:4]):  # Show first 4 turns
            role = "U" if m["role"] == "user" else "A"
            content = m["content"][:80] + "..." if len(m["content"]) > 80 else m["content"]
            print(f"  {role}: {content}")
        if len(msgs) > 4:
            print(f"  ... ({len(msgs)-4} more turns)")

# Save topic distribution to markdown
with open("topic_distribution.md", "w", encoding="utf-8") as f:
    f.write("# SoulChatCorpus 主题分布\n\n")
    f.write(f"- 总对话数: {len(data):,}\n")
    f.write(f"- 总轮数: {total_utterances:,}\n")
    f.write(f"- 平均每对话轮数: {avg_turns:.1f}\n")
    f.write(f"- 主题数: {len(topic_counts)}\n\n")
    f.write("| 主题 | 数量 | 占比 |\n")
    f.write("|------|------|------|\n")
    for topic, count in topic_counts.most_common():
        pct = count / len(data) * 100
        f.write(f"| {topic} | {count:,} | {pct:.1f}% |\n")

print("\nSaved topic_distribution.md")
