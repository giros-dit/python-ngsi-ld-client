# coding: utf-8

# flake8: noqa

"""
    NGSI-LD API

    ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.  # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.0"

# import apis into sdk package
from ngsi_ld_client.api.context_information_consumption_api import ContextInformationConsumptionApi
from ngsi_ld_client.api.context_information_provision_api import ContextInformationProvisionApi
from ngsi_ld_client.api.context_information_subscription_api import ContextInformationSubscriptionApi
from ngsi_ld_client.api.context_source_discovery_api import ContextSourceDiscoveryApi
from ngsi_ld_client.api.context_source_registration_api import ContextSourceRegistrationApi
from ngsi_ld_client.api.context_source_registration_subscription_api import ContextSourceRegistrationSubscriptionApi
from ngsi_ld_client.api.jsonld_context_api_api import JSONLDContextAPIApi
from ngsi_ld_client.api.temporal_context_information_consumption_api import TemporalContextInformationConsumptionApi
from ngsi_ld_client.api.temporal_context_information_provision_api import TemporalContextInformationProvisionApi

# import ApiClient
from ngsi_ld_client.api_response import ApiResponse
from ngsi_ld_client.api_client import ApiClient
from ngsi_ld_client.configuration import Configuration
from ngsi_ld_client.exceptions import OpenApiException
from ngsi_ld_client.exceptions import ApiTypeError
from ngsi_ld_client.exceptions import ApiValueError
from ngsi_ld_client.exceptions import ApiKeyError
from ngsi_ld_client.exceptions import ApiAttributeError
from ngsi_ld_client.exceptions import ApiException

# import models into sdk package
from ngsi_ld_client.models.admin_status import AdminStatus
from ngsi_ld_client.models.admin_status_all_of import AdminStatusAllOf
from ngsi_ld_client.models.admin_status_options import AdminStatusOptions
from ngsi_ld_client.models.append_attrs_temporal_request import AppendAttrsTemporalRequest
from ngsi_ld_client.models.attribute import Attribute
from ngsi_ld_client.models.attribute_list import AttributeList
from ngsi_ld_client.models.batch_entity_error import BatchEntityError
from ngsi_ld_client.models.batch_operation_result import BatchOperationResult
from ngsi_ld_client.models.create_batch201_response import CreateBatch201Response
from ngsi_ld_client.models.create_batch_request import CreateBatchRequest
from ngsi_ld_client.models.create_csr_request import CreateCSRRequest
from ngsi_ld_client.models.create_entity_request import CreateEntityRequest
from ngsi_ld_client.models.create_subscription_request import CreateSubscriptionRequest
from ngsi_ld_client.models.csource_notification import CsourceNotification
from ngsi_ld_client.models.csource_registration_fragment import CsourceRegistrationFragment
from ngsi_ld_client.models.csource_registration_fragment_scope import CsourceRegistrationFragmentScope
from ngsi_ld_client.models.csource_registration_input import CsourceRegistrationInput
from ngsi_ld_client.models.csource_registration_output import CsourceRegistrationOutput
from ngsi_ld_client.models.csource_registration_output_all_of import CsourceRegistrationOutputAllOf
from ngsi_ld_client.models.description import Description
from ngsi_ld_client.models.discontinuity_time import DiscontinuityTime
from ngsi_ld_client.models.enabled import Enabled
from ngsi_ld_client.models.enabled_all_of import EnabledAllOf
from ngsi_ld_client.models.endpoint import Endpoint
from ngsi_ld_client.models.entity_common import EntityCommon
from ngsi_ld_client.models.entity_common_scope import EntityCommonScope
from ngsi_ld_client.models.entity_common_type import EntityCommonType
from ngsi_ld_client.models.entity_fragment_input import EntityFragmentInput
from ngsi_ld_client.models.entity_fragment_input_all_of import EntityFragmentInputAllOf
from ngsi_ld_client.models.entity_info import EntityInfo
from ngsi_ld_client.models.entity_info_type import EntityInfoType
from ngsi_ld_client.models.entity_input import EntityInput
from ngsi_ld_client.models.entity_notification_output import EntityNotificationOutput
from ngsi_ld_client.models.entity_output import EntityOutput
from ngsi_ld_client.models.entity_output_all_of import EntityOutputAllOf
from ngsi_ld_client.models.entity_output_all_of1 import EntityOutputAllOf1
from ngsi_ld_client.models.entity_selector import EntitySelector
from ngsi_ld_client.models.entity_temporal_fragment_input import EntityTemporalFragmentInput
from ngsi_ld_client.models.entity_temporal_input import EntityTemporalInput
from ngsi_ld_client.models.entity_temporal_output import EntityTemporalOutput
from ngsi_ld_client.models.entity_type import EntityType
from ngsi_ld_client.models.entity_type_info import EntityTypeInfo
from ngsi_ld_client.models.entity_type_list import EntityTypeList
from ngsi_ld_client.models.feature import Feature
from ngsi_ld_client.models.feature_collection import FeatureCollection
from ngsi_ld_client.models.feature_properties import FeatureProperties
from ngsi_ld_client.models.feature_properties_type import FeaturePropertiesType
from ngsi_ld_client.models.feature_properties_value import FeaturePropertiesValue
from ngsi_ld_client.models.geo_property_common import GeoPropertyCommon
from ngsi_ld_client.models.geo_property_fragment_input import GeoPropertyFragmentInput
from ngsi_ld_client.models.geo_property_input import GeoPropertyInput
from ngsi_ld_client.models.geo_property_output import GeoPropertyOutput
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
from ngsi_ld_client.models.higher_layer_if import HigherLayerIf
from ngsi_ld_client.models.higher_layer_if_all_of import HigherLayerIfAllOf
from ngsi_ld_client.models.if_index import IfIndex
from ngsi_ld_client.models.if_index_all_of import IfIndexAllOf
from ngsi_ld_client.models.in_broadcast_pkts import InBroadcastPkts
from ngsi_ld_client.models.in_discards import InDiscards
from ngsi_ld_client.models.in_errors import InErrors
from ngsi_ld_client.models.in_multicast_pkts import InMulticastPkts
from ngsi_ld_client.models.in_octets import InOctets
from ngsi_ld_client.models.in_unicast_pkts import InUnicastPkts
from ngsi_ld_client.models.in_unknown_protos import InUnknownProtos
from ngsi_ld_client.models.interface import Interface
from ngsi_ld_client.models.interface_all_of import InterfaceAllOf
from ngsi_ld_client.models.is_part_of import IsPartOf
from ngsi_ld_client.models.key_value_pair import KeyValuePair
from ngsi_ld_client.models.language_property_common import LanguagePropertyCommon
from ngsi_ld_client.models.language_property_fragment_input import LanguagePropertyFragmentInput
from ngsi_ld_client.models.language_property_input import LanguagePropertyInput
from ngsi_ld_client.models.language_property_notification_output import LanguagePropertyNotificationOutput
from ngsi_ld_client.models.language_property_notification_output_all_of import LanguagePropertyNotificationOutputAllOf
from ngsi_ld_client.models.language_property_output import LanguagePropertyOutput
from ngsi_ld_client.models.last_change import LastChange
from ngsi_ld_client.models.last_change_all_of import LastChangeAllOf
from ngsi_ld_client.models.ld_context import LdContext
from ngsi_ld_client.models.ld_context_one_of_inner import LdContextOneOfInner
from ngsi_ld_client.models.link_up_down_trap_enable import LinkUpDownTrapEnable
from ngsi_ld_client.models.link_up_down_trap_enable_all_of import LinkUpDownTrapEnableAllOf
from ngsi_ld_client.models.link_up_down_trap_enable_options import LinkUpDownTrapEnableOptions
from ngsi_ld_client.models.list_contexts200_response import ListContexts200Response
from ngsi_ld_client.models.list_contexts200_response1 import ListContexts200Response1
from ngsi_ld_client.models.list_contexts200_response1_one_of import ListContexts200Response1OneOf
from ngsi_ld_client.models.lower_layer_if import LowerLayerIf
from ngsi_ld_client.models.name import Name
from ngsi_ld_client.models.name_all_of import NameAllOf
from ngsi_ld_client.models.not_updated_details import NotUpdatedDetails
from ngsi_ld_client.models.notification import Notification
from ngsi_ld_client.models.notification_data import NotificationData
from ngsi_ld_client.models.notification_params import NotificationParams
from ngsi_ld_client.models.oper_status import OperStatus
from ngsi_ld_client.models.oper_status_options import OperStatusOptions
from ngsi_ld_client.models.options_no_overwrite import OptionsNoOverwrite
from ngsi_ld_client.models.options_representation import OptionsRepresentation
from ngsi_ld_client.models.options_sys_attrs import OptionsSysAttrs
from ngsi_ld_client.models.options_temporal import OptionsTemporal
from ngsi_ld_client.models.options_upsert import OptionsUpsert
from ngsi_ld_client.models.out_broadcast_pkts import OutBroadcastPkts
from ngsi_ld_client.models.out_discards import OutDiscards
from ngsi_ld_client.models.out_errors import OutErrors
from ngsi_ld_client.models.out_multicast_pkts import OutMulticastPkts
from ngsi_ld_client.models.out_octets import OutOctets
from ngsi_ld_client.models.out_unicast_pkts import OutUnicastPkts
from ngsi_ld_client.models.phys_address import PhysAddress
from ngsi_ld_client.models.phys_address_all_of import PhysAddressAllOf
from ngsi_ld_client.models.problem_details import ProblemDetails
from ngsi_ld_client.models.property_common import PropertyCommon
from ngsi_ld_client.models.property_fragment_input import PropertyFragmentInput
from ngsi_ld_client.models.property_input import PropertyInput
from ngsi_ld_client.models.property_notification_output import PropertyNotificationOutput
from ngsi_ld_client.models.property_notification_output_all_of import PropertyNotificationOutputAllOf
from ngsi_ld_client.models.property_output import PropertyOutput
from ngsi_ld_client.models.property_output_all_of import PropertyOutputAllOf
from ngsi_ld_client.models.query import Query
from ngsi_ld_client.models.query_batch_request import QueryBatchRequest
from ngsi_ld_client.models.query_csr200_response import QueryCSR200Response
from ngsi_ld_client.models.query_entity200_response import QueryEntity200Response
from ngsi_ld_client.models.query_entity200_response_all_of import QueryEntity200ResponseAllOf
from ngsi_ld_client.models.query_entity_coordinates_parameter import QueryEntityCoordinatesParameter
from ngsi_ld_client.models.query_entity_georel_parameter import QueryEntityGeorelParameter
from ngsi_ld_client.models.query_entity_options_parameter_inner import QueryEntityOptionsParameterInner
from ngsi_ld_client.models.query_subscription200_response import QuerySubscription200Response
from ngsi_ld_client.models.query_temporal import QueryTemporal
from ngsi_ld_client.models.query_temporal200_response import QueryTemporal200Response
from ngsi_ld_client.models.query_temporal_all_of import QueryTemporalAllOf
from ngsi_ld_client.models.registration_info import RegistrationInfo
from ngsi_ld_client.models.registration_management_info import RegistrationManagementInfo
from ngsi_ld_client.models.relationship_common import RelationshipCommon
from ngsi_ld_client.models.relationship_fragment_input import RelationshipFragmentInput
from ngsi_ld_client.models.relationship_input import RelationshipInput
from ngsi_ld_client.models.relationship_notification_output import RelationshipNotificationOutput
from ngsi_ld_client.models.relationship_notification_output_all_of import RelationshipNotificationOutputAllOf
from ngsi_ld_client.models.relationship_output import RelationshipOutput
from ngsi_ld_client.models.relationship_output_all_of import RelationshipOutputAllOf
from ngsi_ld_client.models.replace_attrs_request import ReplaceAttrsRequest
from ngsi_ld_client.models.replace_attrs_request1 import ReplaceAttrsRequest1
from ngsi_ld_client.models.replace_entity_request import ReplaceEntityRequest
from ngsi_ld_client.models.retrieve_attr_info200_response import RetrieveAttrInfo200Response
from ngsi_ld_client.models.retrieve_attributes200_response import RetrieveAttributes200Response
from ngsi_ld_client.models.retrieve_attributes200_response1 import RetrieveAttributes200Response1
from ngsi_ld_client.models.retrieve_attributes200_response1_one_of import RetrieveAttributes200Response1OneOf
from ngsi_ld_client.models.retrieve_csr200_response import RetrieveCSR200Response
from ngsi_ld_client.models.retrieve_context200_response import RetrieveContext200Response
from ngsi_ld_client.models.retrieve_entity200_response import RetrieveEntity200Response
from ngsi_ld_client.models.retrieve_subscription200_response import RetrieveSubscription200Response
from ngsi_ld_client.models.retrieve_temporal200_response import RetrieveTemporal200Response
from ngsi_ld_client.models.retrieve_type_info200_response import RetrieveTypeInfo200Response
from ngsi_ld_client.models.retrieve_types200_response import RetrieveTypes200Response
from ngsi_ld_client.models.retrieve_types200_response1 import RetrieveTypes200Response1
from ngsi_ld_client.models.retrieve_types200_response1_one_of import RetrieveTypes200Response1OneOf
from ngsi_ld_client.models.speed import Speed
from ngsi_ld_client.models.statistics import Statistics
from ngsi_ld_client.models.statistics_all_of import StatisticsAllOf
from ngsi_ld_client.models.subscription_common import SubscriptionCommon
from ngsi_ld_client.models.subscription_fragment import SubscriptionFragment
from ngsi_ld_client.models.subscription_fragment_on_change import SubscriptionFragmentOnChange
from ngsi_ld_client.models.subscription_fragment_on_change_all_of import SubscriptionFragmentOnChangeAllOf
from ngsi_ld_client.models.subscription_fragment_periodic import SubscriptionFragmentPeriodic
from ngsi_ld_client.models.subscription_fragment_periodic_all_of import SubscriptionFragmentPeriodicAllOf
from ngsi_ld_client.models.subscription_input import SubscriptionInput
from ngsi_ld_client.models.subscription_on_change import SubscriptionOnChange
from ngsi_ld_client.models.subscription_output import SubscriptionOutput
from ngsi_ld_client.models.subscription_output_all_of import SubscriptionOutputAllOf
from ngsi_ld_client.models.subscription_periodic import SubscriptionPeriodic
from ngsi_ld_client.models.temporal_query import TemporalQuery
from ngsi_ld_client.models.temporal_query_batch_request import TemporalQueryBatchRequest
from ngsi_ld_client.models.time_interval import TimeInterval
from ngsi_ld_client.models.update_csr_request import UpdateCSRRequest
from ngsi_ld_client.models.update_result import UpdateResult
from ngsi_ld_client.models.update_subscription_request import UpdateSubscriptionRequest
from ngsi_ld_client.models.upsert_temporal_request import UpsertTemporalRequest
