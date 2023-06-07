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
from ngsi_ld_client.models.interface_all_of import InterfaceAllOf  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestInterfaceAllOf(unittest.TestCase):
    """InterfaceAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InterfaceAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InterfaceAllOf`
        """
        model = ngsi_ld_client.models.interface_all_of.InterfaceAllOf()  # noqa: E501
        if include_optional :
            return InterfaceAllOf(
                name = ngsi_ld_client.models.name.Name(), 
                description = ngsi_ld_client.models.description.Description(), 
                enabled = ngsi_ld_client.models.enabled.Enabled(), 
                link_up_down_trap_enable = ngsi_ld_client.models.link_up_down_trap_enable.LinkUpDownTrapEnable(), 
                admin_status = ngsi_ld_client.models.admin_status.AdminStatus(), 
                oper_status = ngsi_ld_client.models.oper_status.OperStatus(), 
                last_change = ngsi_ld_client.models.last_change.LastChange(), 
                if_index = ngsi_ld_client.models.if_index.IfIndex(), 
                phys_address = ngsi_ld_client.models.phys_address.PhysAddress(), 
                speed = ngsi_ld_client.models.speed.Speed(), 
                higher_layer_if = ngsi_ld_client.models.higher_layer_if.HigherLayerIf(), 
                lower_layer_if = ngsi_ld_client.models.lower_layer_if.LowerLayerIf()
            )
        else :
            return InterfaceAllOf(
        )
        """

    def testInterfaceAllOf(self):
        """Test InterfaceAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
