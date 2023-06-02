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
from ngsi_ld_client.models.phys_address_all_of import PhysAddressAllOf  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestPhysAddressAllOf(unittest.TestCase):
    """PhysAddressAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PhysAddressAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PhysAddressAllOf`
        """
        model = ngsi_ld_client.models.phys_address_all_of.PhysAddressAllOf()  # noqa: E501
        if include_optional :
            return PhysAddressAllOf(
                value = '2E:B0:20:84:29:30:cc:01:FF:CC:fe:Ee:15:0A:C3:2D:cA:Ec:8a:83:DD:D7:dB:F7:56:7C:88:19:5f:fc:ea:31:C1'
            )
        else :
            return PhysAddressAllOf(
                value = '2E:B0:20:84:29:30:cc:01:FF:CC:fe:Ee:15:0A:C3:2D:cA:Ec:8a:83:DD:D7:dB:F7:56:7C:88:19:5f:fc:ea:31:C1',
        )
        """

    def testPhysAddressAllOf(self):
        """Test PhysAddressAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
