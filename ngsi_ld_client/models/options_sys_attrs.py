# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class OptionsSysAttrs(str, Enum):
    """
    6.3.11 Including system generated attributes.
    """

    """
    allowed enum values
    """
    SYSATTRS = 'sysAttrs'

    @classmethod
    def from_json(cls, json_str: str) -> OptionsSysAttrs:
        """Create an instance of OptionsSysAttrs from a JSON string"""
        return OptionsSysAttrs(json.loads(json_str))


