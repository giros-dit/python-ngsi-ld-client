# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class OptionsNoOverwrite(str, Enum):
    """
    Indicates that no attribute overwrite shall be performed.
    """

    """
    allowed enum values
    """
    NOOVERWRITE = 'noOverwrite'

    @classmethod
    def from_json(cls, json_str: str) -> OptionsNoOverwrite:
        """Create an instance of OptionsNoOverwrite from a JSON string"""
        return OptionsNoOverwrite(json.loads(json_str))


