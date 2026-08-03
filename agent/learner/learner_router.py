"""learner_router — personalized tool-dispatch hints (P2, stub for P0).

P2 adds: when a tool (e.g. paper-reader) is dispatched and the learner has a
high-confidence pattern for the user ("visualization > formula_first"), inject
a hint at the tool_executor dispatch layer — a deterministic behavioral
intervention, not a prompt-suggestion.

Kept as an importable stub; no-op for P0.
"""

from __future__ import annotations

from typing import Any, Optional


def hint_for_tool(agent: Any, tool_name: str, args: dict) -> Optional[str]:
    """Return a personalization hint for a tool dispatch, or None (P2)."""
    return None
