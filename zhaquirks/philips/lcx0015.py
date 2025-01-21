"""Signify LCX015 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster, SIGNIFY

(
    QuirkBuilder(SIGNIFY, "LCX015")
    .friendly_name(
        model="Hue Festavia Gradient Light String 250",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
