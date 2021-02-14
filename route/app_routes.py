from controller.health_check import health_check
from route.model import Route

# Define endpoints here...
routes = (
    Route(path="/status", methods=["GET", "POST"], controller=health_check),
)
