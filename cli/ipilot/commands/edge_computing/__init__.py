"""Edge computing commands."""

from .content_delivery_network import app as content_delivery_network_app
from .edge_computing import app as edge_computing_app
from .edge_functions import app as edge_functions_app
from .internet_of_things import app as internet_of_things_app
from .lora_wan import app as lora_wan_app
from .mesh import app as mesh_app
from .ml import app as ml_app
from .pipeline import app as pipeline_app

__all__ = ["content_delivery_network_app", "edge_computing_app", "edge_functions_app", "internet_of_things_app", "lora_wan_app", "mesh_app", "ml_app", "pipeline_app"]
