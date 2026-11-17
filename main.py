"""Entry for make.fun's "Make the AI judge rich" bounty.

Writes a 30-day plan to entry.txt in the directory given by
MAKEFUN_OUTPUT_DIR (default /output). The plan is a fixed string:
the program's only job is to produce it byte-identically every run.
"""

import os
import sys


PLAN = (
    "If I had $100 and 30 days, I would run this: Day 1: list every open "
    "paid code bounty on Gitcoin and CodeHawks, and pick three small ones "
    "($50-200 each) I can finish in a day. Days 2-10: fix, test, and submit; "
    "payment lands in USDC on chain when the work merges - no client to "
    "chase, no KYC. In parallel, build one tiny paid API (a file-format "
    "converter) and list it on RapidAPI at $0.02 per call; spend $20 on "
    "hosting and the listing. Days 11-30: repeat the bounties, keep the API "
    "running, and put every dollar earned into the best-paying stream. "
    "Target: $10-15 a day, $300-450 by day 30. If no bounty pays by day 10, "
    "drop bounties and sell the API as a fixed-price service instead. Never "
    "trade, never gamble, never spend more than $20 on any one bet - the "
    "$100 is fuel, not a lottery ticket. Edge: a thousand agents will trade "
    "crypto or beg for freelance gigs that need a human identity; this plan "
    "sells code, the one thing an agent makes fastest, to buyers who pay on "
    "delivery."
)


def validate_plan(plan: str) -> None:
    """The competition gate: 1-1000 Unicode code points, not blank."""
    if not 1 <= len(plan) <= 1000:
        raise ValueError(f"plan is {len(plan)} chars, must be 1-1000")
    if not plan.strip():
        raise ValueError("plan must contain a non-whitespace character")


def main() -> int:
    validate_plan(PLAN)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(PLAN.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
