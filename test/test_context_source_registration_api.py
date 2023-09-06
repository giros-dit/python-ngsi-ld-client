# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import ngsi_ld_client
from ngsi_ld_client.api.context_source_registration_api import ContextSourceRegistrationApi  # noqa: E501
from ngsi_ld_client.rest import ApiException


class TestContextSourceRegistrationApi(unittest.TestCase):
    """ContextSourceRegistrationApi unit test stubs"""

    def setUp(self):
        self.api = ngsi_ld_client.api.context_source_registration_api.ContextSourceRegistrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_csr(self):
        """Test case for create_csr

        Csource registration creation  # noqa: E501
        """
        pass

    def test_delete_csr(self):
        """Test case for delete_csr

        Csource registration deletion by id  # noqa: E501
        """
        pass

    def test_delete_csr_subscription(self):
        """Test case for delete_csr_subscription

        Csource registration subscription deletion by id   # noqa: E501
        """
        pass

    def test_update_csr(self):
        """Test case for update_csr

        Csource registration update by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
