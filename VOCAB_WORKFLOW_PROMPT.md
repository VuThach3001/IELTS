# Saved Prompt: Anchor & Link New Vocabulary (Bird by bird.md)

Copy/paste this whole block into chat whenever you add NEW bold vocabulary items to `markdown_ver/READING/ARTICLES/Bird by bird.md` and want the automation done.

---
Task (AUTO-EXECUTION MODE v5):
I have added new bold vocabulary (formatted like **word** or multi-word phrases) in `Bird by bird.md`.
You must automatically perform ALL steps below in one pass with no clarifying questions unless a blocking ambiguity (e.g., anchor collision with different lemma) arises. Assume default behavior: add full enriched entries (Definition, Structures, Collocations, Examples, Notes) — not just placeholders. Proceed immediately.
Please:
1. Detect all newly bolded words/phrases in the Notes Section that are NOT yet hyperlinks (not already like `[**word**](#word)`).
2. Normalize anchor IDs:
   - Lowercase.
   - Replace spaces with hyphens.
   - Keep existing hyphens (e.g., tool-making).
   - Use singular for plural surface forms (logs→log, pots→pot, peasants→peasant, palms→palm, cords→cord). If unclear, choose the base form already used in earlier entries.
3. Assign sequential numbers continuing from the last existing numbered vocab entry (above the `---` divider).
4. Insert new entries (in order of FIRST appearance in the article body) immediately after the last existing entry, using the pattern:
   **<number>. <a id="anchor-id"></a>word** /IPA/
   Then immediately include a first sense/definition line (no blank line before it) followed by (when reasonably inferable) the full block set in this order (each preceded by exactly one blank line):
   **Structures** (list) → **Collocations** (list) → **Examples** (list 2–4 concise sentences) → **Notes** (paragraph). If information is genuinely unavailable, still include the heading with a single bullet `- TBD` (or a short neutral placeholder). Do NOT alter existing earlier entries.
5. If an entry with the same anchor already exists, don’t duplicate—just link the occurrences.
6. In the Notes Section body, convert each plain bold occurrence into an internal link: `[**word**](#anchor-id)`.
   - Don’t re-wrap words already linked.
   - Map plurals to singular anchor (peasants→peasant, etc.).
   - Multi-word phrases (e.g., at will) should link as a single unit: `[**at will**](#at-will)`.
7. Do not modify tables or earlier explanatory vocabulary sections.
8. Light cleanup: Add a missing period only if a sentence ends just before an inserted link and lacks punctuation. No stylistic rewrites.
9. Report back (concise summary after edits):
   - Added entries (number + anchor + surface form)
   - Linked words (including plural→anchor mappings)
   - Any ambiguities/skipped items (and why) — only if any
10. Formatting normalization (apply to BOTH newly added and existing entries if touched):

   - Ensure exactly ONE blank line precedes each section heading block label: **Grammar & Usage**, **Structures**, **Structures (Noun)**, **Structures (Verb)**, **Collocations**, **Collocations / Typical Pairings**, **Examples**, **Notes**, **Existing Phrases**.
   - No blank line needed directly after the headword line if a sense/definition line follows immediately; but there MUST be a blank line before the first block heading label after any grouped sense lines.
   - Remove solitary placeholder dashes (`-` on a line by itself) left from earlier spacing hacks.
   - Standardize bullet indentation: a single hyphen + space (no leading spaces, no double hyphens unless nested lists are intentional—avoid nesting unless necessary).
   - Remove accidental leading space bullets (strip preceding spaces so ` - Item` becomes `- Item`).
   - Keep intra-block bullets contiguous with no extra blank lines inside a block list; maintain exactly one blank line separating different blocks.
   - Preserve inline anchor HTML in headword lines; do NOT convert to markdown headings.
   - Do not alter existing numbering or anchor IDs.
   - Sense lines (additional forms) spacing rule (v3): After the headword line, the FIRST sense line may follow immediately. Insert EXACTLY ONE blank line before every subsequent sense line beginning with `**(n)` `**(v)` `**(adj)` `**(adv)` `**(phr)` etc. (Example: headword + first sense (no blank), then blank line, next sense line, blank line, next sense line …). Do not add a bullet dash before sense lines; they are plain paragraph lines (remove any leading `- ` that was previously used). If a block heading (e.g., **Structures**) directly follows a sense line, ensure there is exactly one blank line before that heading as per the general block rule.
   - Trailing spaces at end of lines should be removed.

