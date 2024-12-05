# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Georgian opposition politician beaten unconscious by police, party says, as government crackdown intensifies**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxQS2dpbFg3RDFlMmFHM0F5WkswdlEzaFdqeV9OdXJTTVlzQ24zNGxRZERPMUdqLVJnQjB4bW9OV0tnRlF3bXJ0ZmZkQ05Cak5BUjFTZnBPR2NmVTZkaVR3dVRQX3VXR1p5UVdJT2pyWTJoSG40T0I0NU1GUG5NSUZOMGhNYzZPRUNlTXpFbU1ZZC0xUdIBiAFBVV95cUxPYlpzRGxRWHdVOEk5NlNyUnJRdnVlXy1fNUd3UE44bXg4NHE5ZlJKRlJTTWY2M2hRNHA0bUEyQVdramxZY2ZGbTB1ZHU5RkpUMlBCM2xBcUUyNVk0ZGo4U09ualN0S1dNSjBILVVIcjZ5Qm5Kd256ZDNMMEZPMGZWZlBVc19nZm5q?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
