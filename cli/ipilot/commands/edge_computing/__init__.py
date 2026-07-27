"""Edge computing commands."""

from .content_delivery_network import app as content_delivery_network_app
from .edge_computing import app as edge_computing_app
from .edge_functions import app as edge_functions_app
from .internet_of_things import app as internet_of_things_app
from .lora_wan import app as lora_wan_app
from .mesh_networking import app as mesh_networking_app
from .machine_learning import app as machine_learning_app
from .data_pipeline import app as data_pipeline_app

__all__ = ["content_delivery_network_app", "edge_computing_app", "edge_functions_app", "internet_of_things_app", "lora_wan_app", "mesh_networking_app", "machine_learning_app", "data_pipeline_app"]
