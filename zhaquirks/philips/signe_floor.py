"""Hue Signe Fradient Floor Lamp device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster

(
    QuirkBuilder()
    .applies_to("Signify Netherlands B.V.", "4080248U9")
    .applies_to("Signify Netherlands B.V.", "915005987101")
    .applies_to("Signify Netherlands B.V.", "915005987201")
    .applies_to("Signify Netherlands B.V.", "915005987501")
    .applies_to("Signify Netherlands B.V.", "915005987601")
    .applies_to("Signify Netherlands B.V.", "915005987701")
    .applies_to("Signify Netherlands B.V.", "915005987801")
    .applies_to("Signify Netherlands B.V.", "929003479601")
    .applies_to("Signify Netherlands B.V.", "929003479701")
    .friendly_name(
        model="Hue Signe Gradient Floor Lamp",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
