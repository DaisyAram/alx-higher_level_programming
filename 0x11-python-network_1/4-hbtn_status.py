#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print(f"Body response:\n\t- type: {response.headers.get('Content-Type')}\n\t- content: {response.text}")
