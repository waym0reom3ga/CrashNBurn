#!/usr/bin/env python3
"""Test WebSocket connection to SDRconnect."""
import json
import websocket
import time

ws = websocket.create_connection("ws://127.0.0.1:5555")
time.sleep(0.5)

# Send get_property command
cmd = {"event_type": "get_property", "property": "can_control"}
ws.send(json.dumps(cmd))

# Wait for response
ws.settimeout(3.0)
try:
    msg = ws.recv()
    print(f"Response type: {type(msg)}")
    if isinstance(msg, str):
        data = json.loads(msg)
        print(f"Parsed: {data}")
    else:
        print(f"Binary ({len(msg)} bytes)")
except Exception as e:
    print(f"Error: {e}")

ws.close()
print("Done")
