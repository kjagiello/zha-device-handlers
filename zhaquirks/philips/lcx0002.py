"""Signify LCX002 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips.gradient import PhilipsGradientCluster

(
    QuirkBuilder("Signify Netherlands B.V.", "LCX002")
    .friendly_name(
        model="Hue Play Gradient Lightstrip 65",
        manufacturer="Philips",
    )
    .replaces(PhilipsGradientCluster, endpoint_id=11)
    .add_to_registry()
)
