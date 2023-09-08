# coding: utf-8

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ngsi_ld_client.models.create_subscription_request1 import CreateSubscriptionRequest1  # noqa: E501

class TestCreateSubscriptionRequest1(unittest.TestCase):
    """CreateSubscriptionRequest1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSubscriptionRequest1:
        """Test CreateSubscriptionRequest1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSubscriptionRequest1`
        """
        model = CreateSubscriptionRequest1()  # noqa: E501
        if include_optional:
            return CreateSubscriptionRequest1(
                id = '',
                type = 'Subscription',
                subscription_name = '',
                description = '',
                entities = [
                    ngsi_ld_client.models.entity_selector.EntitySelector(
                        id = '', 
                        id_pattern = '', 
                        type = '', )
                    ],
                notification_trigger = [
                    'entityCreated'
                    ],
                q = '',
                geo_q = ngsi_ld_client.models.geo_query.GeoQuery(
                    geometry = '', 
                    coordinates = null, 
                    georel = '', 
                    geoproperty = '', ),
                csf = '',
                is_active = True,
                notification = ngsi_ld_client.models.notification_params.NotificationParams(
                    attributes = [
                        ''
                        ], 
                    sys_attrs = True, 
                    format = 'normalized', 
                    show_changes = True, 
                    endpoint = ngsi_ld_client.models.endpoint.Endpoint(
                        uri = '', 
                        accept = 'application/json', 
                        timeout = 1.337, 
                        cooldown = 1.337, 
                        receiver_info = [
                            ngsi_ld_client.models.key_value_pair.KeyValuePair(
                                key = '', 
                                value = '', )
                            ], 
                        notifier_info = [
                            ngsi_ld_client.models.key_value_pair.KeyValuePair(
                                key = '', 
                                value = '', )
                            ], ), 
                    status = 'ok', 
                    times_sent = 0, 
                    times_failed = 0, 
                    last_notification = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_failure = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_success = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                temporal_q = ngsi_ld_client.models.temporal_query.TemporalQuery(
                    timerel = 'before', 
                    time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_time_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    timeproperty = 'observedAt', ),
                scope_q = '',
                lang = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'active',
                watched_attributes = [
                    ''
                    ],
                throttling = 1,
                time_interval = 1,
                context = None
            )
        else:
            return CreateSubscriptionRequest1(
                type = 'Subscription',
                entities = [
                    ngsi_ld_client.models.entity_selector.EntitySelector(
                        id = '', 
                        id_pattern = '', 
                        type = '', )
                    ],
                time_interval = 1,
                context = None,
        )
        """

    def testCreateSubscriptionRequest1(self):
        """Test CreateSubscriptionRequest1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
