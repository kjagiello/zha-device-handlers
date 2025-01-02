"""Signify LCX003 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips.gradient import PhilipsGradientCluster

(
    QuirkBuilder("Signify Netherlands B.V.", "LCX003")
    .friendly_name(
        model="Hue Play Gradient Lightstrip 75",
        manufacturer="Philips",
    )
    .replaces(PhilipsGradientCluster, endpoint_id=11)
    .add_to_registry()
)
