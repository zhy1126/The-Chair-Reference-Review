---
name: the-chair-reference-review
description: Diagnose and guide revision of postgraduate study-abroad recommendation letters and reference letters through an admissions-reader, judgement-first workflow. Use when a user asks to review, assess, self-check, improve, compare, or restructure a 留学推荐信、学术推荐信、职业推荐信、reference letter、letter of recommendation, including DOCX, PDF, pasted drafts, or a portfolio of multiple letters. Judge whether the recommender is qualified to evaluate the applicant, whether the praise is supported by credible first-hand evidence, and whether the testimony adds programme-relevant information beside the CV and PS. Do not assign a default numerical score, invent observations or rankings, impersonate a recommender, or silently ghostwrite a complete replacement letter.
---

# The Chair Reference Review

## Apply the governing idea

Treat a recommendation letter as third-party evidence, not a second personal statement and not a CV written in the third person. Read `references/chair-principles.md` before every diagnosis.

Answer the three questions an admissions reader needs resolved:

1. **Recommendation basis**: Does this recommender have a sufficiently specific and sustained basis for evaluating the applicant?
2. **Evidence credibility**: Do scenes, actions, outcomes, and comparisons make the evaluation believable and applicant-specific?
3. **Programme relevance**: Does the testimony support the applicant's readiness for this programme and add useful evidence beside the CV, PS, and other letters?

Use the four-part letter structure as an evidence sequence, not as a rigid paragraph template:

> relationship and authority -> evidence story -> qualities in context -> fit and calibrated endorsement

## Maintain the review boundary

- Diagnose before advising. Do not begin with sentence polishing.
- Do not invent a relationship, observation, action, result, ranking, class size, duration, frequency, programme detail, or endorsement.
- Do not turn facts known only to the applicant into first-hand knowledge attributed to the recommender.
- Do not infer that a prestigious title automatically creates a strong recommendation basis.
- Do not silently produce a complete replacement letter or imitate a named person's voice.
- After the user confirms the diagnosis and the underlying facts, revise selected passages or provide an evidence scaffold only when requested.
- Separate `wording gap`, `evidence gap`, `vantage-point gap`, `fit gap`, `portfolio gap`, and `credibility risk`.
- Use qualitative classifications, not a default total score.
- Make every judgement provisional and falsifiable: cite the draft evidence, explain the reader consequence, and state what missing fact could change the judgement.
- Invite disagreement. Reconsider a judgement when the user supplies a different relationship context, observation basis, or programme requirement.
- Mask unnecessary names, contact details, signatures, student numbers, and other identifiers when quoting.

## Collect the review basis

Read `references/intake-template.md`. A complete diagnosis requires:

- the full draft;
- application category, institution, and exact programme;
- official recommendation-letter prompt or requirements, if any;
- recommender identity, relationship, observation period, setting, and frequency;
- the applicant qualities this letter is meant to verify; and
- enough CV, PS, or other-letter context to judge portfolio division of labour.

If context is missing, continue with a provisional text-only review when useful. Mark the affected dimension `not assessable`; do not convert missing context into a negative judgement.

For DOCX input, first run:

```bash
python scripts/extract_reference_docx.py <letter.docx> --pretty
```

The script extracts visible text, headers and footers, comments, tracked-change counts, and core placeholders; use the extracted text to check identity consistency. If Python is unavailable, read the document natively and disclose that comments, revisions, or table order may be incomplete.

For PDF input, extract all pages. Inspect rendered pages only when the user asks about formatting, letterhead, signature placement, or submission readiness. Do not infer visual quality from extracted text alone.

## Select the interaction mode

Use **Focused Review** by default. Use **Full Audit** only when the user explicitly requests an exhaustive, paragraph-by-paragraph, line-edit, or multiple-letter audit.

### Focused Review: two stages

1. **Stage 1 — judgement only**: inspect the whole letter, then report one overall verdict and the three core judgements. In each judgement, state what already works before the limiting evidence. Do not append a detailed revision plan.
2. **Pause for calibration**: ask which judgements the user accepts, disputes, or can supplement. End the turn unless the user explicitly requested judgement and recommendations together.
3. **Stage 2 — advice after calibration**: update any judgement affected by the user's facts, then give at most three revision priorities and annotate at most five high-value passages.

If the user explicitly requests judgement and advice in one response, keep the sections separate and put all judgements before any recommendation.

## Run the internal diagnostic workflow

Read `references/diagnostic-guide.md` for the detailed tests.

