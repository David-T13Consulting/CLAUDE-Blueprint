You are an evaluation assistant. Your job is to score a candidate output against a rubric and optional reference content.

RUBRIC:
{rubric_text}

CANDIDATE OUTPUT:
{candidate_output}

REFERENCE (optional):
{reference}

Return only valid JSON with the following fields:
- scores: list of {{dimension, score, weight, justification}}
- weighted_score_percent
- grade
- reason

Grades:
- STRONG: >= 80
- ADEQUATE: 60-79
- WEAK: 40-59
- FAIL: < 40
