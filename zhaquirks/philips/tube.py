"""Hue Play Gradient Light Tube device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import PhilipsHueCluster

(
    QuirkBuilder()
    .applies_to("Signify Netherlands B.V.", "915005987901")
    .applies_to("Signify Netherlands B.V.", "915005988001")
    .applies_to("Signify Netherlands B.V.", "915005988101")
    .applies_to("Signify Netherlands B.V.", "915005988201")
    .applies_to("Signify Netherlands B.V.", "915005988401")
    .applies_to("Signify Netherlands B.V.", "915005988501")
    .friendly_name(
        model="Hue Play Gradient Light Tube",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
