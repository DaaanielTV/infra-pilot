import typer

app = typer.Typer(help="Customer experience")

from .health import app as cx_health_app
from .ticket import app as cx_ticket_app
from .sla import app as cx_sla_app
from .canned_responses import app as canned_responses_app
from .sentiment import app as sentiment_app
from .adoption import app as adoption_app
from .onboarding import app as onboarding_app
from .kb import app as kb_app
from .community import app as community_app
from .communications import app as communications_app
from .nps import app as nps_app
from .success import app as success_app

app.add_typer(cx_health_app, name="health")
app.add_typer(cx_ticket_app, name="ticket")
app.add_typer(cx_sla_app, name="sla")
app.add_typer(canned_responses_app, name="canned")
app.add_typer(sentiment_app, name="sentiment")
app.add_typer(adoption_app, name="adoption")
app.add_typer(onboarding_app, name="onboarding")
app.add_typer(kb_app, name="kb")
app.add_typer(community_app, name="community")
app.add_typer(communications_app, name="comm")
app.add_typer(nps_app, name="nps")
app.add_typer(success_app, name="success")