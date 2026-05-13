import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np


SERVICES = [
    "api-gateway",
    "auth-service",
    "payment-service",
    "notification-service",
    "inventory-service",
    "recommendation-engine",
    "database",
    "cache-layer",
]


INCIDENT_TYPES = [
    "normal",
    "database_slowdown",
    "cache_failure",
    "memory_leak",
    "traffic_spike",
    "authentication_outage",
]


def generate_log_event(timestamp, service, incident_type="normal"):
    base_latency = {
        "api-gateway": 120,
        "auth-service": 90,
        "payment-service": 150,
        "notification-service": 100,
        "inventory-service": 130,
        "recommendation-engine": 180,
        "database": 80,
        "cache-layer": 40,
    }

    latency = np.random.normal(base_latency[service], 20)
    cpu_usage = np.random.normal(45, 10)
    memory_usage = np.random.normal(55, 12)
    error_rate = np.random.normal(0.01, 0.01)
    request_count = int(np.random.normal(500, 80))
    retry_count = int(max(0, np.random.normal(2, 2)))
    queue_size = int(max(0, np.random.normal(10, 5)))

    level = "INFO"
    message = "Service operating normally"

    if incident_type == "database_slowdown" and service in ["database", "payment-service", "api-gateway"]:
        latency *= random.uniform(3, 8)
        cpu_usage += random.uniform(20, 40)
        error_rate += random.uniform(0.05, 0.2)
        retry_count += random.randint(5, 20)
        level = "ERROR" if service != "database" else "WARNING"
        message = "High latency detected due to database slowdown"

    elif incident_type == "cache_failure" and service in ["cache-layer", "api-gateway", "recommendation-engine"]:
        latency *= random.uniform(2, 5)
        error_rate += random.uniform(0.03, 0.15)
        retry_count += random.randint(3, 15)
        level = "ERROR"
        message = "Cache unavailable or slow response"

    elif incident_type == "memory_leak" and service in ["recommendation-engine", "payment-service"]:
        memory_usage += random.uniform(25, 45)
        latency *= random.uniform(1.5, 3)
        level = "WARNING"
        message = "Memory usage increasing abnormally"

    elif incident_type == "traffic_spike" and service in ["api-gateway", "auth-service"]:
        request_count *= random.randint(3, 6)
        latency *= random.uniform(1.5, 4)
        cpu_usage += random.uniform(15, 35)
        queue_size += random.randint(30, 100)
        level = "WARNING"
        message = "Traffic spike causing service pressure"

    elif incident_type == "authentication_outage" and service in ["auth-service", "api-gateway"]:
        error_rate += random.uniform(0.1, 0.3)
        latency *= random.uniform(2, 5)
        level = "ERROR"
        message = "Authentication failures detected"

    return {
        "timestamp": timestamp,
        "service": service,
        "level": level,
        "message": message,
        "latency_ms": round(max(latency, 1), 2),
        "cpu_usage": round(min(max(cpu_usage, 0), 100), 2),
        "memory_usage": round(min(max(memory_usage, 0), 100), 2),
        "error_rate": round(min(max(error_rate, 0), 1), 4),
        "request_count": max(request_count, 0),
        "retry_count": retry_count,
        "queue_size": queue_size,
        "incident_type": incident_type,
    }


def generate_logs(num_minutes=180, output_path="data/simulated/system_logs.csv"):
    start_time = datetime.now() - timedelta(minutes=num_minutes)
    logs = []

    incident_schedule = {
        45: "database_slowdown",
        90: "traffic_spike",
        130: "cache_failure",
        160: "memory_leak",
    }

    for minute in range(num_minutes):
        timestamp = start_time + timedelta(minutes=minute)

        incident_type = incident_schedule.get(minute, "normal")

        for service in SERVICES:
            event = generate_log_event(timestamp, service, incident_type)
            logs.append(event)

    df = pd.DataFrame(logs)
    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    df = generate_logs()
    print(f"Generated {len(df)} log events")
    print(df.head())