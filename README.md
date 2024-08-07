# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Biden convenes national security team as fears of Iran attack grow**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5TYTRRc3R2dDhLZXM1VWtqQ016NDVxclhxQkJTWlRsUFVUWS1WQ014SFdWZkZOUE5VRmFZT0VSUVZSZkNHY0xVTU9VODV6dW5VNV9CRlgzTlVid9IBX0FVX3lxTFB4RmRRUllnLWI0c2ZXbk9hYXVDQ2d4dTFMQkZXMkVISjA1NnkyVXJiRE1oOFFKRHB5M095ZWhDa0hBWm0xcGQ2bmdEMFR4ZlBqSXIwNXMyQ1FWZF9EazYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
