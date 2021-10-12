# Copyright 2021 Canonical Ltd.
# See LICENSE file for licensing details.

"""Helper functions for writing tests."""

import logging

log = logging.getLogger(__name__)


async def get_unit_address(ops_test, app_name: str, unit_num: int) -> str:
    """Get private address of a unit."""
    status = await ops_test.model.get_status()  # noqa: F821
    return status["applications"][app_name]["units"][f"{app_name}/{unit_num}"]["address"]
