# python-ngsi-ld-client
Python client for [`ETSI GS CIM 009 V1.6.1`](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.06.01_60/gs_CIM009v010601p.pdf) cross-cutting Context Information Management (CIM); NGSI-LD API. The OpenAPI specification for the NGSI-LD API is available [here](https://forge.etsi.org/rep/cim/NGSI-LD/-/tree/1.6.1).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

For more information, please visit [https://www.etsi.org/committee/cim](https://www.etsi.org/committee/cim)

The OpenAPI for NGSI-LD API V1.6.1 from which the Python-based client was generated is available [here](schemas/ngsi-ld-api.yaml).

To generate the code derived from the particular schemas defined within the OpenAPI, the [OpenAPI Generator Docker image option](https://openapi-generator.tech/docs/installation#docker) has been used with the following command executed from the current folder:
```bash
$ docker run --rm -v ${PWD}:/python-ngsi-ld-client openapitools/openapi-generator-cli generate -i /python-ngsi-ld-client/schemas/ngsi-ld-api.yaml -g python --package-name ngsi_ld_client -o /python-ngsi-ld-client --additional-properties disallowAdditionalPropertiesIfNotPresent=false --skip-validate-spec
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

# Defining the host is optional and defaults to https://localhost:443/ngsi-ld/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "https://localhost:443/ngsi-ld/v1"
)



# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ngsi_ld_client.ContextInformationConsumptionApi(api_client)
    local = True # bool | 6.3.18 Limiting Distributed Operations. If local=true then no Context Source Registrations shall be considered as matching to avoid cascading distributed operations (see clause 4.3.6.4).  (optional)
    link = 'link_example' # str | 6.3.5 JSON-LD @context resolution  In summary, from a developer's perspective, for POST, PATCH and PUT operations, if MIME type is \"application/ld+json\", then the associated @context shall be provided only as part of the request payload body. Likewise, if MIME type is \"application/json\", then the associated @context shall be provided only by using the JSON- LD Link header. No mixes are allowed, i.e. mixing options shall result in HTTP response errors. Implementations should provide descriptive error messages when these situations arise.  In contrast, GET and DELETE operations always take their input @context from the JSON-LD Link Header.  (optional)
    ngsild_tenant = 'ngsild_tenant_example' # str | 6.3.14 Tenant specification. The tenant to which the NGSI-LD HTTP operation is targeted.  (optional)
    query = ngsi_ld_client.Query() # Query |  (optional)

    try:
        # Query entities based on POST 
        api_response = api_instance.query_batch(local=local, link=link, ngsild_tenant=ngsild_tenant, query=query)
        print("The response of ContextInformationConsumptionApi->query_batch:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContextInformationConsumptionApi->query_batch: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:443/ngsi-ld/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContextInformationConsumptionApi* | [**query_batch**](docs/ContextInformationConsumptionApi.md#query_batch) | **POST** /entityOperations/query | Query entities based on POST 
*ContextInformationConsumptionApi* | [**query_entity**](docs/ContextInformationConsumptionApi.md#query_entity) | **GET** /entities | Query entities 
*ContextInformationConsumptionApi* | [**query_subscription**](docs/ContextInformationConsumptionApi.md#query_subscription) | **GET** /subscriptions | Retrieve list of Subscriptions 
*ContextInformationConsumptionApi* | [**retrieve_attr_info**](docs/ContextInformationConsumptionApi.md#retrieve_attr_info) | **GET** /attributes/{attrId} | Retrieve Available Attribute Information 
*ContextInformationConsumptionApi* | [**retrieve_attributes**](docs/ContextInformationConsumptionApi.md#retrieve_attributes) | **GET** /attributes | Retrieve Available Attributes 
*ContextInformationConsumptionApi* | [**retrieve_entity**](docs/ContextInformationConsumptionApi.md#retrieve_entity) | **GET** /entities/{entityId} | Entity retrieval by id 
*ContextInformationConsumptionApi* | [**retrieve_subscription**](docs/ContextInformationConsumptionApi.md#retrieve_subscription) | **GET** /subscriptions/{subscriptionId} | Subscription retrieval by id 
*ContextInformationConsumptionApi* | [**retrieve_type_info**](docs/ContextInformationConsumptionApi.md#retrieve_type_info) | **GET** /types/{type} | Details about available entity type 
*ContextInformationConsumptionApi* | [**retrieve_types**](docs/ContextInformationConsumptionApi.md#retrieve_types) | **GET** /types | Retrieve available entity types 
*ContextInformationProvisionApi* | [**append_attrs**](docs/ContextInformationProvisionApi.md#append_attrs) | **POST** /entities/{entityId}/attrs | Append attributes to Entity 
*ContextInformationProvisionApi* | [**create_batch**](docs/ContextInformationProvisionApi.md#create_batch) | **POST** /entityOperations/create | Batch Entity creation 
*ContextInformationProvisionApi* | [**create_entity**](docs/ContextInformationProvisionApi.md#create_entity) | **POST** /entities | Entity creation 
*ContextInformationProvisionApi* | [**delete_attrs**](docs/ContextInformationProvisionApi.md#delete_attrs) | **DELETE** /entities/{entityId}/attrs/{attrId} | Attribute delete 
*ContextInformationProvisionApi* | [**delete_batch**](docs/ContextInformationProvisionApi.md#delete_batch) | **POST** /entityOperations/delete | Batch Entity delete 
*ContextInformationProvisionApi* | [**delete_entity**](docs/ContextInformationProvisionApi.md#delete_entity) | **DELETE** /entities/{entityId} | Entity deletion by id 
*ContextInformationProvisionApi* | [**merge_batch**](docs/ContextInformationProvisionApi.md#merge_batch) | **POST** /entityOperations/merge | Batch Entity merge 
*ContextInformationProvisionApi* | [**merge_entity**](docs/ContextInformationProvisionApi.md#merge_entity) | **PATCH** /entities/{entityId} | Entity merge by id 
*ContextInformationProvisionApi* | [**replace_attrs**](docs/ContextInformationProvisionApi.md#replace_attrs) | **PUT** /entities/{entityId}/attrs/{attrId} | Attribute replace 
*ContextInformationProvisionApi* | [**replace_entity**](docs/ContextInformationProvisionApi.md#replace_entity) | **PUT** /entities/{entityId} | Entity replacement by id 
*ContextInformationProvisionApi* | [**update_attrs**](docs/ContextInformationProvisionApi.md#update_attrs) | **PATCH** /entities/{entityId}/attrs/{attrId} | Partial Attribute update 
*ContextInformationProvisionApi* | [**update_batch**](docs/ContextInformationProvisionApi.md#update_batch) | **POST** /entityOperations/update | Batch Entity update 
*ContextInformationProvisionApi* | [**update_entity**](docs/ContextInformationProvisionApi.md#update_entity) | **PATCH** /entities/{entityId}/attrs | Update attributes of an Entity 
*ContextInformationProvisionApi* | [**upsert_batch**](docs/ContextInformationProvisionApi.md#upsert_batch) | **POST** /entityOperations/upsert | Batch Entity create or update (upsert) 
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
*ContextSourceRegistrationSubscriptionApi* | [**query_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#query_csr_subscription) | **GET** /csourceSubscriptions | Retrieval of list of subscriptions to Csource registrations 
*ContextSourceRegistrationSubscriptionApi* | [**retrieve_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#retrieve_csr_subscription) | **GET** /csourceSubscriptions/{subscriptionId} | Retrieval of subscription to Csource registration by id 
*ContextSourceRegistrationSubscriptionApi* | [**update_csr_subscription**](docs/ContextSourceRegistrationSubscriptionApi.md#update_csr_subscription) | **PATCH** /csourceSubscriptions/{subscriptionId} | Csource registration subscription update by id 
*JSONLDContextAPIApi* | [**create_context**](docs/JSONLDContextAPIApi.md#create_context) | **POST** /jsonldContexts | Add a user @context to the internal cache 
*JSONLDContextAPIApi* | [**delete_context**](docs/JSONLDContextAPIApi.md#delete_context) | **DELETE** /jsonldContexts/{contextId} | Delete one specific @context from internal cache, possibly re-inserting a freshly downloaded copy of it 
*JSONLDContextAPIApi* | [**list_contexts**](docs/JSONLDContextAPIApi.md#list_contexts) | **GET** /jsonldContexts | List all cached @contexts 
*JSONLDContextAPIApi* | [**retrieve_context**](docs/JSONLDContextAPIApi.md#retrieve_context) | **GET** /jsonldContexts/{contextId} | Serve one specific user @context 
*TemporalContextInformationConsumptionApi* | [**query_temporal**](docs/TemporalContextInformationConsumptionApi.md#query_temporal) | **GET** /temporal/entities | Query temporal evolution of Entities 
*TemporalContextInformationConsumptionApi* | [**retrieve_temporal**](docs/TemporalContextInformationConsumptionApi.md#retrieve_temporal) | **GET** /temporal/entities/{entityId} | Temporal Representation of Entity retrieval by id 
*TemporalContextInformationConsumptionApi* | [**temporal_query_batch**](docs/TemporalContextInformationConsumptionApi.md#temporal_query_batch) | **POST** /temporal/entityOperations/query | Temporal Representation of Entity Query based on POST 
*TemporalContextInformationProvisionApi* | [**append_attrs_temporal**](docs/TemporalContextInformationProvisionApi.md#append_attrs_temporal) | **POST** /temporal/entities/{entityId}/attrs | Temporal Representation of Entity Attribute instance addition 
*TemporalContextInformationProvisionApi* | [**delete_attr_instance_temporal**](docs/TemporalContextInformationProvisionApi.md#delete_attr_instance_temporal) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | Attribute Instance deletion by instance id 
*TemporalContextInformationProvisionApi* | [**delete_attrs_temporal**](docs/TemporalContextInformationProvisionApi.md#delete_attrs_temporal) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId} | Attribute from Temporal Representation of Entity deletion 
*TemporalContextInformationProvisionApi* | [**delete_temporal**](docs/TemporalContextInformationProvisionApi.md#delete_temporal) | **DELETE** /temporal/entities/{entityId} | Temporal Representation of Entity deletion by id 
*TemporalContextInformationProvisionApi* | [**update_attrs_temporal**](docs/TemporalContextInformationProvisionApi.md#update_attrs_temporal) | **PATCH** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | Attribute Instance update 
*TemporalContextInformationProvisionApi* | [**upsert_temporal**](docs/TemporalContextInformationProvisionApi.md#upsert_temporal) | **POST** /temporal/entities | Temporal Representation of Entity creation 


## Documentation For Models

 - [AppendAttrsTemporalRequest](docs/AppendAttrsTemporalRequest.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeList](docs/AttributeList.md)
 - [BatchEntityError](docs/BatchEntityError.md)
 - [BatchOperationResult](docs/BatchOperationResult.md)
 - [CreateBatch201Response](docs/CreateBatch201Response.md)
 - [CreateBatchRequest](docs/CreateBatchRequest.md)
 - [CreateCSRRequest](docs/CreateCSRRequest.md)
 - [CreateCSRRequest1](docs/CreateCSRRequest1.md)
 - [CreateEntityRequest](docs/CreateEntityRequest.md)
 - [CreateSubscriptionRequest](docs/CreateSubscriptionRequest.md)
 - [CreateSubscriptionRequest1](docs/CreateSubscriptionRequest1.md)
 - [CsourceNotification](docs/CsourceNotification.md)
 - [CsourceRegistration](docs/CsourceRegistration.md)
 - [CsourceRegistrationScope](docs/CsourceRegistrationScope.md)
 - [DateTimeValue](docs/DateTimeValue.md)
 - [Endpoint](docs/Endpoint.md)
 - [Entity](docs/Entity.md)
 - [EntityAdditionalProperties](docs/EntityAdditionalProperties.md)
 - [EntityInfo](docs/EntityInfo.md)
 - [EntityInfoType](docs/EntityInfoType.md)
 - [EntityScope](docs/EntityScope.md)
 - [EntitySelector](docs/EntitySelector.md)
 - [EntityTemporal](docs/EntityTemporal.md)
 - [EntityTemporalValue](docs/EntityTemporalValue.md)
 - [EntityType](docs/EntityType.md)
 - [EntityTypeInfo](docs/EntityTypeInfo.md)
 - [EntityTypeList](docs/EntityTypeList.md)
 - [Feature](docs/Feature.md)
 - [FeatureCollection](docs/FeatureCollection.md)
 - [FeatureProperties](docs/FeatureProperties.md)
 - [FeaturePropertiesType](docs/FeaturePropertiesType.md)
 - [FeaturePropertiesValue](docs/FeaturePropertiesValue.md)
 - [GeoProperty](docs/GeoProperty.md)
 - [GeoQuery](docs/GeoQuery.md)
 - [GeoQueryCoordinates](docs/GeoQueryCoordinates.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryLineString](docs/GeometryLineString.md)
 - [GeometryLinearRing](docs/GeometryLinearRing.md)
 - [GeometryMultiLineString](docs/GeometryMultiLineString.md)
 - [GeometryMultiPoint](docs/GeometryMultiPoint.md)
 - [GeometryMultiPolygon](docs/GeometryMultiPolygon.md)
 - [GeometryPoint](docs/GeometryPoint.md)
 - [GeometryPolygon](docs/GeometryPolygon.md)
 - [KeyValuePair](docs/KeyValuePair.md)
 - [LanguageProperty](docs/LanguageProperty.md)
 - [LdContext](docs/LdContext.md)
 - [LdContextOneOfInner](docs/LdContextOneOfInner.md)
 - [ListContexts200Response](docs/ListContexts200Response.md)
 - [ListContexts200Response1](docs/ListContexts200Response1.md)
 - [ListContexts200Response1OneOfInner](docs/ListContexts200Response1OneOfInner.md)
 - [ListContexts200Response1OneOfInner1](docs/ListContexts200Response1OneOfInner1.md)
 - [ModelProperty](docs/ModelProperty.md)
 - [NotUpdatedDetails](docs/NotUpdatedDetails.md)
 - [Notification](docs/Notification.md)
 - [NotificationData](docs/NotificationData.md)
 - [NotificationParams](docs/NotificationParams.md)
 - [OptionsNoOverwrite](docs/OptionsNoOverwrite.md)
 - [OptionsRepresentation](docs/OptionsRepresentation.md)
 - [OptionsSysAttrs](docs/OptionsSysAttrs.md)
 - [OptionsTemporal](docs/OptionsTemporal.md)
 - [OptionsUpsert](docs/OptionsUpsert.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [PropertyPreviousValue](docs/PropertyPreviousValue.md)
 - [PropertyValue](docs/PropertyValue.md)
 - [Query](docs/Query.md)
 - [QueryBatchRequest](docs/QueryBatchRequest.md)
 - [QueryCSR200ResponseInner](docs/QueryCSR200ResponseInner.md)
 - [QueryCSR200ResponseInner1](docs/QueryCSR200ResponseInner1.md)
 - [QueryEntity200ResponseInner](docs/QueryEntity200ResponseInner.md)
 - [QueryEntity200ResponseInner1](docs/QueryEntity200ResponseInner1.md)
 - [QueryEntityCoordinatesParameter](docs/QueryEntityCoordinatesParameter.md)
 - [QueryEntityGeorelParameter](docs/QueryEntityGeorelParameter.md)
 - [QueryEntityOptionsParameterInner](docs/QueryEntityOptionsParameterInner.md)
 - [QuerySubscription200ResponseInner](docs/QuerySubscription200ResponseInner.md)
 - [QuerySubscription200ResponseInner1](docs/QuerySubscription200ResponseInner1.md)
 - [QueryTemporal](docs/QueryTemporal.md)
 - [QueryTemporal200ResponseInner](docs/QueryTemporal200ResponseInner.md)
 - [QueryTemporal200ResponseInner1](docs/QueryTemporal200ResponseInner1.md)
 - [RegistrationInfo](docs/RegistrationInfo.md)
 - [RegistrationManagementInfo](docs/RegistrationManagementInfo.md)
 - [Relationship](docs/Relationship.md)
 - [ReplaceAttrsRequest](docs/ReplaceAttrsRequest.md)
 - [ReplaceAttrsRequest1](docs/ReplaceAttrsRequest1.md)
 - [ReplaceEntityRequest](docs/ReplaceEntityRequest.md)
 - [RetrieveAttrInfo200Response](docs/RetrieveAttrInfo200Response.md)
 - [RetrieveAttributes200Response](docs/RetrieveAttributes200Response.md)
 - [RetrieveContext200Response](docs/RetrieveContext200Response.md)
 - [RetrieveTypeInfo200Response](docs/RetrieveTypeInfo200Response.md)
 - [RetrieveTypes200Response](docs/RetrieveTypes200Response.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionCommon](docs/SubscriptionCommon.md)
 - [SubscriptionOnChange](docs/SubscriptionOnChange.md)
 - [SubscriptionPeriodic](docs/SubscriptionPeriodic.md)
 - [TemporalQuery](docs/TemporalQuery.md)
 - [TemporalQueryBatchRequest](docs/TemporalQueryBatchRequest.md)
 - [TimeInterval](docs/TimeInterval.md)
 - [UpdateCSRRequest](docs/UpdateCSRRequest.md)
 - [UpdateResult](docs/UpdateResult.md)
 - [UpdateSubscriptionRequest](docs/UpdateSubscriptionRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




