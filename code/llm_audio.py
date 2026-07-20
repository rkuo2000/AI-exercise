# !pip install openai
import base64
from openai import OpenAI

client = OpenAI(
#        base_url='http://192.168.0.22:11434/v1',
        base_url='http://localhost:11434/v1',
        api_key="ollama"
)

def encode_audio(audio_path):
    """Reads a local audio file and converts it to a base64 string."""
    with open(audio_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode("utf-8")

# Path to your local audio (e.g., MP3 or WAV)
audio_path = "./audio/Trump.mp3"

# Get the base64 string
base64_audio = encode_audio(audio_path)

response = client.chat.completions.create(
    model='gemma4:e2b',        
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Transcribe this audio"
                },
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": base64_audio,
                        "format": "mp3"
                    }
                }
            ]
        }
    ]
)

result = response.choices[0].message.content
print(result)
