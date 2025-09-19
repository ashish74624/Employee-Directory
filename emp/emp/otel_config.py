from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

def configure_opentelemetry(service_name: str = "employee"):
    resource = Resource.create({"service.name": service_name})

    # Just set tracer provider — no exporter!
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    # Instrument Django
    DjangoInstrumentor().instrument()

    # Inject trace_id/span_id into logs (no JSON, no exporter spam)
    LoggingInstrumentor().instrument(set_logging_format=False)
