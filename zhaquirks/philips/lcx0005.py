"""Signify LCX005 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster, SIGNIFY

(
    QuirkBuilder(SIGNIFY, "LCX005")
    .friendly_name(
        model="Hue Play Gradient Lightstrip for PC (24-27)",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
