import pandas as pd


def generate_report(incident, logs_df):
    incident_id = incident["incident_id"]
    start_time = incident["start_time"]
    severity = incident["severity"]
    affected_services = incident["affected_services"]
    suspected_type = incident["suspected_incident_type"]

    report = f"""
# CortexOps Incident Report

## Incident ID
{incident_id}

## Severity
{severity}

## Suspected Incident Type
{suspected_type}

## Affected Services
{affected_services}

## Summary
CortexOps detected a {severity.lower()} severity incident involving {len(affected_services)} services.
The suspected issue is related to {suspected_type.replace("_", " ")}.

## Initial Reasoning
The system observed multiple anomalies within the same time window.
Affected services showed abnormal metrics such as latency spikes, CPU/memory pressure, error rate increases, retries, or queue growth.

## Recommended Next Steps
- Check logs for the first affected service.
- Inspect latency and error rate trends.
- Review recent deployments.
- Check database/cache availability if downstream services are affected.
- Monitor whether the anomaly continues in the next time window.
"""
    return report


if __name__ == "__main__":
    incidents = pd.read_csv("data/processed/incidents.csv")
    logs = pd.read_csv("data/processed/anomalies.csv")

    if incidents.empty:
        print("No incidents found.")
    else:
        for _, incident in incidents.iterrows():
            report = generate_report(incident, logs)
            output_path = f"outputs/reports/{incident['incident_id']}.md"

            with open(output_path, "w") as f:
                f.write(report)

            print(f"Generated report: {output_path}")