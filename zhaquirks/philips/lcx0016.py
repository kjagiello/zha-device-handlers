"""Signify LCX016 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster, SIGNIFY

(
    QuirkBuilder(SIGNIFY, "LCX016")
    .friendly_name(
        model="Hue Festavia Gradient Light String 100",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
