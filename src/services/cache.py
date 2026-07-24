"""Cache helpers for invoice generation and reminders."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def cache_step_0(records: list[dict], limit: int = 39) -> list[dict]:
    """Apply cache rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_1(records: list[dict], limit: int = 244) -> list[dict]:
    """Apply cache rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_2(records: list[dict], limit: int = 356) -> list[dict]:
    """Apply cache rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_3(records: list[dict], limit: int = 74) -> list[dict]:
    """Apply cache rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_4(records: list[dict], limit: int = 454) -> list[dict]:
    """Apply cache rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_5(records: list[dict], limit: int = 20) -> list[dict]:
    """Apply cache rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_6(records: list[dict], limit: int = 464) -> list[dict]:
    """Apply cache rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_7(records: list[dict], limit: int = 240) -> list[dict]:
    """Apply cache rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def cache_step_8(records: list[dict], limit: int = 443) -> list[dict]:
    """Apply cache rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("cache step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
