# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**White House releases letter from Biden's doctor after questions about Parkinson's specialist's White House visits**

You can read more about it [here](https://news.google.com/rss/articles/CBMiXWh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3Mvd2hpdGUtaG91c2UtYnJpZWZpbmcta2FyaW5lLWplYW4tcGllcnJlLWJpZGVuLXBhcmtpbnNvbnMtZG9jdG9yL9IBYWh0dHBzOi8vd3d3LmNic25ld3MuY29tL2FtcC9uZXdzL3doaXRlLWhvdXNlLWJyaWVmaW5nLWthcmluZS1qZWFuLXBpZXJyZS1iaWRlbi1wYXJraW5zb25zLWRvY3Rvci8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
