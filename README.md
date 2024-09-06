# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Friday’s jobs report will likely determine the size of the Fed’s rate cut**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxNWDZ1UXZWV0NqNEh4bTBGbnR1MzVXUVA3bVY4YkpsV1VpWVRWX3VWcFBPWllBcnA1Y21WZGgtQnllV0JjS0VxZ1hGZGZrQ1duZDNxQ0Z4Q2JnbGxZazQxamJ1OEZoS2N5YUdzSGM3N0E0NVBDcEg4N19lV09Fb0M3Z0NyeFp1d9IBfEFVX3lxTE16a1pDaE40dF9OSDZRMkxSYUZPNFFKY3NGRnNBbnZjX29Lc1FSX1RUUW41d1ZiMUswUlJFNzRuMXRWSkZNaEsyUjJaYXZCMWRRb0RyM3YtT2FVQVpyNXFqTzVLZ3RzcVgzV0JpUlBFd0Vtd1RwSV84WVVJalU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
