# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Federal Judge Grants Fubo Request to Block Disney, Fox, Warner Bros. Discovery Sports Bundle**

You can read more about it [here](https://news.google.com/rss/articles/CBMieEFVX3lxTFB3ZFpmNHJ3TGx5dzBTQk5aOEhabFJ3ZV9zTDBFYjdpUkhONEZLLUFCaEE3M05XX3hLZTFKbWUzcFNxNnZPNVJZcm5NTlVJaDNjamhHdUN5LWd6LTZRU1JtUHNBQ2l0WGJhWXJVS3RXb215R2k2V3VYRg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
