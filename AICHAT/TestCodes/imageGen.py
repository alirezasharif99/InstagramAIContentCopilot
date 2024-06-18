from diffusers import StableDiffusionPipeline
import torch

# Initialize the model
model_id = "runwayml/stable-diffusion-v1-5"

# Try changing the precision to float32
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

# Move the model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

# Set a text prompt
prompt = "a photo of Fcbayern Player"

# Generate an image
image = pipe(prompt).images[0]

# Save the image to a file
image.save("bayern.png")
