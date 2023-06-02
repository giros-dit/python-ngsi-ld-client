# python-ngsi-ld-client

Python client for ETSI GS CIM 009 V1.6.1 cross-cutting Context Information Management (CIM); NGSI-LD API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

This Python-based NGSI-LD API client includes the class definition for a custom OpenAPI schema for the ietf-intefaces@2018-02-20.yang YANG module 
supported by a model-based network device. The source OpenAPI schemas for the NGSI-LD API V1.6.1 and the ietf-intefaces@2018-02-20.yang YANG module
are available [here](schemas/).

For validating example JSON-LD payloads (e.g., [IETF Interfaces examples](examples/interfaces/)) against the autogenerated Python class bindings, 
run the [test/test_interfaces.py](test/test_interfaces.py) Python unit test from the currect folder as follows:
```bash
$ python tests/interfaces.py
```

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ngsi_ld_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ngsi_ld_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ngsi_ld_client
from ngsi_ld_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost/ngsi-ld/v1"
)



# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextInformationConsumptionApi(api_client)
    query = ngsi_ld_client.Query() # Query | 
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)

    try:
        # Query entities based on POST.
        api_response = api_instance.query_batch(query, local=local, link=link, ngsild_tenant=ngsild_tenant)
        print("The response of ContextInformationConsumptionApi->query_batch:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContextInformationConsumptionApi->query_batch: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContextInformationConsumptionApi* | [**query_batch**](docs/ContextInformationConsumptionApi.md#query_batch) | **POST** /entityOperations/query | Query entities based on POST.
*ContextInformationConsumptionApi* | [**query_entity**](docs/ContextInformationConsumptionApi.md#query_entity) | **GET** /entities | Query entities 
*ContextInformationConsumptionApi* | [**query_subscription**](docs/ContextInformationConsumptionApi.md#query_subscription) | **GET** /subscriptions | Retrieve list of Subscriptions
*ContextInformationConsumptionApi* | [**retrieve_attr_info**](docs/ContextInformationConsumptionApi.md#retrieve_attr_info) | **GET** /attributes/{attrId} | Retrieve Available Attribute Information
*ContextInformationConsumptionApi* | [**retrieve_attributes**](docs/ContextInformationConsumptionApi.md#retrieve_attributes) | **GET** /attributes | Retrieve Available Attributes
*ContextInformationConsumptionApi* | [**retrieve_entity**](docs/ContextInformationConsumptionApi.md#retrieve_entity) | **GET** /entities/{entityId} | Entity retrieval by id 
*ContextInformationConsumptionApi* | [**retrieve_subscription**](docs/ContextInformationConsumptionApi.md#retrieve_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription retrieval by id
*ContextInformationConsumptionApi* | [**retrieve_type_info**](docs/ContextInformationConsumptionApi.md#retrieve_type_info) | **GET** /types/{type} | Details about available entity type
*ContextInformationConsumptionApi* | [**retrieve_types**](docs/ContextInformationConsumptionApi.md#retrieve_types) | **GET** /types | Retrieve available entity types
*ContextInformationProvisionApi* | [**append_attrs**](docs/ContextInformationProvisionApi.md#append_attrs) | **POST** /entities/{entityId}/attrs | Append attributes to Entity 
*ContextInformationProvisionApi* | [**create_batch**](docs/ContextInformationProvisionApi.md#create_batch) | **POST** /entityOperations/create | Batch Entity creation. 
*ContextInformationProvisionApi* | [**create_entity**](docs/ContextInformationProvisionApi.md#create_entity) | **POST** /entities | Entity creation 
*ContextInformationProvisionApi* | [**delete_attrs**](docs/ContextInformationProvisionApi.md#delete_attrs) | **DELETE** /entities/{entityId}/attrs/{attrId} | Attribute delete 
*ContextInformationProvisionApi* | [**delete_batch**](docs/ContextInformationProvisionApi.md#delete_batch) | **POST** /entityOperations/delete | Batch Entity delete. 
*ContextInformationProvisionApi* | [**delete_entity**](docs/ContextInformationProvisionApi.md#delete_entity) | **DELETE** /entities/{entityId} | Entity deletion by id 
*ContextInformationProvisionApi* | [**merge_batch**](docs/ContextInformationProvisionApi.md#merge_batch) | **POST** /entityOperations/merge | Batch Entity merge. 
*ContextInformationProvisionApi* | [**merge_entity**](docs/ContextInformationProvisionApi.md#merge_entity) | **PATCH** /entities/{entityId} | Entity merge by id. 
*ContextInformationProvisionApi* | [**replace_attrs**](docs/ContextInformationProvisionApi.md#replace_attrs) | **PUT** /entities/{entityId}/attrs/{attrId} | Attribute replace. 
*ContextInformationProvisionApi* | [**replace_entity**](docs/ContextInformationProvisionApi.md#replace_entity) | **PUT** /entities/{entityId} | Entity replacement by id. 
*ContextInformationProvisionApi* | [**update_attrs**](docs/ContextInformationProvisionApi.md#update_attrs) | **PATCH** /entities/{entityId}/attrs/{attrId} | Partial Attribute update 
*ContextInformationProvisionApi* | [**update_batch**](docs/ContextInformationProvisionApi.md#update_batch) | **POST** /entityOperations/update | Batch Entity update. 
*ContextInformationProvisionApi* | [**update_entity**](docs/ContextInformationProvisionApi.md#update_entity) | **PATCH** /entities/{entityId}/attrs | Update attributes of an Entity 
*ContextInformationProvisionApi* | [**upsert_batch**](docs/ContextInformationProvisionApi.md#upsert_batch) | **POST** /entityOperations/upsert | Batch Entity create or update (upsert). 
*ContextInformationSubscriptionApi* | [**create_subscription**](docs/ContextInformationSubscriptionApi.md#create_subscription) | **POST** /subscriptions | Create Subscription
*ContextInformationSubscriptionApi* | [**delete_subscription**](docs/ContextInformationSubscriptionApi.md#delete_subscription) | **DELETE** /subscriptions/{subscriptionId} | Subscription deletion by id
*ContextInformationSubscriptionApi* | [**update_subscription**](docs/ContextInformationSubscriptionApi.md#update_subscription) | **PATCH** /subscriptions/{subscriptionId} | Subscription update by id
*ContextSourceDiscoveryApi* | [**query_csr**](docs/ContextSourceDiscoveryApi.md#query_csr) | **GET** /csourceRegistrations | Discover Csource registrations 
*ContextSourceDiscoveryApi* | [**retrieve_csr**](docs/ContextSourceDiscoveryApi.md#retrieve_csr) | **GET** /csourceRegistrations/{registrationId} | Csource registration retrieval by id
*ContextSourceRegistrationApi* | [**create_csr**](docs/ContextSourceRegistrationApi.md#create_csr) | **POST** /csourceRegistrations | Csource registration creation
*ContextSourceRegistrationApi* | [**delete_csr**](docs/ContextSourceRegistrationApi.md#delete_csr) | **DELETE** /csourceRegistrations/{registrationId} | Csource registration deletion by id
*ContextSourceRegistrationApi* | [**delete_csr_subscription**](docs/ContextSourceRegistrationApi.md#delete_csr_subscription) | **DELETE** /csourceSubscriptions/{subscriptionId} | Csource registration subscription deletion by id 
*ContextSourceRegistrationApi* | [**update_csr**](docs/ContextSourceRegistrationApi.md#update_csr) | **PATCH** /csourceRegistrations/{registrationId} | Csource registration update by id
*ContextSourceRegistrationSubscriptionApi* | [**create_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#create_csr_subscription) | **POST** /csourceSubscriptions | Create subscription to Csource registration 
*ContextSourceRegistrationSubscriptionApi* | [**query_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#query_csr_subscription) | **GET** /csourceSubscriptions | Retrieval of list of subscription to Csource registration 
*ContextSourceRegistrationSubscriptionApi* | [**retrieve_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#retrieve_csr_subscription) | **GET** /csourceSubscriptions/{subscriptionId} | Retrieval of list of subscription to Csource registration 
*ContextSourceRegistrationSubscriptionApi* | [**update_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#update_csr_subscription) | **PATCH** /csourceSubscriptions/{subscriptionId} | Csource registration subscription update by id 
*JSONLDContextAPIApi* | [**create_context**](docs/JSONLDContextAPIApi.md#create_context) | **POST** /jsonldContexts | Add a user @context to the internal cache
*JSONLDContextAPIApi* | [**delete_context**](docs/JSONLDContextAPIApi.md#delete_context) | **DELETE** /jsonldContexts/{contextId} | Delete one specific @context from internal cache, possibly re-inserting a freshly downloaded copy of it
*JSONLDContextAPIApi* | [**list_contexts**](docs/JSONLDContextAPIApi.md#list_contexts) | **GET** /jsonldContexts | List all cached @contexts
*JSONLDContextAPIApi* | [**retrieve_context**](docs/JSONLDContextAPIApi.md#retrieve_context) | **GET** /jsonldContexts/{contextId} | Serve one specific user @context
*TemporalContextInformationConsumptionApi* | [**query_temporal**](docs/TemporalContextInformationConsumptionApi.md#query_temporal) | **GET** /temporal/entities | Query temporal evolution of Entities.
*TemporalContextInformationConsumptionApi* | [**retrieve_temporal**](docs/TemporalContextInformationConsumptionApi.md#retrieve_temporal) | **GET** /temporal/entities/{entityId} | Temporal Representation of Entity retrieval by id
*TemporalContextInformationConsumptionApi* | [**temporal_query_batch**](docs/TemporalContextInformationConsumptionApi.md#temporal_query_batch) | **POST** /temporal/entityOperations/query | Temporal Representation of Entity Query based on POST
*TemporalContextInformationProvisionApi* | [**append_attrs_temporal**](docs/TemporalContextInformationProvisionApi.md#append_attrs_temporal) | **POST** /temporal/entities/{entityId}/attrs | Temporal Representation of Entity Attribute instance addition 
*TemporalContextInformationProvisionApi* | [**delete_attr_instance_temporal**](docs/TemporalContextInformationProvisionApi.md#delete_attr_instance_temporal) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | Attribute Instance deletion by instance id. 
*TemporalContextInformationProvisionApi* | [**delete_attrs_temporal**](docs/TemporalContextInformationProvisionApi.md#delete_attrs_temporal) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId} | Attribute from Temporal Representation of Entity deletion. 
*TemporalContextInformationProvisionApi* | [**delete_temporal**](docs/TemporalContextInformationProvisionApi.md#delete_temporal) | **DELETE** /temporal/entities/{entityId} | Temporal Representation of Entity deletion by id. 
*TemporalContextInformationProvisionApi* | [**update_attrs_temporal**](docs/TemporalContextInformationProvisionApi.md#update_attrs_temporal) | **PATCH** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | Attribute Instance update. 
*TemporalContextInformationProvisionApi* | [**upsert_temporal**](docs/TemporalContextInformationProvisionApi.md#upsert_temporal) | **POST** /temporal/entities | Temporal Representation of Entity creation. 


## Documentation For Models

 - [AdminStatus](docs/AdminStatus.md)
 - [AdminStatusAllOf](docs/AdminStatusAllOf.md)
 - [AdminStatusOptions](docs/AdminStatusOptions.md)
 - [Description](docs/Description.md)
 - [DiscontinuityTime](docs/DiscontinuityTime.md)
 - [Enabled](docs/Enabled.md)
 - [EnabledAllOf](docs/EnabledAllOf.md)
 - [EntityCommon](docs/EntityCommon.md)
 - [EntityCommonScope](docs/EntityCommonScope.md)
 - [EntityCommonType](docs/EntityCommonType.md)
 - [EntityFragmentInput](docs/EntityFragmentInput.md)
 - [EntityFragmentInputAllOf](docs/EntityFragmentInputAllOf.md)
 - [EntityInput](docs/EntityInput.md)
 - [GeoPropertyCommon](docs/GeoPropertyCommon.md)
 - [GeoPropertyFragmentInput](docs/GeoPropertyFragmentInput.md)
 - [GeoPropertyInput](docs/GeoPropertyInput.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryLineString](docs/GeometryLineString.md)
 - [GeometryMultiLineString](docs/GeometryMultiLineString.md)
 - [GeometryMultiPoint](docs/GeometryMultiPoint.md)
 - [GeometryMultiPolygon](docs/GeometryMultiPolygon.md)
 - [GeometryPoint](docs/GeometryPoint.md)
 - [GeometryPolygon](docs/GeometryPolygon.md)
 - [HigherLayerIf](docs/HigherLayerIf.md)
 - [HigherLayerIfAllOf](docs/HigherLayerIfAllOf.md)
 - [IfIndex](docs/IfIndex.md)
 - [IfIndexAllOf](docs/IfIndexAllOf.md)
 - [InBroadcastPkts](docs/InBroadcastPkts.md)
 - [InDiscards](docs/InDiscards.md)
 - [InErrors](docs/InErrors.md)
 - [InMulticastPkts](docs/InMulticastPkts.md)
 - [InOctets](docs/InOctets.md)
 - [InUnicastPkts](docs/InUnicastPkts.md)
 - [InUnknownProtos](docs/InUnknownProtos.md)
 - [Interface](docs/Interface.md)
 - [InterfaceAllOf](docs/InterfaceAllOf.md)
 - [IsPartOf](docs/IsPartOf.md)
 - [LastChange](docs/LastChange.md)
 - [LastChangeAllOf](docs/LastChangeAllOf.md)
 - [LinkUpDownTrapEnable](docs/LinkUpDownTrapEnable.md)
 - [LinkUpDownTrapEnableAllOf](docs/LinkUpDownTrapEnableAllOf.md)
 - [LinkUpDownTrapEnableOptions](docs/LinkUpDownTrapEnableOptions.md)
 - [LowerLayerIf](docs/LowerLayerIf.md)
 - [Name](docs/Name.md)
 - [NameAllOf](docs/NameAllOf.md)
 - [OperStatus](docs/OperStatus.md)
 - [OperStatusOptions](docs/OperStatusOptions.md)
 - [OutBroadcastPkts](docs/OutBroadcastPkts.md)
 - [OutDiscards](docs/OutDiscards.md)
 - [OutErrors](docs/OutErrors.md)
 - [OutMulticastPkts](docs/OutMulticastPkts.md)
 - [OutOctets](docs/OutOctets.md)
 - [OutUnicastPkts](docs/OutUnicastPkts.md)
 - [PhysAddress](docs/PhysAddress.md)
 - [PhysAddressAllOf](docs/PhysAddressAllOf.md)
 - [PropertyCommon](docs/PropertyCommon.md)
 - [PropertyFragmentInput](docs/PropertyFragmentInput.md)
 - [PropertyInput](docs/PropertyInput.md)
 - [RelationshipCommon](docs/RelationshipCommon.md)
 - [RelationshipFragmentInput](docs/RelationshipFragmentInput.md)
 - [RelationshipInput](docs/RelationshipInput.md)
 - [Speed](docs/Speed.md)
 - [Statistics](docs/Statistics.md)
 - [StatisticsAllOf](docs/StatisticsAllOf.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author



