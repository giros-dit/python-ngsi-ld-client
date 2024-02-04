# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client.models.entity_selector import EntitySelector

class TestEntitySelector(unittest.TestCase):
    """EntitySelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitySelector:
        """Test EntitySelector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitySelector`
        """
        model = EntitySelector()
        if include_optional:
            return EntitySelector(
                id = '',
                id_pattern = '',
                type = ''
            )
        else:
            return EntitySelector(
                type = '',
        )
        """

    def testEntitySelector(self):
        """Test EntitySelector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
