 from pathlib import Path

TOPICS = [
    "Arrays",
    "Strings",
    "Recursion",
    "LinkedList",
    "Stack",
    "Queue",
    "HashMap",
    "Trees",
    "BST",
    "Heap",
    "Graph",
    "DynamicProgramming",
    "Greedy",
    "SlidingWindow",
    "Backtracking",
]

topic_counts = {}
total = 0

for topic in TOPICS:
    folder = Path(topic)

    count = 0

    if folder.exists():
        count = sum(1 for item in folder.iterdir() if item.is_dir())

    topic_counts[topic] = count
    total += count

stats = f"""| Metric | Count |
|-------|------:|
| Total Problems | {total} |
"""

topics = "| Topic | Problems |\n|------|----------:|\n"

for topic in TOPICS:
    topics += f"| {topic} | {topic_counts[topic]} |\n"

readme = Path("README.md")

text = readme.read_text(encoding="utf-8")

text = text.replace(
    "<!-- STATS_START -->\nLoading...\n<!-- STATS_END -->",
    f"<!-- STATS_START -->\n{stats}\n<!-- STATS_END -->"
)

text = text.replace(
    "<!-- TOPICS_START -->\nLoading...\n<!-- TOPICS_END -->",
    f"<!-- TOPICS_START -->\n{topics}\n<!-- TOPICS_END -->"
)

readme.write_text(text, encoding="utf-8")

print("README updated successfully!")
