# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Matching dinosaur footprints found more than 3,700 miles apart, on different continents**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxOXzJLenF5VHlyMUxwelQxN3plYmVTZmVKeXROM2F5M2F6a1pKeXhMaXFlOE5RZlNzdGpnWjlic0pDbV9NcUV1aUtkNENPWnVhTHZVZ3luUFFWd0pETWRiNEl3eDhmQllyRWtnd3NnX19uMFFzc3pKSmE1MGJEUTB6M3dNUndJNGxONE5UUXZTcmxnemRCWGhKZUF0UdIBoAFBVV95cUxNODA5OHVwTHpxY1RCN2ttQnU5eG1XMUdZc044NVVwYTR2TE5QSWt1aXg0RzIzclZLYW5IRDRUNHR4YkdRRWZfWlB3NjBRdGRhWENhSVZON2FFMGpkOURpYWl4OXFWXzVmZ18xazhaLUdINDhCWUhrUWpENmJKOTI4cExjUUlaYVJ5N1FITTRZSHFBRnFtRjJfUFJvWURxZnlu?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
