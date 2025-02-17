curl -X 'POST' \
  'http://127.0.0.1:8000/alert' \
  -H 'Content-Type: application/json' \
  -d '{
    "receiver": "webhook",
    "status": "firing",
    "alerts": [
      {
        "status": "firing",
        "labels": {
          "alertname": "HighCpuUsage",
          "instance": "node-exporter:9100",
          "ip": "node-exporter:9100",
          "severity": "critical",
          "project": "ai",
          "app": "mysql"
        },
        "annotations": {
          "summary": "CPU usage on node-exporter:9100 is above 60%"
        },
        "startsAt": "2025-02-17T06:45:18.626Z",
        "endsAt": "0001-01-01T00:00:00Z",
        "generatorURL": "http://c1ce1b51015b:9090/graph?g0.expr=%28100+-+%28avg+by+%28instance%29+%28rate%28node_cpu_seconds_total%7Bmode%3D%22idle%22%7D%5B1m%5D%29%29+%2A+100%29%29+%3E+60&g0.tab=1",
        "fingerprint": "07c3678ba294ed9f"
      }
    ],
    "groupLabels": {
      "alertname": "HighCpuUsage"
    },
    "commonLabels": {
      "alertname": "HighCpuUsage",
      "instance": "node-exporter:9100",
      "ip": "node-exporter:9100",
      "severity": "critical"
    },
    "commonAnnotations": {
      "summary": "CPU usage on node-exporter:9100 is above 60%"
    },
    "externalURL": "http://0737428618ea:9093",
    "version": "4",
    "groupKey": "{}:{alertname=\"HighCpuUsage\"}",
    "truncatedAlerts": 0
  }'


