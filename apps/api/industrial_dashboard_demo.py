from fastapi import APIRouter, Response
import time

router = APIRouter()

@router.get("/api/data-sources")
def get_data_sources():
    return [
        {
            "name": "EEG Neural Monitor Array",
            "status": "critical",
            "records": 154404,
            "size_gb": 23.4,
            "throughput": "2.4 MB/s",
            "location": "Lab Station A-1",
            "health": 98,
            "uptime": 99.97,
            "error_rate": 0.3,
            "last_updated": "just now",
            "state": "active"
        },
        {
            "name": "Industrial Audio Processor",
            "status": "high",
            "records": 89760,
            "size_gb": 18.7,
            "throughput": "1.8 MB/s",
            "location": "Production Floor B-2",
            "health": 95,
            "uptime": 99.95,
            "error_rate": 0.5,
            "last_updated": "5 seconds ago",
            "state": "active"
        },
        {
            "name": "Neural Pattern Recognition Engine",
            "status": "critical",
            "records": 235984,
            "size_gb": 42.1,
            "throughput": "3.2 MB/s",
            "location": "AI Processing Center",
            "health": 99,
            "uptime": 99.99,
            "error_rate": 0.1,
            "last_updated": "4 seconds ago",
            "state": "collecting"
        },
        {
            "name": "Environmental Sensor Network",
            "status": "medium",
            "records": 54320,
            "size_gb": 8.9,
            "throughput": "512 KB/s",
            "location": "Facility Wide",
            "health": 92,
            "uptime": 99.85,
            "error_rate": 1.5,
            "last_updated": "10 seconds ago",
            "state": "active"
        },
        {
            "name": "High-Frequency Audio Spectrometer",
            "status": "high",
            "records": 12340,
            "size_gb": 2.1,
            "throughput": "0 MB/s",
            "location": "Lab Station C-3",
            "health": 45,
            "uptime": 97.12,
            "error_rate": 28.5,
            "last_updated": "2 minutes ago",
            "state": "error"
        },
        {
            "name": "Industrial Vibration Sensors",
            "status": "medium",
            "records": 78560,
            "size_gb": 12.3,
            "throughput": "0 MB/s",
            "location": "Machine Shop D-1",
            "health": 0,
            "uptime": 95.67,
            "error_rate": 0.0,
            "last_updated": "1 hour ago",
            "state": "maintenance"
        }
    ]

@router.get("/api/activity-log")
def get_activity_log():
    return [
        {"time": "13:03:33", "type": "Collection", "source": "System Controller", "message": "Bulk data collection initiated successfully"},
        {"time": "13:02:53", "type": "Detection", "source": "Neural Pattern Engine", "message": "High-frequency pattern detected in sector 7"},
        {"time": "13:02:48", "type": "Network", "source": "Audio Spectrometer", "message": "Connection timeout - attempting reconnection"},
        {"time": "13:02:41", "type": "Backup", "source": "EEG Monitor Array", "message": "Data backup completed successfully"},
        {"time": "13:02:35", "type": "Storage", "source": "System Controller", "message": "Storage usage exceeded 75% threshold"}
    ]

@router.post("/api/start-bulk-collection")
def start_bulk_collection():
    time.sleep(1)
    return {"success": True, "message": "Bulk data collection initiated successfully"}

@router.get("/api/performance-metrics")
def get_performance_metrics():
    return {
        "cpu_usage": 72.9,
        "storage_used_tb": 1.8,
        "storage_total_tb": 2.4,
        "storage_percent": 75.0,
        "network_throughput": 45.2,
        "network_percent": 60.0,
        "error_rate": 0.12,
        "system_load": 72.9,
        "connections": 19,
        "data_rate": 8.4
    }

@router.get("/api/system-status")
def get_system_status():
    return {
        "core_services": "Operational",
        "network": "Connected",
        "maintenance": "Scheduled",
        "data_integrity": "Verified"
    }

@router.get("/api/storage-alert")
def get_storage_alert():
    return {
        "active": True,
        "message": "Storage usage has exceeded 75% capacity. Consider archiving older data."
    }

@router.get("/api/audio-spectrometer-error")
def get_audio_spectrometer_error():
    return {
        "active": True,
        "message": "Audio Spectrometer connection failed. Check network configuration."
    }
