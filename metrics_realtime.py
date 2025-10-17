import psutil, datetime, random

def get_realtime_metrics():
    now = datetime.datetime.utcnow().isoformat()
    metrics = {
        "timestamp": now,
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "network_io": psutil.net_io_counters().bytes_sent,
        "active_nodes": random.randint(3, 10),
        "system_health": "optimal" if psutil.cpu_percent() < 85 else "high_load"
    }
    return metrics
