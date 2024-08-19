# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Some India doctors stay off job after strike over colleague's rape and murder**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxQZXRqLXR6U01peDY0QkF1czI0c0ljcUVuLWYyZTE0eU1lRXdremxEVmRsRS1IQ0dLTGJIRW9uSkVGQi1ldU1jMFFYcEU3WmllajEtc0JYakJnbFdSWTR6bzJXRkxsX2JjenRGZ3dtYm11Z0V3YzRSbVBIM3pIbE1tUmUwLWczRjVLSDU4QnpOc0ZnelVOanA0UjZuQ21td1lEQTQtQmUzZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
