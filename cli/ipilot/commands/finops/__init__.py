import typer

app = typer.Typer(help="FinOps management")

from .commitment import app as commitment_app
from .spot import app as spot_app
from .uoe import app as uoe_app
from .anomaly import app as anomaly_app
from .budget import app as budget_app
from .rightsizing import app as rightsizing_app
from .waste import app as waste_app
from .carbon import app as carbon_app
from .arbitrage import app as arbitrage_app
from .reports import app as reports_app

app.add_typer(commitment_app, name="commitment")
app.add_typer(spot_app, name="spot")
app.add_typer(uoe_app, name="uoe")
app.add_typer(anomaly_app, name="anomaly")
app.add_typer(budget_app, name="budget")
app.add_typer(rightsizing_app, name="rightsizing")
app.add_typer(waste_app, name="waste")
app.add_typer(carbon_app, name="carbon")
app.add_typer(arbitrage_app, name="arbitrage")
app.add_typer(reports_app, name="reports")