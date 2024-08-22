# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tom Brady, Peyton Manning mostly agree on the top quarterbacks in the NFL, with 1 exception**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxQNFdQSlZFMUpzSE5taVNJc191eEQ2eVRZZm1faEdmcjEzc0RuTkRPd0VQZ0NSY3EwMzUtWjJRNVM4bXBER05fSTJZdG90cG9faU9Kd0g1TmZBWXVrUDJ5ZlBFOGpBLU9BWWdZc3hXTWphOEU2bWpoUXNlRGFlNHR6eUlic3U2QlBIYWd6dXRwSUluN3hMcDgtRFBsbVN5U255dVFhWDROa1d0M1cxS3J5b2NQamhfYWlyakVyS0FIT1hKcTBjNTBuRQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
