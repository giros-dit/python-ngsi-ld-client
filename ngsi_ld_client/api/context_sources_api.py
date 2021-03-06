# coding: utf-8

"""
    ETSI ISG CIM / NGSI-LD API

    This OAS file describes the NGSI-LD API defined by the ETSI ISG CIM group. This Cross-domain Context Information Management API allows to provide, consume and subscribe to context information in multiple scenarios and involving multiple stakeholders  # noqa: E501

    The version of the OpenAPI document: latest
    Contact: NGSI-LD@etsi.org
    Generated by: https://openapi-generator.tech
"""

from ngsi_ld_client.api_client import ApiClient
from ngsi_ld_client.api.context_sources_api_endpoints.create_c_source_subscription import CreateCSourceSubscription
from ngsi_ld_client.api.context_sources_api_endpoints.query_csources import QueryCsources
from ngsi_ld_client.api.context_sources_api_endpoints.register_csource import RegisterCsource
from ngsi_ld_client.api.context_sources_api_endpoints.remove_c_source_subscription import RemoveCSourceSubscription
from ngsi_ld_client.api.context_sources_api_endpoints.remove_csource import RemoveCsource
from ngsi_ld_client.api.context_sources_api_endpoints.retrieve_c_source_subscriptions import RetrieveCSourceSubscriptions
from ngsi_ld_client.api.context_sources_api_endpoints.retrieve_c_source_subscriptions_by_id import RetrieveCSourceSubscriptionsById
from ngsi_ld_client.api.context_sources_api_endpoints.retrieve_csource import RetrieveCsource
from ngsi_ld_client.api.context_sources_api_endpoints.update_c_source_subscription import UpdateCSourceSubscription


class ContextSourcesApi(
    CreateCSourceSubscription,
    QueryCsources,
    RegisterCsource,
    RemoveCSourceSubscription,
    RemoveCsource,
    RetrieveCSourceSubscriptions,
    RetrieveCSourceSubscriptionsById,
    RetrieveCsource,
    UpdateCSourceSubscription,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
