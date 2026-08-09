import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract LD+JSON
match = re.search(r'<script type="application/ld\+json">\s*([\s\S]*?)\s*</script>', content)
if not match:
    print("ERROR: No JSON-LD script found in index.html")
    exit(1)

raw_json = match.group(1)
try:
    data = json.loads(raw_json)
    print("SUCCESS: JSON-LD parses cleanly with zero syntax errors!")
except json.JSONDecodeError as e:
    print(f"ERROR: JSON decoding failed: {e}")
    exit(1)

# Verify graph
graph = data.get("@graph", [])
ids = {node["@id"]: node for node in graph if "@id" in node}

print(f"Total graph nodes: {len(graph)}")
for node in graph:
    print(f" - [{node.get('@type')}]: {node.get('@id')}")

# Check person
person_id = "https://sankara25.github.io/sankarasubramanian.dev/#person"
assert person_id in ids, "Missing Person node"
person = ids[person_id]
assert "https://github.com/sankara25" in person.get("sameAs", []), "Missing GitHub sameAs"
assert "https://linkedin.com/in/sankara-subramanian" in person.get("sameAs", []), "Missing LinkedIn sameAs"
assert len(person.get("knowsAbout", [])) > 10, "knowsAbout is too sparse"
assert len(person.get("workExample", [])) == 6, "Expected 6 workExample project references"

# Verify all workExample IDs resolve to actual nodes in the graph
for we in person.get("workExample", []):
    proj_id = we["@id"]
    assert proj_id in ids, f"Dangling reference: {proj_id}"
    proj_node = ids[proj_id]
    print(f"   Verified project: {proj_node.get('name')} -> creator: {proj_node.get('creator', {}).get('@id')}")

print("\nALL SEO & SCHEMA VALIDATION CHECKS PASSED PERFECTLY!")
