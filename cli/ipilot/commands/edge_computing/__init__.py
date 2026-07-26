"""Edge computing commands."""

from .cdn import app as cdn_app
from .edge import app as edge_app
from .functions import app as fn_app
from .iot import app as iot_app
from .lorawan import app as gw_app
from .mesh import app as mesh_app
from .ml import app as ml_app
from .pipeline import app as pipeline_app

__all__ = ["cdn_app", "edge_app", "fn_app", "iot_app", "gw_app", "mesh_app", "ml_app", "pipeline_app"]
