# Remote Server Health Check

A Python script to perform basic health checks on a remote Linux server via SSH using Paramiko.

## Features

- Connects to a remote server via SSH with a private key.
- Runs commands to check system uptime, CPU usage, memory, and disk usage.
- Saves the results as timestamped JSON files in an output folder.

## Requirements

- Python 3.x
- `paramiko` Python package (install with `pip install paramiko`)
- Access to the remote server with SSH key authentication

## Configuration

Edit the `health-check.py` file and update the following variables:

```python
HOST = "your.server.ip"
USERNAME = "your_username"
KEY_FILE = "path/to/your/private/key"
