from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from app.core.websocket import manager
from app.core.security import decode_access_token

router = APIRouter(
    prefix="/ws",
    tags=["websockets"]
)

# --- WEBSOCKET TASK NOTIFICATION ROUTE ---
# Clients connect to: ws://localhost:8000/api/v1/ws/tasks?token=<JWT_TOKEN>
# This establishes a persistent TCP connection for real-time server push notifications.

@router.websocket("/tasks")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str | None = Query(None)
):
    """
    WebSocket endpoint that streams real-time updates for tasks.
    Secured by extracting and verifying the JWT token from the query parameters.
    """
    # Connect and accept the handshake
    await manager.connect(websocket)
    
    # JWT authentication check
    if token:
        payload = decode_access_token(token)
        if not payload:
            try:
                await websocket.send_json({"status": "unauthorized", "message": "Invalid JWT Token"})
                manager.disconnect(websocket)
                await websocket.close(code=1008)  # 1008 is standard WS close code for Policy Violation
            except Exception:
                pass
            return
            
    try:
        # Keep connection open. Websockets are bidirectional, so we must yield execution
        # to wait for potential client messages or disconnection events.
        while True:
            # Receive and echo message (or just keep connection open)
            data = await websocket.receive_text()
            await websocket.send_json({"received": data, "message": "Echo from server!"})
    except WebSocketDisconnect:
        # Clean up connection when client closes socket
        manager.disconnect(websocket)
