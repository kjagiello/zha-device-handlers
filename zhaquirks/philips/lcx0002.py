"""Signify LCX002 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import SIGNIFY, PhilipsHueCluster

(
    QuirkBuilder(SIGNIFY, "LCX002")
    .friendly_name(
        model="Hue Play Gradient Lightstrip 65",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
