import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

invoke_url = "https://ai.api.nvidia.com/v1/vlm/nvidia/neva-22b"

with open("sequence-diagram.png", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()

assert len(image_b64) < 180_000, \
    "To upload larger images, use the assets API (see docs)"

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Accept": "application/json"
}

payload = {
    "messages": [
        {
            "role": "user",
            "content": f'What formula is presented on this image? <img src="data:image/png;base64,{image_b64}" />'
        }
    ],
    "max_tokens": 1024,
    "temperature": 0.20,
    "top_p": 0.20
}

response = requests.post(invoke_url, headers=headers, json=payload)

print(response.json())
