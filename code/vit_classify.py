import torch
from PIL import Image
from torchvision.models import ViT_B_16_Weights, vit_b_16

# 1. Load the pretrained weights and initialize the model
weights = ViT_B_16_Weights.DEFAULT
model = vit_b_16(weights=weights)
model.eval()  # Set the model to evaluation mode

# 2. Get the optimal preprocessing transforms associated with the weights
preprocess = weights.transforms()

# 3. Load a sample image (replace with your own image path)
# Note: ViT-B/16 standard input size is typically 224x224 pixels
img_path = "./image/taxi.jpg"
try:
  image = Image.open(img_path).convert("RGB")
except FileNotFoundError:
  # Creating a dummy image if file doesn't exist for demonstration
  image = Image.new("RGB", (224, 224), color="red")

# 4. Preprocess the image and add a batch dimension
batch = preprocess(image).unsqueeze(0)

# 5. Run inference
with torch.no_grad():
  prediction = model(batch)

# 6. Get the predicted category index and label
predicted_category = prediction.squeeze(0).softmax(dim=0).argmax().item()
label_name = weights.meta["categories"][predicted_category]

print(f"Predicted category index: {predicted_category}")
print(f"Predicted label: {label_name}")
