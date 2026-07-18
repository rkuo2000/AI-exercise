# !pip install openai
import base64
from openai import OpenAI

client = OpenAI(
#        base_url='http://192.168.0.22:11434/v1',
        base_url='http://localhost:11434/v1',
        api_key="ollama"
)

def encode_image(image_path):
    """Reads a local image file and converts it to a base64 string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Path to your local image (e.g., JPEG or PNG)
image_path = "./image/LaTeX_ocr.png"

# Get the base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model='gemma4-turbo-128k:e2b',        
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "What is inside this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
)

result = response.choices[0].message.content
print(result)
