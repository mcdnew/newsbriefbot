def generate_brief(summaries, format="markdown"):
    brief = ""
    for item in summaries:
        brief += f"### {item['title']}\n\n{item['summary']}\n\n---\n\n"
    return brief

