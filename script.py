import os
from PIL import Image
import matplotlib.pyplot as plt
from diffusers import StableDiffusionPipeline
import torch
from transformers import pipeline
import matplotlib.pyplot as plt
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration
import numpy as np

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-large").to("cuda")

# Check if the prompt file exists
if os.path.exists('prompt.txt'):
    # If the prompt file exists, read the prompt from the file
    with open('prompt.txt', 'r') as f:
        prompt = f.read().strip()
else:
    # If the prompt file does not exist, use a default prompt
    prompt = "Live updates: SpaceX targeting late Florida launch of Starlink satellites"

# Generate an image from the prompt
image = pipe(prompt).images[0]

# Generate a prompt from the image
inputs = processor(image, return_tensors="pt").to("cuda")
out = model.generate(**inputs)
prompt = (processor.decode(out[0], skip_special_tokens=True))

# Save the prompt to a file
with open('prompt.txt', 'w') as f:
    f.write(prompt)

# Save the image to a file
plt.imsave('image.png', image)

# Update the README file
with open('README.md', 'w') as f:
    f.write(f'![Generated Image](image.png)\n\nPrompt: {prompt}')
