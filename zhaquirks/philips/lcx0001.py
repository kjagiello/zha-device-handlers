"""Signify LCX001 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster, SIGNIFY

(
    QuirkBuilder(SIGNIFY, "LCX001")
    .friendly_name(
        model="Hue Play Gradient Lightstrip 55",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
