# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**YG Organizes Peace Walk Between Rival Gangs, Takes Them To Burger Shop**

You can read more about it [here](https://news.google.com/rss/articles/CBMiekFVX3lxTE84XzVDMk5nS3VFWGhIMklNVDV0ajZFbWJUVnhybkpCVGU4VHZRTjFEYnFvNm5HbjktWnpSNXBzVWVXTmdWOThhOHV3cnVzeTlWTFEycExUbXJsTExwNXhfN3phMHFLeU56aklOYllLeVFoZ3k2RDI1NU1n0gF6QVVfeXFMUG1hcVBYcGZLNmlWZUlVT2sxemJIc2FoNzA5MVpRTUwwN2lwWHA1MGZMV2FabUxTX1V3N1JYWUdGVGJnLW5lUnF5ckhpNmNwTFhkZlN4aGp0STJJRjBZUDc0anZ3VUllbk1Jd2phcHUzbnBZZGN6aW5uSEE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
