from fastapi import APIRouter, Request, Response, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import Response
import cbor2
from typing import List, Dict, Any
import asyncio
import json
from datetime import datetime

router = APIRouter(prefix="/api/alba", tags=["ALBA Data Collection"])

# Simulated EEG data streams
active_streams = {}
stream_configs = {}

@router.get("/status")
async def alba_status():
    """Get ALBA module status"""
    return {
        "module": "ALBA",
        "status": "active",
        "streams_count": len(active_streams),
        "streams": list(active_streams.keys()),
        "data_collection": "running",
        "timestamp": datetime.now().isoformat()
    }

# Endpoint GET: Kthen CBOR
@router.get("/alba/cbor", response_class=Response)
async def get_cbor():
    data = {"status": "ok", "timestamp": "2025-10-09", "module": "alba"}
    cbor_bytes = cbor2.dumps(data)
    return Response(content=cbor_bytes, media_type="application/cbor")

# Endpoint POST: Pranon CBOR
@router.post("/alba/cbor", response_class=Response)
async def post_cbor(request: Request):
    body = await request.body()
    try:
        data = cbor2.loads(body)
        response = {"received": True, "data": data}
        cbor_bytes = cbor2.dumps(response)
        return Response(content=cbor_bytes, media_type="application/cbor")
    except Exception as e:
        error = {"error": str(e)}
        cbor_bytes = cbor2.dumps(error)
        return Response(content=cbor_bytes, media_type="application/cbor", status_code=400)

@router.post("/streams/start")
async def start_data_stream(stream_config: Dict[str, Any]):
    """Start a new data collection stream"""
    stream_id = stream_config.get("stream_id", f"stream_{len(active_streams) + 1}")
    
    active_streams[stream_id] = {
        "config": stream_config,
        "start_time": datetime.now(),
        "data_points": 0,
        "status": "active"
    }
    
    return {
        "message": f"Stream {stream_id} started successfully",
        "stream_id": stream_id,
        "status": "active"
    }

@router.post("/streams/{stream_id}/stop")
async def stop_data_stream(stream_id: str):
    """Stop a data collection stream"""
    if stream_id not in active_streams:
        raise HTTPException(status_code=404, detail="Stream not found")
    
    active_streams[stream_id]["status"] = "stopped"
    active_streams[stream_id]["end_time"] = datetime.now()
    
    return {
        "message": f"Stream {stream_id} stopped",
        "stream_id": stream_id,
        "status": "stopped"
    }

@router.get("/streams")
async def get_active_streams():
    """Get all active data streams"""
    return {
        "active_streams": active_streams,
        "total_streams": len(active_streams)
    }

@router.get("/streams/{stream_id}/data")
async def get_stream_data(stream_id: str, limit: int = 100):
    """Get collected data from specific stream"""
    if stream_id not in active_streams:
        raise HTTPException(status_code=404, detail="Stream not found")
    
    # Simulated EEG data
    simulated_data = {
        "stream_id": stream_id,
        "data_points": [
            {
                "timestamp": datetime.now().isoformat(),
                "channel_1": 0.5 + 0.1 * i,
                "channel_2": 0.3 + 0.05 * i,
                "channel_3": 0.7 + 0.02 * i,
                "signal_quality": 0.95 - 0.01 * i
            }
            for i in range(min(limit, 50))
        ],
        "metadata": active_streams[stream_id]
    }
    
    return simulated_data

@router.websocket("/ws/{stream_id}")
async def websocket_data_stream(websocket: WebSocket, stream_id: str):
    """WebSocket for real-time EEG data streaming"""
    await websocket.accept()
    
    try:
        while True:
            # Simulate real-time EEG data
            eeg_data = {
                "stream_id": stream_id,
                "timestamp": datetime.now().isoformat(),
                "channels": {
                    f"channel_{i}": 0.5 + 0.1 * (i % 8) for i in range(8)
                },
                "frequency_bands": {
                    "delta": 0.1 + 0.05 * (datetime.now().second % 10),
                    "theta": 0.2 + 0.08 * (datetime.now().second % 10),
                    "alpha": 0.3 + 0.12 * (datetime.now().second % 10),
                    "beta": 0.4 + 0.15 * (datetime.now().second % 10),
                    "gamma": 0.5 + 0.18 * (datetime.now().second % 10)
                },
                "signal_quality": 0.95
            }
            
            await websocket.send_json(eeg_data)
            await asyncio.sleep(0.1)  # 10Hz data rate
            
    except WebSocketDisconnect:
        print(f"WebSocket disconnected for stream {stream_id}")

@router.post("/config")
async def update_collection_config(config: Dict[str, Any]):
    """Update data collection configuration"""
    global stream_configs
    stream_configs.update(config)
    
    return {
        "message": "Configuration updated",
        "new_config": stream_configs
    }

@router.get("/metrics")
async def get_collection_metrics():
    """Get data collection metrics"""
    total_data_points = sum(stream["data_points"] for stream in active_streams.values())
    active_streams_count = len([s for s in active_streams.values() if s["status"] == "active"])
    
    return {
        "total_data_points": total_data_points,
        "active_streams": active_streams_count,
        "total_streams": len(active_streams),
        "data_rate_Hz": 256,  # Standard EEG sampling rate
        "storage_usage_mb": total_data_points * 0.001,  # Simulated
        "uptime_hours": 24  # Simulated
    }

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "module": "ALBA",
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }
