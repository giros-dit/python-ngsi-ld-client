# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client.api.temporal_context_information_consumption_api import TemporalContextInformationConsumptionApi


class TestTemporalContextInformationConsumptionApi(unittest.TestCase):
    """TemporalContextInformationConsumptionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TemporalContextInformationConsumptionApi()

    def tearDown(self) -> None:
        pass

    def test_query_temporal(self) -> None:
        """Test case for query_temporal

        Query temporal evolution of Entities 
        """
        pass

    def test_retrieve_temporal(self) -> None:
        """Test case for retrieve_temporal

        Temporal Representation of Entity retrieval by id 
        """
        pass

    def test_temporal_query_batch(self) -> None:
        """Test case for temporal_query_batch

        Temporal Representation of Entity Query based on POST 
        """
        pass


if __name__ == '__main__':
    unittest.main()
