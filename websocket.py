import asyncio
import json
import websockets

print("=================================")
print("==      Made by Tim Digga     ===")
print("=================================")
print("Thanks for your support!")
connected_clients = set()
signal_counter = 0

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

async def rtl433_reader():
    global signal_counter

    process = await asyncio.create_subprocess_exec(
        "rtl_433", "-F", "json",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    print("[+] Started rtl_433 process.")

    while True:
        line = await process.stdout.readline()
        if not line:
            break

        try:
            data = json.loads(line.decode("utf-8").strip())
            signal_counter += 1
        except json.JSONDecodeError:
            print("[-] Failed to decode JSON:", line)
            continue

        if "temperature_F" in data:
            data["temperature_C"] = fahrenheit_to_celsius(data["temperature_F"])

        message = json.dumps(data, indent=4)
        print(f"Signal #{signal_counter}:")
        print(message)

        websockets.broadcast(connected_clients, message)

    await process.wait()
    print("[-] No supported device found!")

async def websocket_handler(websocket, path):
    print(f"[+] Client connected from {websocket.remote_address} with path: {path}")
    connected_clients.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)
        print(f"[+] Client disconnected from {websocket.remote_address}")

async def main():
    asyncio.create_task(rtl433_reader())
    async with websockets.serve(websocket_handler, "localhost", 8765):
        print("[+] WebSocket server started on ws://localhost:8765")
        print("[+] You can now start the HTML File!")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[---] Server stopped by user.")
