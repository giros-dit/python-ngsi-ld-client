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
from ngsi_ld_client.models.list_contexts200_response1_one_of import ListContexts200Response1OneOf  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestListContexts200Response1OneOf(unittest.TestCase):
    """ListContexts200Response1OneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListContexts200Response1OneOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListContexts200Response1OneOf`
        """
        model = ngsi_ld_client.models.list_contexts200_response1_one_of.ListContexts200Response1OneOf()  # noqa: E501
        if include_optional :
            return ListContexts200Response1OneOf(
                context = None
            )
        else :
            return ListContexts200Response1OneOf(
                context = None,
        )
        """

    def testListContexts200Response1OneOf(self):
        """Test ListContexts200Response1OneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
