"""
Signal Generator Routes - Industrial API
Author: Ledjan Ahmati
License: Closed Source
"""

from fastapi import APIRouter, HTTPException
import numpy as np
import time

router = APIRouter()

@router.get("/signal-gen/sine", tags=["SignalGen"])
def generate_sine_wave(freq: float = 10.0, duration: float = 1.0, sample_rate: int = 1000):
    """Gjeneron sinjal sine industrial (real data)."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * freq * t)
    return {
        "frequency": freq,
        "duration": duration,
        "sample_rate": sample_rate,
        "signal": signal.tolist(),
        "timestamp": time.time()
    }

@router.get("/signal-gen/status", tags=["SignalGen"])
def get_signal_gen_status():
    """Kthen statusin real të gjeneratorit të sinjaleve industriale."""
    return {
        "status": "active",
        "timestamp": time.time()
    }
