"""Signify LCX006 device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips.gradient import PhilipsGradientCluster

(
    QuirkBuilder()
    .applies_to("Signify Netherlands B.V.", "915005986901")
    .applies_to("Signify Netherlands B.V.", "915005987001")
    .applies_to("Signify Netherlands B.V.", "915005987401")
    .applies_to("Signify Netherlands B.V.", "915005987301")
    .friendly_name(
        model="Hue Signe Gradient Table Lamp",
        manufacturer="Philips",
    )
    .replaces(PhilipsGradientCluster, endpoint_id=11)
    .add_to_registry()
)
