---
name: the-chair-reference-review
description: Diagnose and guide revision of undergraduate and postgraduate study-abroad recommendation letters, reference letters, referee forms, and scholarship references through an admissions-reader, judgement-first workflow. Use when a user asks to review, assess, self-check, compare, or improve a 留学推荐信、学术推荐信、职业推荐信、reference letter、letter of recommendation, including DOCX, PDF, pasted drafts, structured referee responses, or a portfolio of multiple letters. Judge formal recommender eligibility and observation basis, evidence credibility and applicant distinctiveness, programme relevance, and contribution beside the CV, PS, and other references. Do not assign a default numerical score, invent observations or rankings, convert applicant-supplied facts into recommender testimony, impersonate a recommender, or silently ghostwrite a complete replacement letter.
---

# The Chair Reference Review

## Apply the governing idea

Treat a recommendation as third-party evidence, not a second personal statement or a CV written in the third person. Read `references/chair-principles.md` before forming the first judgement in a task.

Use three core lenses:

1. **Recommendation basis**: Is the recommender formally acceptable, sufficiently independent, and positioned to observe the applicant?
2. **Evidence credibility**: Do first-hand observations, records, patterns, comparisons, or examples support an applicant-specific judgement?
3. **Application contribution**: Does the testimony support relevant readiness and add useful evidence beside the CV, PS, and other references?

Treat the official prompt, referee form, eligibility rules, submission instructions, and credible local genre conventions as controlling. Use the three lenses as defaults, not as an exhaustive universal model. For a reusable letter, judge field- or programme-family relevance rather than demanding school-specific praise.

## Maintain the review boundary

- Diagnose before advising. Do not begin with sentence polishing.
- Do not invent a relationship, observation, result, comparison, ranking, programme detail, or endorsement.
- Separate three kinds of confirmation:
  1. the applicant can confirm that a fact is accurate;
  2. the recommender can confirm that they observed or had access to it;
  3. the recommender alone can confirm that the interpretation and endorsement are theirs.
- Do not turn applicant-supplied facts into first-person recommender testimony without recommender verification and assent.
- Do not infer that prestige creates either formal eligibility or a strong observation basis.
- Do not silently produce a complete replacement letter or imitate a named person's voice.
- After calibration, revise selected passages only when requested and only from confirmed evidence. Use placeholders for facts still awaiting recommender confirmation.
- Use qualitative classifications, not a default total score.
- Make each judgement provisional and falsifiable: cite the evidence, explain the reader consequence, and state which fact could change it.
- Ask the user to correct facts or assumptions, not merely to accept the judgement.
- Assign each defect a primary dimension. Cross-reference it elsewhere without lowering multiple dimensions unless it causes a distinct reader consequence in each.
- If nothing meaningful works in a dimension, say so; do not manufacture a positive finding to satisfy the output order.
- Mask unnecessary names, contact details, signatures, student numbers, and other identifiers when quoting.

## Route supporting resources

- Read `references/intake-template.md` only when inputs are incomplete, the user asks what to provide, or a programme-specific/portfolio diagnosis is requested.
- Read the relevant sections of `references/diagnostic-guide.md` while testing recommender basis, evidence form, programme contribution, genre conventions, or submission risk. Read the whole file for a Full Audit.
- Read `references/output-schema.md` before producing Stage 1, Stage 2, combined, or Full Audit output.

For DOCX input, resolve the bundled script from this skill's installed directory, not from the user's current working directory:

```bash
python "<skill-directory>/scripts/extract_reference_docx.py" <letter.docx> --pretty
```

The optional extractor requires Python 3.8+. It reports visible text, headers and footers, comments, tracked-change counts, Latin-word count, CJK-character count, non-whitespace character count, and common English/Chinese placeholders. If the runtime is unavailable, read the document natively and disclose the extraction limits.

For PDF input, extract all pages. Render pages when layout, letterhead, signature, contact information, or submission readiness is in scope; never infer visual quality from text extraction alone.

## Select the interaction state

### Focused Stage 1 — default

Report judgement only: review basis, one-sentence verdict, likely reader takeaway, and the three core lenses. Under the third lens, classify **programme relevance** and **portfolio contribution** separately so one may remain assessable when the other is not. End with a factual calibration request. Do not provide revision verbs, sample replacements, or content to insert.

### Focused Stage 2

Use only after the user corrects, confirms, or supplements the factual basis. Update the affected judgements, then give at most three revision priorities and at most five high-value annotations. Identify whether each missing fact requires applicant confirmation, recommender verification, recommender assent, or an official source.

### Combined response

Use only when the user explicitly requests judgement and recommendations together. Present all judgements first, then a clearly separated Stage 2 plan. Do not fill missing evidence by inference.

### Full Audit

Use when the user explicitly requests an exhaustive paragraph audit, submission audit, or multiple-letter portfolio audit. Provide the three judgements first, then cover every paragraph or response field and all material risks. Summarize recurring sentence-level problems and quote up to eight representative high-value passages; do not claim to provide a line edit unless every material line was actually inspected.

Full Audit remains diagnostic by default and pauses before sample rewrites. If the user also explicitly requests a repair plan, add it after the audit in a separate section, subject to the same evidence rules.

## Run the diagnostic workflow

1. **Classify the job.** Identify application level, programme or field, official prompt, referee type, required eligibility, relationship setting, likely reader, submission form, length limit, and the intended role beside other materials.
2. **Perform the trust scan.** Read the opening or form context, topic sentences, evidence-bearing passages, comparative claims, reservations, and closing strength. Record what the recommender can credibly know and what image remains after deleting praise adjectives.
3. **Test recommendation basis.** Judge formal eligibility and independence separately from relationship depth and observation access. Mark either component `not assessable` when its governing rules or facts are missing.
4. **Test evidence credibility.** Accept multiple evidence forms: a specific episode, longitudinal pattern, assessed work, documented record, legitimate comparison, repeated interaction, or evaluative synthesis grounded in observation. Do not force every good letter into a story.
5. **Test application contribution.** Assess programme or field relevance independently from portfolio contribution. Repetition is useful only when it adds independent verification, a new vantage point, or a meaningful comparison.
6. **Audit authenticity and tone.** Calibrate precision, hedging, restraint, enthusiasm, reservations, omissions, and recommendation strength to the recommender's role, evidence, official prompt, and credible genre context. Do not interpret culturally restrained language as faint praise without adequate context.
7. **Audit submission risk.** Check names, pronouns, institution and programme, placeholders, conflicts, letterhead, signature, contact details, and official submission rules when supplied.
8. **Form classifications.** Use only `convincing`, `convincing with local gaps`, `developing`, `structural risk`, or `not assessable`. Apply local, recurring, and structural severity consistently.

Use the canonical issue types defined in `references/diagnostic-guide.md`. Treat missing proof as a verification question, not dishonesty; reserve `credibility risk` for contradiction, misleading attribution, implausible access, unsupported comparison, or conflict with supplied materials.

## Produce the diagnosis

Follow `references/output-schema.md`. Match the user's language and preserve quoted text in its original language. In Stage 1, state only the factual condition that could change a judgement; do not disguise advice as a boundary. Never append a fabricated complete letter.

