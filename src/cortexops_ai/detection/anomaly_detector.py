import pandas as pd


METRICS = [
    "latency_ms",
    "cpu_usage",
    "memory_usage",
    "error_rate",
    "request_count",
    "retry_count",
    "queue_size",
]


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["is_anomaly"] = False
    df["anomaly_reasons"] = ""

    for service in df["service"].unique():
        service_mask = df["service"] == service
        service_df = df[service_mask]

        for metric in METRICS:
            mean = service_df[metric].mean()
            std = service_df[metric].std()

            if std == 0:
                continue

            threshold = mean + 2.5 * std
            anomaly_mask = service_mask & (df[metric] > threshold)

            df.loc[anomaly_mask, "is_anomaly"] = True
            df.loc[anomaly_mask, "anomaly_reasons"] += f"{metric} above threshold; "

    return df


if __name__ == "__main__":
    logs = pd.read_csv("data/simulated/system_logs.csv")
    result = detect_anomalies(logs)
    result.to_csv("data/processed/anomalies.csv", index=False)

    print("Total logs:", len(result))
    print("Anomalies detected:", result["is_anomaly"].sum())
    print(result[result["is_anomaly"]].head())