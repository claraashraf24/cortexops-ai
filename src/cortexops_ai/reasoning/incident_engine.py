import pandas as pd


def detect_incidents(df: pd.DataFrame, window_minutes=5) -> pd.DataFrame:
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    anomaly_df = df[df["is_anomaly"] == True].copy()

    incidents = []

    if anomaly_df.empty:
        return pd.DataFrame(incidents)

    anomaly_df["time_window"] = anomaly_df["timestamp"].dt.floor(f"{window_minutes}min")

    grouped = anomaly_df.groupby("time_window")

    incident_id = 1

    for time_window, group in grouped:
        affected_services = group["service"].unique().tolist()
        anomaly_count = len(group)

        if anomaly_count >= 3 or len(affected_services) >= 2:
            severity = "HIGH" if anomaly_count >= 8 else "MEDIUM"

            incidents.append({
                "incident_id": f"INC-{incident_id:03d}",
                "start_time": time_window,
                "severity": severity,
                "affected_services": affected_services,
                "anomaly_count": anomaly_count,
                "suspected_incident_type": group["incident_type"].mode()[0],
            })

            incident_id += 1

    return pd.DataFrame(incidents)


if __name__ == "__main__":
    df = pd.read_csv("data/processed/anomalies.csv")
    incidents = detect_incidents(df)
    incidents.to_csv("data/processed/incidents.csv", index=False)

    print("Incidents detected:")
    print(incidents)