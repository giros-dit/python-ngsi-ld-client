# coding: utf-8

"""
    ETSI ISG CIM / NGSI-LD API

    This OAS file describes the NGSI-LD API defined by the ETSI ISG CIM group. This Cross-domain Context Information Management API allows to provide, consume and subscribe to context information in multiple scenarios and involving multiple stakeholders  # noqa: E501

    The version of the OpenAPI document: latest
    Contact: NGSI-LD@etsi.org
    Generated by: https://openapi-generator.tech
"""

import unittest

import ngsi_ld_client
from ngsi_ld_client.api.c_source_subscriptions_api import CSourceSubscriptionsApi  # noqa: E501


class TestCSourceSubscriptionsApi(unittest.TestCase):
    """CSourceSubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = CSourceSubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_c_source_subscription(self):
        """Test case for create_c_source_subscription

        """
        pass

    def test_remove_c_source_subscription(self):
        """Test case for remove_c_source_subscription

        """
        pass

    def test_retrieve_c_source_subscriptions(self):
        """Test case for retrieve_c_source_subscriptions

        """
        pass

    def test_retrieve_c_source_subscriptions_by_id(self):
        """Test case for retrieve_c_source_subscriptions_by_id

        """
        pass

    def test_update_c_source_subscription(self):
        """Test case for update_c_source_subscription

        """
        pass


if __name__ == '__main__':
    unittest.main()
