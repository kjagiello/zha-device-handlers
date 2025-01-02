"""Common utilities for gradient-compatible devices."""

from typing import Final

from zigpy import types
from zigpy.quirks import CustomCluster
from zigpy.zcl.foundation import (
    BaseAttributeDefs,
    DataTypeId,
    Direction,
    ZCLAttributeDef,
    ZCLCommandDef,
)


class PhilipsGradientCluster(CustomCluster):
    """Philips manufacturer cluster for the gradient."""

    cluster_id: Final[types.uint16_t] = 0xFC03
    ep_attribute: Final[str] = "philips_gradient_cluster"
    name: Final[str] = "PhilipsGradientCluster"

    server_commands = {
        0x0000: ZCLCommandDef(
            name="multicolor",
            schema={"data": types.SerializableBytes},
            direction=Direction.Client_to_Server,
            is_manufacturer_specific=True,
        )
    }

    class AttributeDefs(BaseAttributeDefs):
        """Manufacturer specific attributes."""

        state = ZCLAttributeDef(
            id=0x0002,
            type=types.LongOctetString,
            zcl_type=DataTypeId.octstr,
            access="r",
            is_manufacturer_specific=True,
        )
