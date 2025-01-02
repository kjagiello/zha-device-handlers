"""Signify LCX005 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips.gradient import PhilipsGradientCluster

(
    QuirkBuilder("Signify Netherlands B.V.", "LCX005")
    .friendly_name(
        model="Hue Play Gradient Lightstrip for PC (24-27)",
        manufacturer="Philips",
    )
    .replaces(PhilipsGradientCluster, endpoint_id=11)
    .add_to_registry()
)
