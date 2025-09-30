# Saved Prompt: Anchor & Link New Vocabulary (Bird by bird.md)

Copy/paste this whole block into chat whenever you add NEW bold vocabulary items to `markdown_ver/READING/ARTICLES/Bird by bird.md` and want the automation done.

---
Task:
I have added new bold vocabulary (formatted like **word** or multi-word phrases) in `Bird by bird.md`.
Please:
1. Detect all newly bolded words/phrases in the Notes Section that are NOT yet hyperlinks (not already like `[**word**](#word)`).
2. Normalize anchor IDs:
   - Lowercase.
   - Replace spaces with hyphens.
   - Keep existing hyphens (e.g., tool-making).
   - Use singular for plural surface forms (logs→log, pots→pot, peasants→peasant, palms→palm, cords→cord). If unclear, choose the base form already used in earlier entries.
3. Assign sequential numbers continuing from the last existing numbered vocab entry (above the `---` divider).
4. Insert new entries (in order of FIRST appearance in the article body) immediately after the last existing entry, using:
   **<number>. <a id="anchor-id"></a>word** /IPA/
   (definition placeholder)
   Leave definition blank or just a dash if none provided. Do NOT alter existing earlier entries.
5. If an entry with the same anchor already exists, don’t duplicate—just link the occurrences.
6. In the Notes Section body, convert each plain bold occurrence into an internal link: `[**word**](#anchor-id)`.
   - Don’t re-wrap words already linked.
   - Map plurals to singular anchor (peasants→peasant, etc.).
   - Multi-word phrases (e.g., at will) should link as a single unit: `[**at will**](#at-will)`.
7. Do not modify tables or earlier explanatory vocabulary sections.
8. Light cleanup: Add a missing period only if a sentence ends just before an inserted link and lacks punctuation. No stylistic rewrites.
9. Report back:
   - Added entries (number + anchor + surface form).
   - Linked words (including plural→anchor mappings).
   - Any ambiguities or skipped bold items (and why).
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

Optional triggers:
- If I say "IPA" include IPA (single form unless explicitly two variants exist already).
- If I say "defs" add a concise definition line (POS tags optional).
- If I say "examples" add one short usage sentence per new entry.

End of prompt
---

## Quick Reference

Anchor entry pattern:
```
**19. <a id="briskly"></a>briskly** /ˈbrɪsk.li/
(definition here)
```
Body link pattern:
```
[**briskly**](#briskly)
```
Plural mapping examples: `logs → log`, `pots → pot`, `peasants → peasant`, `palms → palm`, `cords → cord`.

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
- v3: Added mandatory blank line rule before every additional sense line; clarified that sense lines are not list bullets; added regex helper to insert blank lines between consecutive sense lines; updated formatting normalization rule #10 accordingly.
- v2: Added formatting normalization step (#10) and regex helpers for spacing; clarified blank line rules and bullet hygiene.
- v1 (initial): Created canonical workflow instructions.

Feel free to extend this file with additional conventions (e.g., color-coding, tags) later.
