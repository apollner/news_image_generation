# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**CrowdStrike accused of defrauding investors in class action lawsuit**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxPSnNhTTdCbW9wZmpzS3ZsVzNvRy1sa3hJdFU2M0o3UWtBRVRnMkc4bUxKWUxDdTBzRE1DVjBoNmotNDROMV8wMG1zVHprcEF6SmpCb3htdUQ2YVhSNW9PVHFGYkZLWGtNRE40NVlBbTFWejR3SEZuVE0wVTBPdHVnd1VZU0NpUTFKc2JDUFN3UDNPZXZZb3RVQ0ZfdndOWXRFdWpZdTJwMUc1V0E4TE5lZlBoWDFOU1Z0Y2xFM1ZPSGt3MlJF0gHEAUFVX3lxTFBxN3c4UzBQZHlPQUNqOUc2N245b0d4LVdUZDF2b041MlEzeVhYdUhzd2dqVFJValdKblBfVXBzMS1ZWUlLcFp1b0lzNm9Ha3dZZER2X2otRlFzUy1XaVZMZ0VKSmZ5b3RtODh2eEduN3JsdVE1Yjl1bURoX1lQTzlUa0k0OHduTTNJYkVtcmFIZ0JOd2pwLTUxUk9qb2JWWXJ5aVN5cTZOeXJtMHhBdzhWcWxzVHk4cm9EeUI2VFAwc1NGV1U?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
