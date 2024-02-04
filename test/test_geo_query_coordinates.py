# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client.models.geo_query_coordinates import GeoQueryCoordinates

class TestGeoQueryCoordinates(unittest.TestCase):
    """GeoQueryCoordinates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoQueryCoordinates:
        """Test GeoQueryCoordinates
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoQueryCoordinates`
        """
        model = GeoQueryCoordinates()
        if include_optional:
            return GeoQueryCoordinates(
            )
        else:
            return GeoQueryCoordinates(
        )
        """

    def testGeoQueryCoordinates(self):
        """Test GeoQueryCoordinates"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
