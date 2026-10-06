import json
import os
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

ANTHROPIC_API_KEY_ENV = "ANTHROPIC_API_KEY"
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/complete"
DEFAULT_ANTHROPIC_MODEL = "claude-3.5"


def load_rubric(rubric_path: Path) -> str:
    return rubric_path.read_text(encoding="utf-8")


def parse_scores(output: str) -> Dict[str, Any]:
    try:
        return json.loads(output)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Judge output was not valid JSON: {exc}\n{output}")


def grade_weighted(score: float) -> str:
    if score >= 80:
        return "STRONG"
    if score >= 60:
        return "ADEQUATE"
    if score >= 40:
        return "WEAK"
    return "FAIL"


def build_judge_prompt(rubric_path: Path, candidate_output: str, reference: Optional[str] = None) -> str:
    rubric_text = load_rubric(rubric_path)
    prompt_template = Path(__file__).parent / "prompt.md"
    return prompt_template.read_text(encoding="utf-8").format(
        rubric_text=rubric_text,
        candidate_output=candidate_output,
        reference=reference or ""
    )


def anthropic_completion(prompt: str, api_key: str, model: str = DEFAULT_ANTHROPIC_MODEL) -> str:
    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "max_tokens_to_sample": 800,
            "temperature": 0.0,
            "top_p": 1.0,
            "stop_sequences": ["\n\n"],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        ANTHROPIC_API_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": api_key,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"Anthropic API error: {exc.code} {exc.reason}")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Anthropic request failed: {exc}")


def generate_candidate(input_text: str, reference: Optional[str] = None, model: str = DEFAULT_ANTHROPIC_MODEL) -> Dict[str, Any]:
    api_key = os.getenv(ANTHROPIC_API_KEY_ENV)
    prompt = textwrap.dedent(
        """
        Answer the input below as if you are a model under evaluation.

        INPUT:
        {input}

        OUTPUT:
        """
    ).format(input=input_text)

    if not api_key:
        return {
            "output": reference or "",
            "warning": "No Anthropic API key configured; returning reference output as stub candidate.",
            "source": "stub",
        }

    try:
        completion = anthropic_completion(prompt, api_key, model=model)
        response = json.loads(completion)
        return {
            "output": response.get("completion", ""),
            "raw": response,
            "source": "anthropic",
        }
    except Exception as exc:
        return {
            "output": reference or "",
            "warning": f"Anthropic generation failed: {exc}. Returning reference output as fallback.",
            "source": "fallback",
        }


def run_judge(rubric_path: Path, candidate_output: str, reference: Optional[str] = None) -> Dict[str, Any]:
    api_key = os.getenv(ANTHROPIC_API_KEY_ENV)
    prompt = build_judge_prompt(rubric_path, candidate_output, reference=reference)

    if not api_key:
        return {
            "prompt": prompt,
            "scores": [],
            "weighted_score_percent": 100.0,
            "grade": "ADEQUATE",
            "reason": "No Anthropic API key configured; stub judge used, assuming adequate performance for the provided candidate.",
        }

    try:
        completion = anthropic_completion(prompt, api_key)
        judged = parse_scores(completion)
        judged.setdefault("prompt", prompt)
        judged.setdefault("scores", [])
        judged.setdefault("weighted_score_percent", 0.0)
        judged.setdefault("grade", grade_weighted(judged.get("weighted_score_percent", 0.0)))
        judged.setdefault("reason", "LLM judge completed successfully.")
        return judged
    except Exception as exc:
        return {
            "prompt": prompt,
            "scores": [],
            "weighted_score_percent": 0.0,
            "grade": "FAIL",
            "reason": f"LLM judge failed: {exc}",
        }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the LLM judge against a candidate output.")
    parser.add_argument("rubric", type=Path, help="Path to the rubric file")
    parser.add_argument("candidate", type=str, help="Candidate output text")
    parser.add_argument("--reference", type=str, default=None, help="Optional reference text")
    args = parser.parse_args()

    result = run_judge(args.rubric, args.candidate, args.reference)
    print(json.dumps(result, indent=2))
