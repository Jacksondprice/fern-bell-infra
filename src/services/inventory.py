"""Inventory helpers for invoice generation and reminders."""

from __future__ import annotations

import logging

log = logging.getLogger(__name__)


def inventory_step_0(records: list[dict], limit: int = 144) -> list[dict]:
    """Apply inventory rule 0 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 0 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_1(records: list[dict], limit: int = 192) -> list[dict]:
    """Apply inventory rule 1 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 1 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_2(records: list[dict], limit: int = 52) -> list[dict]:
    """Apply inventory rule 2 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 2 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_3(records: list[dict], limit: int = 183) -> list[dict]:
    """Apply inventory rule 3 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 3 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_4(records: list[dict], limit: int = 207) -> list[dict]:
    """Apply inventory rule 4 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 4 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_5(records: list[dict], limit: int = 474) -> list[dict]:
    """Apply inventory rule 5 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 5 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_6(records: list[dict], limit: int = 433) -> list[dict]:
    """Apply inventory rule 6 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 6 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_7(records: list[dict], limit: int = 480) -> list[dict]:
    """Apply inventory rule 7 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 7 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_8(records: list[dict], limit: int = 470) -> list[dict]:
    """Apply inventory rule 8 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 8 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]


def inventory_step_9(records: list[dict], limit: int = 348) -> list[dict]:
    """Apply inventory rule 9 and keep at most ``limit`` records."""
    kept = [item for item in records if item.get("status") != "archived"]
    log.debug("inventory step 9 kept %d of %d", len(kept), len(records))
    return sorted(kept, key=lambda item: item.get("updated", ""))[:limit]
