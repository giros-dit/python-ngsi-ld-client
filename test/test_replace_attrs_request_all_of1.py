# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import ngsi_ld_client
from ngsi_ld_client.models.replace_attrs_request_all_of1 import ReplaceAttrsRequestAllOf1  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestReplaceAttrsRequestAllOf1(unittest.TestCase):
    """ReplaceAttrsRequestAllOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ReplaceAttrsRequestAllOf1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReplaceAttrsRequestAllOf1`
        """
        model = ngsi_ld_client.models.replace_attrs_request_all_of1.ReplaceAttrsRequestAllOf1()  # noqa: E501
        if include_optional :
            return ReplaceAttrsRequestAllOf1(
                context = None
            )
        else :
            return ReplaceAttrsRequestAllOf1(
                context = None,
        )
        """

    def testReplaceAttrsRequestAllOf1(self):
        """Test ReplaceAttrsRequestAllOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