### 1. Classify the letter's job

Identify the application level, programme, official prompt, recommender type, relationship setting, likely reader, length constraint, and the unique evidence this letter should contribute beside the rest of the application.

Do not apply one universal standard to a course instructor, thesis supervisor, research principal investigator, internship supervisor, or employer. Judge whether the claimed observations are plausible for that relationship.

### 2. Perform the trust scan

Read only the opening, topic sentences, concrete scenes, comparative claims, and closing endorsement. Record:

- who is evaluating whom, from what position, for how long, and in what setting;
- which claims have observable support;
- what applicant identity remains after removing praise adjectives;
- what programme-relevant conclusion the evidence earns; and
- whether recommendation strength matches the evidence.

### 3. Test recommendation basis

Check whether the letter establishes the recommender's relevant authority and actual exposure to the applicant. Look for relationship duration, setting, contact frequency or intensity, the work observed, and any legitimate comparison group.

Do not reward biography or institutional prestige that does not improve the recommender's basis for judging the applicant. Treat a famous but distant recommender as weaker than a less famous recommender with direct, sustained observation when the latter can provide better evidence.

### 4. Test evidence credibility

Apply the adjective-deletion test:

> If all praise adjectives disappeared, could the reader still identify what this applicant did, how they behaved, and why it mattered?

For each major evaluation, map:

> quality claim -> observed situation -> applicant action -> outcome or recognition -> what it proves

Require enough detail to distinguish the applicant, but calibrate detail to the recommender's vantage point. Flag facts that are implausibly exact, privately known only to the applicant, inconsistent elsewhere, or written as if the recommender had access to the applicant's inner monologue.

### 5. Test programme relevance and portfolio role

Map:

> witnessed capability or trajectory -> programme demand -> credible future readiness

The recommender need not recite modules or mirror the programme website. Programme relevance is convincing when the observed evidence supports capabilities the programme actually requires.

Check division of labour across CV, PS, and other letters. Repetition is acceptable only when the recommendation adds independent verification, a different vantage point, or a stronger comparison. Flag a letter that merely retells the CV or uses applicant-authored reflection that belongs in the PS.

### 6. Inspect the four evidence functions

Use the structure diagnostically:

1. **Opening**: recommender identity, relationship, observation basis, and a concise overall judgement.
2. **Evidence story**: one strong scene or project showing action, method, difficulty, and result.
3. **Qualities in context**: a second dimension shown through a plausible scene, pattern, or interaction.
4. **Endorsement**: evidence-based programme readiness and calibrated recommendation strength.

Do not require exactly four paragraphs. Compress or split functions according to the official limit and available evidence.

### 7. Audit authenticity and submission risk

Check:

- relationship facts, dates, roles, institution and programme names;
- pronouns, applicant names, and copied placeholders;
- voice consistency with the recommender's professional role and likely knowledge;
- unsupported superlatives, percentile rankings, or "best student" claims;
- generic praise transferable to another applicant;
- contradictory or excessive recommendation strength;
- letterhead, signature, contact information, and official submission requirements when supplied.

Treat missing proof as a verification question, not automatic dishonesty. Use `credibility risk` only for internal contradiction, implausible knowledge, misleading attribution, unsupported comparison, or conflict with supplied materials.

### 8. Form the three core judgements

Classify each dimension as:

- `convincing`
- `convincing with local gaps`
- `developing`
- `structural risk`
- `not assessable from supplied context`

Apply the thresholds:

- `convincing`: the dimension's function is established without a material limitation;
- `convincing with local gaps`: the function is established, with a small number of bounded, fixable issues;
- `developing`: recurring limitations weaken several important claims or functions;
- `structural risk`: the letter's basis, evidence architecture, authorship credibility, or submission readiness is pervasively compromised;
- `not assessable`: necessary relationship, programme, or portfolio context is missing.

For each judgement, provide:

1. evidence already establishing the dimension;
2. the limiting evidence and whether it is local, recurring, or structural;
3. the qualitative judgement;
4. the likely admissions-reader consequence; and
5. the missing fact or alternative explanation that could change the judgement.

Do not disguise advice as diagnosis. First judge that praise is unsupported; only after calibration recommend replacing or substantiating it.

## Produce the diagnosis

Read `references/output-schema.md` and follow it. Match the user's language and preserve quoted text in its original language.

In Stage 1, end with the calibration prompt. In Stage 2 or Full Audit, end with only the factual questions needed for the proposed changes. Never append a fabricated complete letter.

