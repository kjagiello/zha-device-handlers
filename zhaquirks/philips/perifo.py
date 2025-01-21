"""Hue Perifo device."""

from zigpy.quirks.v2 import QuirkBuilder

from zhaquirks.philips import SIGNIFY, PhilipsHueCluster

(
    QuirkBuilder()
    .applies_to(SIGNIFY, "929003116301")
    .applies_to(SIGNIFY, "929003116401")
    .applies_to(SIGNIFY, "929003116501")
    .applies_to(SIGNIFY, "929003116601")
    .friendly_name(
        model="Hue Perifo Light Tube",
        manufacturer="Philips",
    )
    .replaces(PhilipsHueCluster, endpoint_id=11)
    .add_to_registry()
)
