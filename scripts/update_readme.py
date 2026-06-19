from pathlib import Path

TOPICS = [
    "Arrays","Strings","Recursion","LinkedList","Stack",
    "Queue","HashMap","Trees","BST","Heap","Graph",
    "DynamicProgramming","Greedy","SlidingWindow","Backtracking"
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

        for f in java_files:
            recent.append(f"- {topic} / {f.stem}")

    topic_counts[topic] = count
    total += count


stats = f"""| Metric | Count |
|-------|------:|
| Total Problems | {total} |
"""

topics = "| Topic | Problems |\n|------|----------:|\n"
for t in TOPICS:
    topics += f"| {t} | {topic_counts[t]} |\n"

recent_text = "\n".join(recent[-5:]) if recent else "No problems solved yet."

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")

def replace_section(start, end, content):
    before = text.split(start)[0]
    after = text.split(end)[1]
    return before + start + "\n" + content + "\n" + end + after

text = replace_section("<!-- STATS_START -->", "<!-- STATS_END -->", stats)
text = replace_section("<!-- TOPICS_START -->", "<!-- TOPICS_END -->", topics)
text = replace_section("<!-- RECENT_START -->", "<!-- RECENT_END -->", recent_text)

readme.write_text(text, encoding="utf-8")

print("README updated successfully")
