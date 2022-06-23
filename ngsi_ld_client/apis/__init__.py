# coding: utf-8

# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from ngsi_ld_client.api.batch_operations_api import BatchOperationsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ngsi_ld_client.api.batch_operations_api import BatchOperationsApi
from ngsi_ld_client.api.c_source_registrations_api import CSourceRegistrationsApi
from ngsi_ld_client.api.c_source_subscriptions_api import CSourceSubscriptionsApi
from ngsi_ld_client.api.context_information_api import ContextInformationApi
from ngsi_ld_client.api.context_sources_api import ContextSourcesApi
from ngsi_ld_client.api.context_subscription_api import ContextSubscriptionApi
from ngsi_ld_client.api.entities_api import EntitiesApi
from ngsi_ld_client.api.subscriptions_api import SubscriptionsApi
from ngsi_ld_client.api.temporal_api import TemporalApi
from ngsi_ld_client.api.temporal_evolution_api import TemporalEvolutionApi
