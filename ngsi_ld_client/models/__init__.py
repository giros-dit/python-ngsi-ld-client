# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from ngsi_ld_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from ngsi_ld_client.model.batch_entity_error import BatchEntityError
from ngsi_ld_client.model.batch_operation_result import BatchOperationResult
from ngsi_ld_client.model.context_source_registration import ContextSourceRegistration
from ngsi_ld_client.model.context_source_registration_fragment import ContextSourceRegistrationFragment
from ngsi_ld_client.model.context_source_registration_list import ContextSourceRegistrationList
from ngsi_ld_client.model.coordinates import Coordinates
from ngsi_ld_client.model.created_at import CreatedAt
from ngsi_ld_client.model.dataset_id import DatasetId
from ngsi_ld_client.model.endpoint import Endpoint
from ngsi_ld_client.model.entity import Entity
from ngsi_ld_client.model.entity_fragment import EntityFragment
from ngsi_ld_client.model.entity_info import EntityInfo
from ngsi_ld_client.model.entity_list import EntityList
from ngsi_ld_client.model.entity_temporal import EntityTemporal
from ngsi_ld_client.model.entity_temporal_fragment import EntityTemporalFragment
from ngsi_ld_client.model.entity_temporal_list import EntityTemporalList
from ngsi_ld_client.model.geo_json import GeoJSON
from ngsi_ld_client.model.geo_property import GeoProperty
from ngsi_ld_client.model.geo_query import GeoQuery
from ngsi_ld_client.model.geometry import Geometry
from ngsi_ld_client.model.georel import Georel
from ngsi_ld_client.model.instance_id import InstanceId
from ngsi_ld_client.model.ld_context import LdContext
from ngsi_ld_client.model.line_string import LineString
from ngsi_ld_client.model.linear_ring import LinearRing
from ngsi_ld_client.model.model_property import ModelProperty
from ngsi_ld_client.model.modified_at import ModifiedAt
from ngsi_ld_client.model.multi_line_string import MultiLineString
from ngsi_ld_client.model.multi_point import MultiPoint
from ngsi_ld_client.model.multi_polygon import MultiPolygon
from ngsi_ld_client.model.name import Name
from ngsi_ld_client.model.not_updated_details import NotUpdatedDetails
from ngsi_ld_client.model.notification_params import NotificationParams
from ngsi_ld_client.model.observed_at import ObservedAt
from ngsi_ld_client.model.point import Point
from ngsi_ld_client.model.polygon import Polygon
from ngsi_ld_client.model.position import Position
from ngsi_ld_client.model.position_array import PositionArray
from ngsi_ld_client.model.problem_details import ProblemDetails
from ngsi_ld_client.model.registration_info import RegistrationInfo
from ngsi_ld_client.model.relationship import Relationship
from ngsi_ld_client.model.subscription import Subscription
from ngsi_ld_client.model.subscription_fragment import SubscriptionFragment
from ngsi_ld_client.model.subscription_list import SubscriptionList
from ngsi_ld_client.model.time_interval import TimeInterval
from ngsi_ld_client.model.timerel import Timerel
from ngsi_ld_client.model.update_result import UpdateResult
