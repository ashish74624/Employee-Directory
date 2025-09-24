from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

def configure_opentelemetry(service_name: str = "employee"):
    resource = Resource.create({"service.name": service_name})

    # Create tracer provider
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    # Instrument Django
    DjangoInstrumentor().instrument()

    # Inject trace_id/span_id into logs
    LoggingInstrumentor().instrument(set_logging_format=False)

    # --- Force a root span for non-HTTP contexts (shell, startup, etc.) ---
    tracer = trace.get_tracer(service_name)
    global _root_span_ctx
    _root_span_ctx = tracer.start_as_current_span("startup-root-span")
    _root_span_ctx.__enter__()
