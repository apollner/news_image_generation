# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Netanyahu is unequivocal about ceasefire and hostage agreement with Hamas: ‘There’s not a deal in the making’**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxPdkRqNFJJOUhXNkV3dnNRUS1aa05DbEp5a3RUMGhXdjV2Z0t5RzZWSGxIaE01Qm5hbFpfYzRCQXN1SmdfalBISnIyVFo2UEhNcmxOZ3NMZGNxa3BQajZuMFR4ZXQzMm9BUWYzb1hhTGdheExGWlJTaTU5bHhoQm1KMHJuRUVxLS1PR3M4MEdsdzN3TlhH0gGLAUFVX3lxTE1aRlI4SE1sR3AyM19Yejg4X0xib3piVWZmRjBfOXhGUjJZb2M2QXVMYVByV1UwVHlSN1oyeHJkeG40VzU5ei1tWG02ZC14Mmx4UzBBZ1ZWT0tlMmEwTjNveGl6cy1YOUZRVzhFdVlWTjlkc3RIRkNUeldsRDdJZ1g5eUdYMkdESXlDMVk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
