# coding: utf-8

# flake8: noqa
"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from ngsi_ld_client.models.append_attrs_temporal_request import AppendAttrsTemporalRequest
from ngsi_ld_client.models.attribute import Attribute
from ngsi_ld_client.models.attribute_list import AttributeList
from ngsi_ld_client.models.batch_entity_error import BatchEntityError
from ngsi_ld_client.models.batch_operation_result import BatchOperationResult
from ngsi_ld_client.models.create_batch201_response import CreateBatch201Response
from ngsi_ld_client.models.create_batch_request import CreateBatchRequest
from ngsi_ld_client.models.create_csr_request import CreateCSRRequest
from ngsi_ld_client.models.create_csr_request1 import CreateCSRRequest1
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.create_subscription_request1 import CreateSubscriptionRequest1
from ngsi_ld_client.models.csource_notification import CsourceNotification
from ngsi_ld_client.models.csource_registration import CsourceRegistration
from ngsi_ld_client.models.csource_registration_scope import CsourceRegistrationScope
from ngsi_ld_client.models.date_time_value import DateTimeValue
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.models.entity import Entity
from ngsi_ld_client.models.entity_info import EntityInfo
from ngsi_ld_client.models.entity_info_type import EntityInfoType
from ngsi_ld_client.models.entity_scope import EntityScope
from ngsi_ld_client.models.entity_selector import EntitySelector
from ngsi_ld_client.models.entity_temporal import EntityTemporal
from ngsi_ld_client.models.entity_temporal_value import EntityTemporalValue
from ngsi_ld_client.models.entity_type import EntityType
from ngsi_ld_client.models.entity_type_info import EntityTypeInfo
from ngsi_ld_client.models.entity_type_list import EntityTypeList
from ngsi_ld_client.models.entity_value import EntityValue
from ngsi_ld_client.models.feature import Feature
from ngsi_ld_client.models.feature_collection import FeatureCollection
from ngsi_ld_client.models.feature_properties import FeatureProperties
from ngsi_ld_client.models.feature_properties_type import FeaturePropertiesType
from ngsi_ld_client.models.feature_properties_value import FeaturePropertiesValue
from ngsi_ld_client.models.geo_property import GeoProperty
from ngsi_ld_client.models.geo_query import GeoQuery
from ngsi_ld_client.models.geo_query_coordinates import GeoQueryCoordinates
from ngsi_ld_client.models.geometry import Geometry
from ngsi_ld_client.models.geometry_line_string import GeometryLineString
from ngsi_ld_client.models.geometry_linear_ring import GeometryLinearRing
from ngsi_ld_client.models.geometry_multi_line_string import GeometryMultiLineString
from ngsi_ld_client.models.geometry_multi_point import GeometryMultiPoint
from ngsi_ld_client.models.geometry_multi_polygon import GeometryMultiPolygon
from ngsi_ld_client.models.geometry_point import GeometryPoint
from ngsi_ld_client.models.geometry_polygon import GeometryPolygon
from ngsi_ld_client.models.key_value_pair import KeyValuePair
from ngsi_ld_client.models.language_property import LanguageProperty
from ngsi_ld_client.models.ld_context import LdContext
from ngsi_ld_client.models.ld_context_one_of_inner import LdContextOneOfInner
from ngsi_ld_client.models.list_contexts200_response import ListContexts200Response
from ngsi_ld_client.models.list_contexts200_response1 import ListContexts200Response1
from ngsi_ld_client.models.list_contexts200_response1_one_of_inner import ListContexts200Response1OneOfInner
from ngsi_ld_client.models.list_contexts200_response1_one_of_inner1 import ListContexts200Response1OneOfInner1
from ngsi_ld_client.models.model_property import ModelProperty
from ngsi_ld_client.models.not_updated_details import NotUpdatedDetails
from ngsi_ld_client.models.notification import Notification
from ngsi_ld_client.models.notification_data import NotificationData
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.options_no_overwrite import OptionsNoOverwrite
from ngsi_ld_client.models.options_representation import OptionsRepresentation
from ngsi_ld_client.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client.models.options_temporal import OptionsTemporal
from ngsi_ld_client.models.options_upsert import OptionsUpsert
from ngsi_ld_client.models.problem_details import ProblemDetails
from ngsi_ld_client.models.property_previous_value import PropertyPreviousValue
from ngsi_ld_client.models.property_value import PropertyValue
from ngsi_ld_client.models.query import Query
from ngsi_ld_client.models.query_batch_request import QueryBatchRequest
from ngsi_ld_client.models.query_csr200_response_inner import QueryCSR200ResponseInner
from ngsi_ld_client.models.query_csr200_response_inner1 import QueryCSR200ResponseInner1
from ngsi_ld_client.models.query_entity200_response_inner import QueryEntity200ResponseInner
from ngsi_ld_client.models.query_entity200_response_inner1 import QueryEntity200ResponseInner1
from ngsi_ld_client.models.query_entity_coordinates_parameter import QueryEntityCoordinatesParameter
from ngsi_ld_client.models.query_entity_georel_parameter import QueryEntityGeorelParameter
from ngsi_ld_client.models.query_entity_options_parameter_inner import QueryEntityOptionsParameterInner
from ngsi_ld_client.models.query_subscription200_response_inner import QuerySubscription200ResponseInner
from ngsi_ld_client.models.query_subscription200_response_inner1 import QuerySubscription200ResponseInner1
from ngsi_ld_client.models.query_temporal import QueryTemporal
from ngsi_ld_client.models.query_temporal200_response_inner import QueryTemporal200ResponseInner
from ngsi_ld_client.models.query_temporal200_response_inner1 import QueryTemporal200ResponseInner1
from ngsi_ld_client.models.registration_info import RegistrationInfo
from ngsi_ld_client.models.registration_management_info import RegistrationManagementInfo
from ngsi_ld_client.models.relationship import Relationship
from ngsi_ld_client.models.replace_attrs_request import ReplaceAttrsRequest
from ngsi_ld_client.models.replace_attrs_request1 import ReplaceAttrsRequest1
from ngsi_ld_client.models.replace_entity_request import ReplaceEntityRequest
from ngsi_ld_client.models.retrieve_attr_info200_response import RetrieveAttrInfo200Response
from ngsi_ld_client.models.retrieve_attributes200_response import RetrieveAttributes200Response
from ngsi_ld_client.models.retrieve_context200_response import RetrieveContext200Response
from ngsi_ld_client.models.retrieve_type_info200_response import RetrieveTypeInfo200Response
from ngsi_ld_client.models.retrieve_types200_response import RetrieveTypes200Response
from ngsi_ld_client.models.subscription import Subscription
from ngsi_ld_client.models.subscription_common import SubscriptionCommon
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.temporal_query import TemporalQuery
from ngsi_ld_client.models.temporal_query_batch_request import TemporalQueryBatchRequest
from ngsi_ld_client.models.time_interval import TimeInterval
from ngsi_ld_client.models.update_csr_request import UpdateCSRRequest
from ngsi_ld_client.models.update_result import UpdateResult
from ngsi_ld_client.models.update_subscription_request import UpdateSubscriptionRequest
