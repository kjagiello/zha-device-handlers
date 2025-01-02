"""Signify LCX016 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips.gradient import PhilipsGradientCluster

(
    QuirkBuilder("Signify Netherlands B.V.", "LCX016")
    .friendly_name(
        model="Hue Festavia Gradient Light String 100",
        manufacturer="Philips",
    )
    .replaces(PhilipsGradientCluster, endpoint_id=11)
    .add_to_registry()
)
