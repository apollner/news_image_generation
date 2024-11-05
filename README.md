# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**What life is like in one of the most remote places on Earth**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxOWEZBZUNZUi1Hay00OTVmN3h5blpxalZIMlFKdGJPQWlhMkNPR0lKS3BWUjlkVzBuZEV5elYwa1FSQ1VhY01NQjdvYzBfVGxsT2pPSWdORVFlSC1XM0NISzhXR3BwWHVpZXpaSUZEOFY3YjNhdTlXTzFhRG1NNEJQWFBtbXlfa2t1TVBMMG84UUJxQdIBiAFBVV95cUxOcGZUem9yVExaTWxVU2Q5VzFTNVR5alFDSHFMSXhacFBnZkdtZkFpMU5TVVk3OVhjQ3dJaF9USGhIMl93TG83Vlh1ZG1hZzdYQ1dPNTMzbC1DZ0dxbFNnT2hPUmpmb1J3NVg3MjhXY1F2NUc1eGhMU3RCbTQ1SWtjZTkzUENUa3lf?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
