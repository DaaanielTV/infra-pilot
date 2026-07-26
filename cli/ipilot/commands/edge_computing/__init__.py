"""Edge computing commands."""

from .content_delivery_network import app as content_delivery_network_app
from .edge_computing import app as edge_computing_app
from .functions import app as fn_app
from .iot import app as iot_app
from .lorawan import app as gw_app
from .mesh import app as mesh_app
from .ml import app as ml_app
from .pipeline import app as pipeline_app

__all__ = ["content_delivery_network_app", "edge_computing_app", "fn_app", "iot_app", "gw_app", "mesh_app", "ml_app", "pipeline_app"]
