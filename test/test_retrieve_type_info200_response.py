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
from ngsi_ld_client.models.retrieve_type_info200_response import RetrieveTypeInfo200Response  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestRetrieveTypeInfo200Response(unittest.TestCase):
    """RetrieveTypeInfo200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RetrieveTypeInfo200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveTypeInfo200Response`
        """
        model = ngsi_ld_client.models.retrieve_type_info200_response.RetrieveTypeInfo200Response()  # noqa: E501
        if include_optional :
            return RetrieveTypeInfo200Response(
                id = '', 
                type = 'EntityTypeInfo', 
                type_name = '', 
                entity_count = 1.337, 
                attribute_details = [
                    ngsi_ld_client.models.attribute.Attribute(
                        id = '', 
                        type = 'Attribute', 
                        attribute_name = '', 
                        attribute_count = 1.337, 
                        attribute_types = [
                            ''
                            ], 
                        type_names = [
                            ''
                            ], )
                    ], 
                context = None
            )
        else :
            return RetrieveTypeInfo200Response(
                id = '',
                type = 'EntityTypeInfo',
                type_name = '',
                entity_count = 1.337,
                attribute_details = [
                    ngsi_ld_client.models.attribute.Attribute(
                        id = '', 
                        type = 'Attribute', 
                        attribute_name = '', 
                        attribute_count = 1.337, 
                        attribute_types = [
                            ''
                            ], 
                        type_names = [
                            ''
                            ], )
                    ],
                context = None,
        )
        """

    def testRetrieveTypeInfo200Response(self):
        """Test RetrieveTypeInfo200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
