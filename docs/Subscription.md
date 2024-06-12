# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription identifier (JSON-LD @id).  | [optional] 
**type** | **str** | JSON-LD @type.  | [optional] 
**subscription_name** | **str** | A (short) name given to this Subscription.  | [optional] 
**description** | **str** | Subscription description.  | [optional] 
**entities** | [**List[EntitySelector]**](EntitySelector.md) | Entities subscribed.  | [optional] 
**notification_trigger** | **List[str]** | The notification triggers listed indicate what kind of changes shall trigger a notification. If not present, the default is the combination attributeCreated and attributeUpdated. entityUpdated is equivalent to the combination attributeCreated, attributeUpdated and attributeDeleted.  | [optional] 
**q** | **str** | Query that shall be met by subscribed entities in order to trigger the notification.  | [optional] 
**geo_q** | [**GeoQuery**](GeoQuery.md) | Geoquery that shall be met by subscribed entities in order to trigger the notification.  | [optional] 
**csf** | **str** | Context source filter that shall be met by Context Source Registrations describing Context Sources to be used for Entity Subscriptions.  | [optional] 
**is_active** | **bool** | Allows clients to temporarily pause the subscription by making it inactive. true indicates that the Subscription is under operation. false indicates that the subscription is paused and notifications shall not be delivered.  | [optional] [default to True]
**notification** | [**NotificationParams**](NotificationParams.md) | Notification details.  | [optional] 
**expires_at** | **datetime** | Expiration date for the subscription.  | [optional] 
**temporal_q** | [**TemporalQuery**](TemporalQuery.md) | Temporal Query to be used only in Context Registration Subscriptions for matching Context Source Registrations of Context Sources providing temporal information.  | [optional] 
**scope_q** | **str** | Scope query.  | [optional] 
**lang** | **str** | Language filter to be applied to the query (clause 4.15).  | [optional] 
**system_generated_attrs** | [**SystemGeneratedAttributes**](SystemGeneratedAttributes.md) |  | [optional] 
**status** | **str** | Read-only. Provided by the system when querying the details of a subscription.  | [optional] [readonly] 
**jsonld_context** | **str** | The dereferenceable URI of the JSON-LD @context to be used when sending  a notification resulting from the subscription. If not provided, the @context used for the subscription shall be used as a default.  | [optional] 
**watched_attributes** | **List[str]** | Watched Attributes (Properties or Relationships). If not defined it means any Attribute.  | [optional] 
**throttling** | **float** | Minimal period of time in seconds which shall elapse between two consecutive notifications.  | [optional] 
**time_interval** | **float** | Indicates that a notification shall be delivered periodically regardless of attribute changes. Actually, when the time interval (in seconds) specified in this value field is reached.  | [optional] 

## Example

```python
from ngsi_ld_client.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


