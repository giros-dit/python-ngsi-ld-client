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
from ngsi_ld_client.models.notification import Notification  # noqa: E501
from ngsi_ld_client.rest import ApiException

class TestNotification(unittest.TestCase):
    """Notification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Notification
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Notification`
        """
        model = ngsi_ld_client.models.notification.Notification()  # noqa: E501
        if include_optional :
            return Notification(
                id = '', 
                type = 'Notification', 
                subscription_id = '', 
                notified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                data = None
            )
        else :
            return Notification(
                id = '',
                type = 'Notification',
                subscription_id = '',
                notified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data = None,
        )
        """

    def testNotification(self):
        """Test Notification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()