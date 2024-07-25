# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock market news today: Stocks smoked, Nasdaq falls over 3.5% in worst day since 2022 after Tesla, Alphabet trigger Big Tech sell-off**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgJBVV95cUxNXzAzOVNEdURaUEtfa3R3UmlVTjdSblpTaW13MXR6MDJwN2dFS1hvNWVVLWZ1LUlUa3FmRWs3NFcxa2F2NXA1QmxLVGR6ajRUSk1EVEZyeVM3OG9MY01DUkhTV2RnemUzS1hCaURIMWwxeUZ0cTNBUEZyMl82dmNIVDMxbUc4VUtXeTNjeFNkb24yeXEwVmdVVmpDXzNVWWViM0hBdllod2xHT2FuN0lSTkFyRUZTWjRmMENZQThodi10cGJyUjFWelEtY3c3TWRqLWl1MjJqYWltVlMyOGl0VTR2d3RCLWE4QXhzLU5lZUFlWmM5Y0plbWh0MjNyZGdRdXlzMmJ3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
