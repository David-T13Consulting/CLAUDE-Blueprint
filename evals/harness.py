#!/usr/bin/env python3
import argparse
import json
import textwrap
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
GOLDEN_DATASET_PATH = DATA_DIR / "golden_dataset.json"
REDTEAM_PATH = ROOT / "redteam" / "cases.json"


@dataclass
class EvalCase:
    id: str
    input: str
    expected_output: str
    category: str
    tags: List[str] = field(default_factory=list)
    notes: Optional[str] = None


@dataclass
class EvalResult:
    case_id: str
    passed: bool
    actual_output: str
    expected_output: str
    category: str
    tags: List[str]
    score: float
    verdict: str
    details: Optional[str] = None


class EvalHarness:
    def __init__(self, judge: str = "exact"):
        self.judge = judge
        self.cases = self.load_golden_dataset()

    def load_golden_dataset(self) -> List[EvalCase]:
        if not GOLDEN_DATASET_PATH.exists():
            raise FileNotFoundError(f"Golden dataset not found: {GOLDEN_DATASET_PATH}")

        payload = json.loads(GOLDEN_DATASET_PATH.read_text(encoding="utf-8"))
        cases = []
        for item in payload:
            cases.append(
                EvalCase(
                    id=item["id"],
                    input=item["input"],
                    expected_output=item["expected_output"],
                    category=item.get("category", "uncategorized"),
                    tags=item.get("tags", []),
                    notes=item.get("notes"),
                )
            )
        return cases

    def run(self) -> Dict[str, Any]:
        results = []
        for case in self.cases:
            actual_output = self.generate_answer(case)
            result = self.score_case(case, actual_output)
            results.append(result)

        summary = self.summarize(results)
        return {"results": [asdict(r) for r in results], "summary": summary}

    def generate_answer(self, case: EvalCase) -> str:
        if self.judge == "exact":
            return case.expected_output
        if self.judge == "llm":
            return self.llm_answer(case)
        raise ValueError(f"Unsupported judge: {self.judge}")

    def llm_answer(self, case: EvalCase) -> str:
        try:
            from judge.scorer import generate_candidate
        except ImportError:
            raise RuntimeError("Could not import judge runner. Ensure evals/judge/scorer.py is importable.")

        result = generate_candidate(
            input_text=case.input,
            reference=case.expected_output,
        )
        return result.get("output", "")

    def score_case(self, case: EvalCase, actual_output: str) -> EvalResult:
        if self.judge == "exact":
            passed = self.normalize(actual_output) == self.normalize(case.expected_output)
            score = 1.0 if passed else 0.0
            verdict = "pass" if passed else "fail"
            details = None
            return EvalResult(
                case_id=case.id,
                passed=passed,
                actual_output=actual_output,
                expected_output=case.expected_output,
                category=case.category,
                tags=case.tags,
                score=score,
                verdict=verdict,
                details=details,
            )

        try:
            from judge.scorer import run_judge
        except ImportError:
            raise RuntimeError("Could not import judge runner. Ensure evals/judge/scorer.py is importable.")

        rubric_path = ROOT / "../.claude/evals/rubrics/research.md"
        if not rubric_path.exists():
            raise FileNotFoundError(f"Rubric file not found: {rubric_path}")

        judge_report = run_judge(rubric_path, actual_output, reference=case.expected_output)
        weighted = float(judge_report.get("weighted_score_percent", 0.0))
        grade = judge_report.get("grade", "FAIL")
        passed = grade != "FAIL"
        score = round(weighted / 100.0, 3)
        verdict = grade.lower()
        details = json.dumps(judge_report, indent=2)

        return EvalResult(
            case_id=case.id,
            passed=passed,
            actual_output=actual_output,
            expected_output=case.expected_output,
            category=case.category,
            tags=case.tags,
            score=score,
            verdict=verdict,
            details=details,
        )

    @staticmethod
    def normalize(text: str) -> str:
        return " ".join(text.strip().split())

    def summarize(self, results: List[EvalResult]) -> Dict[str, Any]:
        total = len(results)
        passed = sum(1 for result in results if result.passed)
        fail_count = total - passed
        categories = {}
        for result in results:
            categories.setdefault(result.category, {"total": 0, "passed": 0})
            categories[result.category]["total"] += 1
            if result.passed:
                categories[result.category]["passed"] += 1
        return {
            "total_cases": total,
            "passed": passed,
            "failed": fail_count,
            "pass_rate": round((passed / total) * 100, 2) if total else 0.0,
            "judge": self.judge,
            "categories": categories,
        }

    @staticmethod
    def validate_redteam() -> Dict[str, Any]:
        if not REDTEAM_PATH.exists():
            raise FileNotFoundError(f"Red-team definition not found: {REDTEAM_PATH}")
        payload = json.loads(REDTEAM_PATH.read_text(encoding="utf-8"))
        for item in payload:
            if not item.get("id") or not item.get("input") or not item.get("threat"):
                raise ValueError(f"Invalid red-team case: {item}")
        return {"case_count": len(payload), "valid": True}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the CLAUDE blueprint eval harness.")
    parser.add_argument("--run", action="store_true", help="Run the golden dataset cases.")
    parser.add_argument("--judge", choices=["exact", "llm"], default="exact", help="Scoring mode.")
    parser.add_argument("--list", action="store_true", help="List golden dataset cases.")
    parser.add_argument("--validate-redteam", action="store_true", help="Validate red-team case schema.")
    parser.add_argument("--output", type=str, help="Write the run summary to a JSON file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.list:
        harness = EvalHarness(judge=args.judge)
        for case in harness.cases:
            print(f"{case.id}: {case.category} — {case.input[:80]}...")
        return 0

    if args.validate_redteam:
        report = EvalHarness.validate_redteam()
        print(json.dumps(report, indent=2))
        return 0

    if not args.run:
        print("Nothing to do. Use --run, --list, or --validate-redteam.")
        return 1

    harness = EvalHarness(judge=args.judge)
    report = harness.run()
    output_text = json.dumps(report, indent=2)
    print(output_text)
    if args.output:
        Path(args.output).write_text(output_text, encoding="utf-8")
        print(f"Wrote summary to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
