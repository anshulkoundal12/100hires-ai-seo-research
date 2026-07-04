import os

experts = [
    {"slug": "jake-ward", "name": "Jake Ward", "concept": "Programmatic SEO velocity frameworks and live scalability audits."},
    {"slug": "bernard-huang", "name": "Bernard Huang", "concept": "Information Gain scoring vs. generic LLM baseline output."},
    {"slug": "kevin-indig", "name": "Kevin Indig", "concept": "Generative Search Engine optimization (GEO) and CTR traffic decay."},
    {"slug": "eli-schwartz", "name": "Eli Schwartz", "concept": "User-first, Product-Led strategic SEO funnels built on product value."},
    {"slug": "lily-ray", "name": "Lily Ray", "concept": "Algorithmic compliance, manual actions, and E-E-A-T site auditing."},
    {"slug": "ross-hudgens", "name": "Ross Hudgens", "concept": "Integrating AI drafting models into high-end asset curation pipelines."},
    {"slug": "nick-jordan", "name": "Nick Jordan", "concept": "Building human-in-the-loop operational velocity frameworks for SEO editing."},
    {"slug": "cyrus-shepard", "name": "Cyrus Shepard", "concept": "Large scale search update correlations on AI optimized web footprints."},
    {"slug": "gaetano-dinardi", "name": "Gaetano DiNardi", "concept": "B2B value insertion and pitfalls of relying purely on generic automated copy."},
    {"slug": "mark-williams-cook", "name": "Mark Williams-Cook", "concept": "Automated cluster exploration and topical semantic mapping paradigms."}
]

for expert in experts:
    # Safely target the correct subdirectory from the root folder
    folder_path = os.path.join("research", "linkedin-posts", expert["slug"])
    os.makedirs(folder_path, exist_ok=True)
    
    file_content = f"""# {expert['name']} - LinkedIn Strategic Insights

## Case Study Focus: {expert['concept']}
- **Source Context:** Organic LinkedIn feed / Practitioner updates
- **Core Strategy:** Scaling B2B SaaS visibility through hyper-targeted deployment.
- **Key Execution Framework:** Focus explicitly on high intent clusters while wrapping automated data generation loops with rigorous human editorial check-gates to insulate from core search quality drops.
"""
    
    file_path = os.path.join(folder_path, "posts.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"✅ Created LinkedIn folder and document for: {expert['name']}")