# coding: utf-8

"""
    ietf-intefaces@2018-02-20.yang

    OpenAPI schema for the ietf-intefaces@2018-02-20.yang YANG module  supported by a model-based network device.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class LinkUpDownTrapEnableOptions(str, Enum):
    """
    Options for linkUp/linkDown SNMP notifications.
    """

    """
    allowed enum values
    """
    ENABLED = 'enabled'
    DISABLED = 'disabled'

    @classmethod
    def from_json(cls, json_str: str) -> LinkUpDownTrapEnableOptions:
        """Create an instance of LinkUpDownTrapEnableOptions from a JSON string"""
        return LinkUpDownTrapEnableOptions(json.loads(json_str))


