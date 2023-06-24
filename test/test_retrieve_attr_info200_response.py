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
from ngsi_ld_client.models.retrieve_attr_info200_response import RetrieveAttrInfo200Response  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestRetrieveAttrInfo200Response(unittest.TestCase):
    """RetrieveAttrInfo200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RetrieveAttrInfo200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveAttrInfo200Response`
        """
        model = ngsi_ld_client.models.retrieve_attr_info200_response.RetrieveAttrInfo200Response()  # noqa: E501
        if include_optional :
            return RetrieveAttrInfo200Response(
                id = '', 
                type = 'Attribute', 
                attribute_name = '', 
                attribute_count = 1.337, 
                attribute_types = [
                    ''
                    ], 
                type_names = [
                    ''
                    ], 
                context = None
            )
        else :
            return RetrieveAttrInfo200Response(
                id = '',
                type = 'Attribute',
                attribute_name = '',
                context = None,
        )
        """

    def testRetrieveAttrInfo200Response(self):
        """Test RetrieveAttrInfo200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
