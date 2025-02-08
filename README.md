# Real-Time Data Visualization with WebSockets

This project demonstrates a real-time data visualization system that uses WebSockets to stream temperature and tire pressure data to a web-based dashboard. The temperature data comes from sensors, and the tire pressure monitoring system (TPMS) data is collected from vehicles. The real-time data is displayed through interactive charts using the [Chart.js](https://www.chartjs.org/) library.

## Features

- **Real-Time Data Visualization**: Display temperature (in Celsius) and tire pressure (in PSI) in real-time.
- **Interactive Charts**: Choose which sensor or vehicle to visualize the data from, and see the charts update live.
- **WebSocket Communication**: Data is streamed to the client using WebSockets, ensuring real-time updates.

## Installation

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/timdigga/rtl433websocket
cd rtl433websocket
```
Install the required Python dependencies:

```bash
pip install -r requirements.txt
```
3. Run the WebSocket Server
Start the WebSocket server to begin reading data from the sensors and broadcasting it to connected clients:

```bash
python websocket.py
```
The WebSocket server will start on ws://localhost:8765. You will see messages printed in the terminal for each received data signal.

4. Open the Web Dashboard
Open the index.html file in your web browser. You will see dropdowns to select sensors and vehicles, and the charts will update in real-time as data is received from the server.

WebSocket Data Format
The WebSocket server sends data in JSON format. Here’s an example of the data structure:

Temperature Data (Sensor)
{
    "time": "2025-02-08T12:34:56Z",
    "model": "Sensor A",
    "temperature_F": 72.5,
    "temperature_C": 22.5
}
TPMS Data (Vehicle)
{
    "time": "2025-02-08T12:34:56Z",
    "model": "Vehicle XYZ",
    "pressure_PSI": 32.1
}
The temperature_F field is converted to Celsius (temperature_C), and both temperature and pressure values are updated live.

Frontend Details
The front-end HTML page includes two sections:

Temperature Visualization: Displays the temperature data for a selected sensor.
TPMS Visualization: Displays the tire pressure data for a selected vehicle.
The real-time charts are powered by Chart.js, and they automatically update as new data is received via the WebSocket connection.

Dependencies
The backend server requires the following Python dependencies:

asyncio: For managing asynchronous I/O operations.
json: For parsing JSON data.
websockets: For setting up the WebSocket server and broadcasting data to clients.
To install the required Python packages, run:

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contributing
If you would like to contribute to this project, feel free to fork the repository and create a pull request with your improvements. Contributions are always welcome!

Author
Made by Tim Digga

Thank you for your support!
