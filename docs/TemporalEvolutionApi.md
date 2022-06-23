# ngsi_ld_client.TemporalEvolutionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_temporal_entity_attrs**](TemporalEvolutionApi.md#add_temporal_entity_attrs) | **POST** /temporal/entities/{entityId}/attrs/ | 
[**create_update_entity_temporal**](TemporalEvolutionApi.md#create_update_entity_temporal) | **POST** /temporal/entities/ | 
[**modify_entity_temporal_attr_instance**](TemporalEvolutionApi.md#modify_entity_temporal_attr_instance) | **PATCH** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | 
[**query_temporal_entities**](TemporalEvolutionApi.md#query_temporal_entities) | **GET** /temporal/entities/ | 
[**remove_entity_temporal_attr**](TemporalEvolutionApi.md#remove_entity_temporal_attr) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId} | 
[**remove_entity_temporal_attr_instance**](TemporalEvolutionApi.md#remove_entity_temporal_attr_instance) | **DELETE** /temporal/entities/{entityId}/attrs/{attrId}/{instanceId} | 
[**remove_entity_temporal_by_id**](TemporalEvolutionApi.md#remove_entity_temporal_by_id) | **DELETE** /temporal/entities/{entityId} | 
[**retrieve_entity_temporal_by_id**](TemporalEvolutionApi.md#retrieve_entity_temporal_by_id) | **GET** /temporal/entities/{entityId} | 

# **add_temporal_entity_attrs**
> add_temporal_entity_attrs(entity_identity_temporal_fragment)



Add new attributes to an existing Temporal Entity within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.entity_temporal_fragment import EntityTemporalFragment
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    body = EntityTemporalFragment(
        context=LdContext(None),
        location=[
            GeoProperty(
                type="GeoProperty",
                value=GeoJSON(None),
                observed_at="1970-01-01T00:00:00.00Z",
                created_at="1970-01-01T00:00:00.00Z",
                modified_at="1970-01-01T00:00:00.00Z",
                dataset_id="dataset_id_example",
                instance_id="instance_id_example",
            )
        ],
        observation_space=[],
        operation_space=[],
        id="id_example",
        type=Name("_"),
        created_at="1970-01-01T00:00:00.00Z",
        modified_at="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.add_temporal_entity_attrs(
            path_params=path_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->add_temporal_entity_attrs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporalFragment**](EntityTemporalFragment.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporalFragment**](EntityTemporalFragment.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content
400 | ApiResponseFor400 | Bad request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_update_entity_temporal**
> create_update_entity_temporal(entity_temporal)



Create or update temporal representation of an Entity within an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.entity_temporal import EntityTemporal
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    body = EntityTemporal(None)
    try:
        api_response = api_instance.create_update_entity_temporal(
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->create_update_entity_temporal: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporal**](EntityTemporal.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporal**](EntityTemporal.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | ApiResponseFor201 | Created. Contains the resource URI of the created Entity
204 | ApiResponseFor204 | Updated. No Content
400 | ApiResponseFor400 | Bad request
409 | ApiResponseFor409 | Already exists
422 | ApiResponseFor422 | Unprocessable Entity

#### ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, SchemaFor409ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor409ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, SchemaFor422ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor422ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_entity_temporal_attr_instance**
> modify_entity_temporal_attr_instance(entity_idattr_idinstance_identity_temporal_fragment)



Allows modifying a specific Attribute (Property or Relationship) instance, identified by its instanceId, of a Temporal Representation of an Entity.

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.entity_temporal_fragment import EntityTemporalFragment
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
        'attrId': Name("_"),
        'instanceId': "instanceId_example",
    }
    body = EntityTemporalFragment(
        context=LdContext(None),
        location=[
            GeoProperty(
                type="GeoProperty",
                value=GeoJSON(None),
                observed_at="1970-01-01T00:00:00.00Z",
                created_at="1970-01-01T00:00:00.00Z",
                modified_at="1970-01-01T00:00:00.00Z",
                dataset_id="dataset_id_example",
                instance_id="instance_id_example",
            )
        ],
        observation_space=[],
        operation_space=[],
        id="id_example",
        type=Name("_"),
        created_at="1970-01-01T00:00:00.00Z",
        modified_at="1970-01-01T00:00:00.00Z",
    )
    try:
        api_response = api_instance.modify_entity_temporal_attr_instance(
            path_params=path_params,
            body=body,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->modify_entity_temporal_attr_instance: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyApplicationLdjson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

#### SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporalFragment**](EntityTemporalFragment.md) |  | 


#### SchemaForRequestBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporalFragment**](EntityTemporalFragment.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 
attrId | AttrIdSchema | | 
instanceId | InstanceIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


#### InstanceIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content
400 | ApiResponseFor400 | Bad request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_temporal_entities**
> EntityTemporalList query_temporal_entities()



Query temporal evolution of Entities from an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.coordinates import Coordinates
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.entity_temporal_list import EntityTemporalList
from ngsi_ld_client.model.geometry import Geometry
from ngsi_ld_client.model.georel import Georel
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.timerel import Timerel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only optional values
    query_params = {
        'id': "id_example",
        'idPattern': "idPattern_example",
        'type': "type_example",
        'attrs': "attrs_example",
        'q': "q_example",
        'georel': Georel(None),
        'geometry': Geometry("Point"),
        'coordinates': Coordinates(None),
        'geoproperty': "geoproperty_example",
        'timerel': Timerel("before"),
        'timeproperty': Name("_"),
        'time': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
        'csf': "csf_example",
        'limit': 1,
        'options': "temporalValues",
        'lastN': 1,
    }
    try:
        api_response = api_instance.query_temporal_entities(
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->query_temporal_entities: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | optional
idPattern | IdPatternSchema | | optional
type | TypeSchema | | optional
attrs | AttrsSchema | | optional
q | QSchema | | optional
georel | GeorelSchema | | optional
geometry | GeometrySchema | | optional
coordinates | CoordinatesSchema | | optional
geoproperty | GeopropertySchema | | optional
timerel | TimerelSchema | | optional
timeproperty | TimepropertySchema | | optional
time | TimeSchema | | optional
endTime | EndTimeSchema | | optional
csf | CsfSchema | | optional
limit | LimitSchema | | optional
options | OptionsSchema | | optional
lastN | LastNSchema | | optional


#### IdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### IdPatternSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### QSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### GeorelSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Georel**](Georel.md) |  | 


#### GeometrySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Geometry**](Geometry.md) |  | 


#### CoordinatesSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Coordinates**](Coordinates.md) |  | 


#### GeopropertySchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TimerelSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Timerel**](Timerel.md) |  | 


#### TimepropertySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


#### TimeSchema

Type | Description | Notes
------------- | ------------- | -------------
**datetime** |  | 

#### EndTimeSchema

Type | Description | Notes
------------- | ------------- | -------------
**datetime** |  | 

#### CsfSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### LimitSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["temporalValues", "sysAttrs", ]

#### LastNSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | OK
400 | ApiResponseFor400 | Bad request

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporalList**](EntityTemporalList.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporalList**](EntityTemporalList.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**EntityTemporalList**](EntityTemporalList.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity_temporal_attr**
> remove_entity_temporal_attr(entity_idattr_id)



Attribute from Temporal Representation of Entity deletion

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
        'attrId': Name("_"),
    }
    try:
        api_response = api_instance.remove_entity_temporal_attr(
            path_params=path_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->remove_entity_temporal_attr: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 
attrId | AttrIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content.
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity_temporal_attr_instance**
> remove_entity_temporal_attr_instance(entity_idattr_idinstance_id)



Attribute Instance deletion by instance id.

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
        'attrId': Name("_"),
        'instanceId': "instanceId_example",
    }
    try:
        api_response = api_instance.remove_entity_temporal_attr_instance(
            path_params=path_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->remove_entity_temporal_attr_instance: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 
attrId | AttrIdSchema | | 
instanceId | InstanceIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### AttrIdSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


#### InstanceIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content.
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity_temporal_by_id**
> remove_entity_temporal_by_id(entity_id)



Removes the temporal representation of an Entity from an NGSI-LD system

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.remove_entity_temporal_by_id(
            path_params=path_params,
            query_params=query_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->remove_entity_temporal_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
        'type': Name("_"),
    }
    try:
        api_response = api_instance.remove_entity_temporal_by_id(
            path_params=path_params,
            query_params=query_params,
        )
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->remove_entity_temporal_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
type | TypeSchema | | optional


#### TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | ApiResponseFor204 | No Content. The entity was removed successfully
400 | ApiResponseFor400 | Bad Request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



void (empty response body)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity_temporal_by_id**
> EntityTemporal retrieve_entity_temporal_by_id(entity_id)



Retrieve the temporal representation of an specific Entity from an NGSI-LD system. It's possible to specify the Entity attributes to be retrieved by using query parameters

### Example

```python
import ngsi_ld_client
from ngsi_ld_client.api import temporal_evolution_api
from ngsi_ld_client.model.entity_temporal import EntityTemporal
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.timerel import Timerel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ngsi_ld_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with ngsi_ld_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temporal_evolution_api.TemporalEvolutionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.retrieve_entity_temporal_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->retrieve_entity_temporal_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'entityId': "entityId_example",
    }
    query_params = {
        'attrs': "attrs_example",
        'type': Name("_"),
        'options': "temporalValues",
        'timerel': Timerel("before"),
        'timeproperty': Name("_"),
        'time': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
        'lastN': 1,
    }
    try:
        api_response = api_instance.retrieve_entity_temporal_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except ngsi_ld_client.ApiException as e:
        print("Exception when calling TemporalEvolutionApi->retrieve_entity_temporal_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/ld+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
attrs | AttrsSchema | | optional
type | TypeSchema | | optional
options | OptionsSchema | | optional
timerel | TimerelSchema | | optional
timeproperty | TimepropertySchema | | optional
time | TimeSchema | | optional
endTime | EndTimeSchema | | optional
lastN | LastNSchema | | optional


#### AttrsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

#### TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


#### OptionsSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  |  must be one of ["temporalValues", "sysAttrs", ]

#### TimerelSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Timerel**](Timerel.md) |  | 


#### TimepropertySchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Name**](Name.md) |  | 


#### TimeSchema

Type | Description | Notes
------------- | ------------- | -------------
**datetime** |  | 

#### EndTimeSchema

Type | Description | Notes
------------- | ------------- | -------------
**datetime** |  | 

#### LastNSchema

Type | Description | Notes
------------- | ------------- | -------------
**int** |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
entityId | EntityIdSchema | | 

#### EntityIdSchema

Type | Description | Notes
------------- | ------------- | -------------
**str** |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | ApiResponseFor200 | OK
400 | ApiResponseFor400 | Bad request
404 | ApiResponseFor404 | Not Found

#### ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporal**](EntityTemporal.md) |  | 


#### SchemaFor200ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityTemporal**](EntityTemporal.md) |  | 


#### ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, SchemaFor400ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor400ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, SchemaFor404ResponseBodyApplicationLdjson, ] |  |
headers | Unset | headers were not defined |

#### SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 


#### SchemaFor404ResponseBodyApplicationLdjson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProblemDetails**](ProblemDetails.md) |  | 



[**EntityTemporal**](EntityTemporal.md)

### Authorization

No authorization required

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

