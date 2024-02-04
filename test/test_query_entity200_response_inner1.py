# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ngsi_ld_client.models.query_entity200_response_inner1 import QueryEntity200ResponseInner1

class TestQueryEntity200ResponseInner1(unittest.TestCase):
    """QueryEntity200ResponseInner1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryEntity200ResponseInner1:
        """Test QueryEntity200ResponseInner1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryEntity200ResponseInner1`
        """
        model = QueryEntity200ResponseInner1()
        if include_optional:
            return QueryEntity200ResponseInner1(
                id = '',
                type = None,
                scope = None,
                location = {
                    'key' : null
                    },
                observation_space = {
                    'key' : null
                    },
                operation_space = {
                    'key' : null
                    },
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                context = None
            )
        else:
            return QueryEntity200ResponseInner1(
                id = '',
                type = None,
                context = None,
        )
        """

    def testQueryEntity200ResponseInner1(self):
        """Test QueryEntity200ResponseInner1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
