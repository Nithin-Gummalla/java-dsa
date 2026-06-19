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
recent = []

for topic in TOPICS:
    folder = Path(topic)
    count = 0

    if folder.exists():
        java_files = list(folder.glob("*.java"))
        count = len(java_files)

        for file in java_files:
            recent.append(f"- {topic} / {file.stem}")

    topic_counts[topic] = count
    total += count

# STATS
stats = f"""| Metric | Count |
|-------|------:|
| Total Problems | {total} |
"""

# TOPICS
topics = "| Topic | Problems |\n|------|----------:|\n"
for topic in TOPICS:
    topics += f"| {topic} | {topic_counts[topic]} |\n"

# RECENT
recent_text = "\n".join(recent[-5:]) if recent else "No problems solved yet."

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

text = text.replace(
    "<!-- RECENT_START -->\nLoading...\n<!-- RECENT_END -->",
    f"<!-- RECENT_START -->\n{recent_text}\n<!-- RECENT_END -->"
)

readme.write_text(text, encoding="utf-8")

print("README updated successfully!")
