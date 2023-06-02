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
from ngsi_ld_client.models.in_broadcast_pkts import InBroadcastPkts  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestInBroadcastPkts(unittest.TestCase):
    """InBroadcastPkts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InBroadcastPkts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InBroadcastPkts`
        """
        model = ngsi_ld_client.models.in_broadcast_pkts.InBroadcastPkts()  # noqa: E501
        if include_optional :
            return InBroadcastPkts(
                type = 'Property', 
                value = 56, 
                observed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                unit_code = '', 
                dataset_id = ''
            )
        else :
            return InBroadcastPkts(
                type = 'Property',
                value = 56,
        )
        """

    def testInBroadcastPkts(self):
        """Test InBroadcastPkts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
