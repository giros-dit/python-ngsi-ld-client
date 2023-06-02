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
from ngsi_ld_client.api.temporal_context_information_consumption_api import TemporalContextInformationConsumptionApi  # noqa: E501
from ngsi_ld_client.rest import ApiException


class TestTemporalContextInformationConsumptionApi(unittest.TestCase):
    """TemporalContextInformationConsumptionApi unit test stubs"""

    def setUp(self):
        self.api = ngsi_ld_client.api.temporal_context_information_consumption_api.TemporalContextInformationConsumptionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_temporal(self):
        """Test case for query_temporal

        Query temporal evolution of Entities.  # noqa: E501
        """
        pass

    def test_retrieve_temporal(self):
        """Test case for retrieve_temporal

        Temporal Representation of Entity retrieval by id  # noqa: E501
        """
        pass

    def test_temporal_query_batch(self):
        """Test case for temporal_query_batch

        Temporal Representation of Entity Query based on POST  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
