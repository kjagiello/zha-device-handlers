"""Hue Signe Fradient Table Lamp device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import SIGNIFY, PhilipsHueCluster

(
    QuirkBuilder()
    .applies_to(SIGNIFY, "915005986901")
    .applies_to(SIGNIFY, "915005987001")
    .applies_to(SIGNIFY, "915005987401")
    .applies_to(SIGNIFY, "915005987301")
    .friendly_name(
        model="Hue Signe Gradient Table Lamp",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
