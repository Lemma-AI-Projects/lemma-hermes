"""learner_scheduler — spaced-repetition scheduling (P2, stub for P0).

P0 ships the storage + SM-2 primitives inside LearnerCore (get_due_reviews /
reschedule_review / enqueue_review). This module will add, in P2:
  * cron job registration for due-review reminders (default off)
  * todo-tool integration (schedule reviews as tasks)

Kept as an importable stub so the wiring surface exists from day one.
"""

from __future__ import annotations

from agent.learner.learner_core import LearnerCore


class ReviewScheduler:
    """Placeholder — P2 milestone."""

    def __init__(self, core: LearnerCore) -> None:
        self._core = core

    def due_today(self, user_id: str) -> list:
        return self._core.get_due_reviews(user_id, limit=50)
