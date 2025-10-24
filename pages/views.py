# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from django.http import HttpResponse, JsonResponse
import socket
import time
from datetime import datetime, timezone

def home_page_view(request):
    return HttpResponse("Hello, world")


def health(request):
    # GCP / k8s / uptime checks
    return HttpResponse("ok", status=200)

def lbheartbeat(request):
    return HttpResponse("ok", status=200)

def info(request):
    """Simple JSON info endpoint."""
    return JsonResponse({
        "service": "otel-django-demo",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "host": socket.gethostname(),
        "path": request.path,
    })


def slow(request):
    """Simulates a slow endpoint for tracing latency."""
    time.sleep(2)  # delay for 2 seconds
    return HttpResponse("slow response completed after 2s")


def error(request):
    """Intentional error route to demonstrate error tracing."""
    raise Exception("intentional demo error")