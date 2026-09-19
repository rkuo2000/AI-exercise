from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import requests

# 1. Load a real Vision Transformer model and its image processor
model_name = "google/vit-base-patch16-224"
processor = ViTImageProcessor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# 2. Get your image (can be a local file path or a URL)
#url = "http://cocodataset.org"
#image = Image.open(requests.get(url, stream=True).raw)
image = Image.open("./image/taxi.jpg")

# 3. Preprocess the image (resizes, normalizes, and converts to tensors)
inputs = processor(images=image, return_tensors="pt")

# 4. Forward pass through the model
outputs = model(**inputs)
logits = outputs.logits

# 5. Extract the predicted class
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])

