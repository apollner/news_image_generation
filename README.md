# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Ex-FBI officials worry that Kash Patel as director may wield unlimited power**

You can read more about it [here](https://news.google.com/rss/articles/CBMie0FVX3lxTE5RZUkwRHZUUTNkWnFkTEEzdGxrdTlHVEM1NHBDSTItLWxLSnBVUzFxRnNWODI2dUhyVlZfVmNzUDJZdDQwdkkxRGNxZl91Umk3TlcyUFlmMFc2U01CZ0RpRWxCYlhGWUd5WFhPZnBtZnV5endWRV9NRkI5MNIBe0FVX3lxTE1MbmtReG51NjJ3Y2xrOG0tTFE4cXVHb1poX3JjTEFHSmU1YXl2X0NMY29oX2RkMHprREp3TThJbE5GSl9vbFp3MlYzc1FCX01zNHQ4UV9HM0tOc0N0Q0xnc3JzcFZTcjhGRjBMYnBwTHpqRF94My0yTHpBUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