11. Back link rule (navigation):
   - Each vocabulary entry MUST contain a single `[↩ back](#article)` link inline at the END of its first definition/sense line (or at the end of the headword line if that line already contains the first definition).
   - If you detect any legacy standalone line whose entire content is exactly `[↩ back](#article)` (or that line appears immediately under the headword line before the first sense), remove that standalone line and relocate the link inline to the correct first sense/definition line as described above.
   - Do NOT add more than one back link per entry.
   - Preserve existing spacing rules: no extra blank line created by removing the standalone link; ensure the headword line and first sense still follow the “no blank line” rule.
   - If the first sense begins on the line after the headword (typical pattern), append the back link to that first sense line; do NOT modify the headword line unless it itself houses the definition.
   - When auto-adding a brand new entry, include the back link immediately while writing the first sense line.

Optional triggers (override defaults):
- Saying "minimal" will suppress enrichment (use just definition line; skip Structures/Collocations/Examples/Notes).
- Saying "no-examples" omits Examples blocks.
- Saying "skeleton" restores v3 behavior (definition placeholder only).
- Otherwise (default) always enrich fully (IPA + sense + Structures + Collocations + Examples + Notes).

Automatic inclusions (default):
- Always include IPA (single form) if can be sourced or reliably inferred.
- Always include at least one definition line and attempt additional senses if clearly present in text context.
- Provide 2–4 examples; prefer one example adapted from article usage if present, rephrased minimally to avoid duplication.
- Provide concise, neutral Notes (usage, register, pitfalls, variants, synonyms/antonyms when clarifying).

End of prompt
---

## Quick Reference

Anchor entry pattern (with inline back link):
```
**19. <a id="briskly"></a>briskly** /ˈbrɪsk.li/
**(adv):** quickly; energetically; with purpose [↩ back](#article)
(subsequent senses / blocks follow with standard blank-line rules)
```
Body link pattern:
```
[**briskly**](#briskly)
```
Plural mapping examples: `logs → log`, `pots → pot`, `peasants → peasant`, `palms → palm`, `cords → cord`.

Back link placement summary:
1. Exactly one per entry.
2. Inline at end of first definition/sense line (or head line if head holds definition).
3. Remove and relocate any legacy standalone `[↩ back](#article)` lines.
4. Never place the back link inside bullet lists or later sense lines.

## VS Code Regex Helpers (Manual Use)
Find bold not already a link:
```regex
(?<!\[)\*\*(?!\d+\. )(?![^*]*\]\()([A-Za-z][A-Za-z-]*(?:\s+[A-Za-z-]+)?)\*\*
```
(This avoids matches inside existing `[** **](#id)` links.)

Insert a blank line before a block heading (run with "Use Regular Expression" ON). Test carefully:
Find:
```regex
(?<!\n)\n(\*\*(?:Grammar & Usage|Structures(?: \(Noun\)| \(Verb\))?|Collocations(?: \/ Typical Pairings)?|Examples|Notes|Existing Phrases)\*\*)
```
Replace with:
```
\n\n$1
```

Remove stray single dash lines used as spacers:
Find:
```regex
^-[ \t]*$\n?
```
Replace with nothing.

Fix leading space before bullet:
Find:
```regex
^ +- 
```
Replace with:
```
- 
```

Ensure blank line before each additional sense line (adds a blank line before sense labels that are immediately after another sense without an intervening blank line; run iteratively if needed):
Find:
```regex
(?<=\*\*\([a-zA-Z]+\)[^\n]*\n)(\*\*\([a-zA-Z]+\))
```
Replace with:
```
\n$1
```
NOTE: This regex assumes sense lines start with patterns like `**(n)` `**(v)` etc. Adjust character class if you introduce new POS tags.

## Future Automation Idea (Script Outline)
1. Read file.
2. Parse existing anchors -> map anchor->number.
3. Scan Notes Section body after `---` for `**...**` tokens not inside `[ ](`.
4. Normalize forms; collect new ones preserving first-seen order.
5. Append new entries with incremented numbering.
6. Rewrite body occurrences with link syntax.
7. Write file + summary log.

## Change Log
- v5: Added mandatory inline back link navigation rule (no standalone back link lines); updated entry pattern example to include inline `[↩ back](#article)`; added step 11 and guidance for migrating legacy placement.
- v4: Auto-execution mode (no confirmation needed); default full enrichment (Structures, Collocations, Examples, Notes) for all new entries; placeholder dashes replaced by structured blocks; added override triggers (minimal, no-examples, skeleton); clarified reporting format.
- v3: Added mandatory blank line rule before every additional sense line; clarified that sense lines are not list bullets; added regex helper to insert blank lines between consecutive sense lines; updated formatting normalization rule #10 accordingly.
- v2: Added formatting normalization step (#10) and regex helpers for spacing; clarified blank line rules and bullet hygiene.
- v1 (initial): Created canonical workflow instructions.

Feel free to extend this file with additional conventions (e.g., color-coding, tags) later.
