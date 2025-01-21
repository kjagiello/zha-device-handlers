"""Signify LCX003 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import SIGNIFY, PhilipsHueCluster

(
    QuirkBuilder(SIGNIFY, "LCX003")
    .friendly_name(
        model="Hue Play Gradient Lightstrip 75",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
