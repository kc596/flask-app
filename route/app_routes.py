from controller.health_check import health_check
from controller.kafka_stats import kafka_stats
from route.model import Route

# Define endpoints here...
routes = (
    Route(path="/status", methods=["GET", "POST"], controller=health_check),
    Route(path="/stats/kafka", methods=["GET", "POST"], controller=kafka_stats)
)
