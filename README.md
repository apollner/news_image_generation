# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Evacuations ordered near Athens as Greek authorities try to contain wildfires**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxNUFhEemRTMjFESDFnWWcxSWpQTkxhX1A4VlpCeDM3cTdYZ3A5QjdWSk51ZlZiOGV2Nld4cEZfZklIQjQxZVN2cGxWN0J3d0t6WjlhR3YyMkt1SGJKYkZtdEhEX3otVEdvUHd3V2pEVTZkMHhLUEJnT1Zqak9xZmdfbG16OXlPOTRvVER2QlBBTUsxZ9IBiAFBVV95cUxQdTI3dm50VEhfcjNZM04yZDJEcUZpLUFGdGFMMF9OcktMbHR4Y0dja3diZjlmdzdoOEt0NkJYLVBNT2VwUlhiRUg3TElkenFJNnZGRkhYR1Qzd0ZzN3Q5czc0V0hLUXI4akNKdkZhVjVyLUFMUXRCY0JhSzV1dVJUUWJzUDhNYTlS?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
