import re
import os

# Mapping for POS abbreviations
POS_MAP = {
    "adj": "adjective",
    "n": "noun",
    "v": "verb",
    "adv": "adverb",
    "prep": "preposition",
    "conj": "conjunction",
    "pron": "pronoun",
    "det": "determiner",
    "interj": "interjection"
}

# Step 1: Ask user for the markdown file path
md_path = input("Enter the path of your markdown file: ").strip()

# Step 2: Read markdown file
with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Step 3: Extract vocab entries (word + pos + definition)
entries = []
# Pattern: **1. Word** /ipa/ (adj) ... : definition
pattern = re.compile(r"\*\*\d+\.\s*([^*]+)\*\*.*?\(([^)]+)\).*?:\s*([^\n]+)")
for match in pattern.finditer(text):
    word = match.group(1).strip()
    pos_abbr = match.group(2).strip().lower()
    definition = match.group(3).strip()

    # Expand part of speech if in dictionary
    pos_full = POS_MAP.get(pos_abbr, pos_abbr)

    entries.append((word, pos_full, definition))

# Step 4: Prepare HTML (print word + POS in list)
js_entries = [f'"{w}, {p}. {d}"' for w, p, d in entries]

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Vocabulary TTS</title>
</head>
<body>
  <h1>Vocabulary List</h1>

  <button onclick="playAll()" style="font-size:18px; padding:10px; margin-top:20px;">🔊 Play All Words</button>

  <script>
    function playAll() {{
      const entries = [{", ".join(js_entries)}];

      let index = 0;
      function speakNext() {{
        if (index < entries.length) {{
          const utterance = new SpeechSynthesisUtterance(entries[index]);
          utterance.lang = "en-US";
          utterance.onend = () => {{
            index++;
            speakNext();
          }};
          speechSynthesis.speak(utterance);
        }}
      }}

      speakNext();
    }}
  </script>
  
  <pre style="font-size:16px; line-height:1.5em; font-weight:bold;">
{chr(10).join(f"- {w} ({p})" for w, p, d in entries)}
  </pre>

</body>
</html>
"""

# Step 5: Write HTML file in same folder as markdown
output_path = os.path.splitext(md_path)[0] + ".html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"✅ Done! HTML file saved as: {output_path}")
