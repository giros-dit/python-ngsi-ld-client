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
from ngsi_ld_client.models.update_csr_request import UpdateCSRRequest  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestUpdateCSRRequest(unittest.TestCase):
    """UpdateCSRRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateCSRRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCSRRequest`
        """
        model = ngsi_ld_client.models.update_csr_request.UpdateCSRRequest()  # noqa: E501
        if include_optional :
            return UpdateCSRRequest(
                id = '', 
                type = 'ContextSourceRegistration', 
                registration_name = '0', 
                description = '0', 
                information = [
                    ngsi_ld_client.models.registration_info.RegistrationInfo(
                        entities = [
                            ngsi_ld_client.models.entity_info.EntityInfo(
                                id = '', 
                                id_pattern = '', 
                                type = null, )
                            ], 
                        property_names = [
                            ''
                            ], 
                        relationship_names = [
                            ''
                            ], )
                    ], 
                tenant = '', 
                observation_interval = ngsi_ld_client.models.time_interval.TimeInterval(
                    start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                management_interval = ngsi_ld_client.models.time_interval.TimeInterval(
                    start_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                location = None, 
                observation_space = None, 
                operation_space = None, 
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                endpoint = '', 
                context_source_info = [
                    ngsi_ld_client.models.key_value_pair.KeyValuePair(
                        key = '', 
                        value = '', )
                    ], 
                scope = None, 
                mode = 'inclusive', 
                operations = [
                    ''
                    ], 
                refresh_rate = '', 
                management = ngsi_ld_client.models.registration_management_info.RegistrationManagementInfo(
                    local_only = True, 
                    cache_duration = '', 
                    timeout = 1, 
                    cooldown = 1, ), 
                context = None
            )
        else :
            return UpdateCSRRequest(
                context = None,
        )
        """

    def testUpdateCSRRequest(self):
        """Test UpdateCSRRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
