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
from ngsi_ld_client.api.c_source_registrations_api import CSourceRegistrationsApi  # noqa: E501


class TestCSourceRegistrationsApi(unittest.TestCase):
    """CSourceRegistrationsApi unit test stubs"""

    def setUp(self):
        self.api = CSourceRegistrationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_csources(self):
        """Test case for query_csources

        """
        pass

    def test_register_csource(self):
        """Test case for register_csource

        """
        pass

    def test_remove_csource(self):
        """Test case for remove_csource

        """
        pass

    def test_retrieve_csource(self):
        """Test case for retrieve_csource

        """
        pass


if __name__ == '__main__':
    unittest.main()
