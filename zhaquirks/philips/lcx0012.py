"""Signify LCX012 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster

(
    QuirkBuilder("Signify Netherlands B.V.", "LCX012")
    .friendly_name(
        model="Hue Festavia Gradient Light String 250 (1st-gen)",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
