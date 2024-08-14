# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**News outlets were leaked insider material from the Trump campaign. They chose not to print it**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxNallxb05HeXExU1JKUzJzeS15b2hGbkpwSDJUc096QV9XczB1TXdqS2ZORTZRbHc2YzhhZnh6VHphLThmNjFNdjBVcnM4T0lNT0NqM2oxeWxWUEJaMmdEdXhzQ2U0UzZSYl91RE5WV3diQU5pWFZlM2R0S2pZYVhKUlZKVDh6Wmx0VlFYd0RCMW5ZVnAtQjM4?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
