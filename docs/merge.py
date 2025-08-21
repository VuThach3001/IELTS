import os
import re
import json

folder = "E:/Project/IELTS/docs"

all_words = []
all_html_blocks = []
all_entries = []

for filename in os.listdir(folder):
    if filename.endswith(".html") and filename.lower() != "index.html":
        path = os.path.join(folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

            # Extract vocab block inside <pre>...</pre>
            if "<pre" in content:
                block = content.split("<pre")[1].split("</pre>")[0]
                html_block = "<pre" + block + "</pre>"
                all_html_blocks.append(html_block)

            # Extract const entries = [...]
            match = re.search(r"const\s+entries\s*=\s*\[(.*?)\];", content, re.S)
            if match:
                js_block = match.group(1)
                # Extract all quoted strings
                entries = re.findall(r"'([^']*)'|\"([^\"]*)\"", js_block)
                entries = [e1 or e2 for e1, e2 in entries if (e1 or e2)]
                all_entries.extend(entries)
                    

# Build merged index.html
index_html = f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Vocabulary Index</title>
</head>
<body>
  <button onclick="playAll()">▶ Play All</button>
  
  <script>
    function playAll() {{
      const entries = {json.dumps(all_entries, ensure_ascii=False, indent=2)};

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
  <h1>All Vocabulary</h1>
  {"".join(all_html_blocks)}

</body>
</html>
"""

output_path = os.path.join(folder, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"✅ index.html created at {output_path}")
