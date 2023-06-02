# coding: utf-8

"""
    ietf-intefaces@2018-02-20.yang

    OpenAPI schema for the ietf-intefaces@2018-02-20.yang YANG module  supported by a model-based network device.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import ngsi_ld_client
from ngsi_ld_client.models.geometry_line_string import GeometryLineString  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestGeometryLineString(unittest.TestCase):
    """GeometryLineString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GeometryLineString
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeometryLineString`
        """
        model = ngsi_ld_client.models.geometry_line_string.GeometryLineString()  # noqa: E501
        if include_optional :
            return GeometryLineString(
                type = 'LineString', 
                coordinates = ngsi_ld_client.models.geometry/line_string.Geometry.LineString(
                    type = 'LineString', )
            )
        else :
            return GeometryLineString(
        )
        """

    def testGeometryLineString(self):
        """Test GeometryLineString"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
