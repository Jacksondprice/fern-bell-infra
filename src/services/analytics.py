"""Analytics helpers for invoice generation and reminders."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def analytics_step_0(records: list[dict], limit: int = 288) -> list[dict]:
    """Apply analytics rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_1(records: list[dict], limit: int = 142) -> list[dict]:
    """Apply analytics rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_2(records: list[dict], limit: int = 135) -> list[dict]:
    """Apply analytics rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_3(records: list[dict], limit: int = 50) -> list[dict]:
    """Apply analytics rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_4(records: list[dict], limit: int = 242) -> list[dict]:
    """Apply analytics rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_5(records: list[dict], limit: int = 150) -> list[dict]:
    """Apply analytics rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_6(records: list[dict], limit: int = 153) -> list[dict]:
    """Apply analytics rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_7(records: list[dict], limit: int = 400) -> list[dict]:
    """Apply analytics rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_8(records: list[dict], limit: int = 402) -> list[dict]:
    """Apply analytics rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_9(records: list[dict], limit: int = 31) -> list[dict]:
    """Apply analytics rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def analytics_step_10(records: list[dict], limit: int = 422) -> list[dict]:
    """Apply analytics rule 10 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("analytics step 10 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
