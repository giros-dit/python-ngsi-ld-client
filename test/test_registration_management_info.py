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
from ngsi_ld_client.models.registration_management_info import RegistrationManagementInfo  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestRegistrationManagementInfo(unittest.TestCase):
    """RegistrationManagementInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegistrationManagementInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegistrationManagementInfo`
        """
        model = ngsi_ld_client.models.registration_management_info.RegistrationManagementInfo()  # noqa: E501
        if include_optional :
            return RegistrationManagementInfo(
                local_only = True, 
                cache_duration = '', 
                timeout = 1, 
                cooldown = 1
            )
        else :
            return RegistrationManagementInfo(
        )
        """

    def testRegistrationManagementInfo(self):
        """Test RegistrationManagementInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
