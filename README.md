# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Can weight loss drugs curb more than appetite? What to know about research on other possible effects**

You can read more about it [here](https://news.google.com/rss/articles/CBMigwFBVV95cUxPSlJQTE8zT1FjU3MtZm82eVJ5QUdGNzJDbUo5Q2V4aGhqcGhRaTc0eWxEMGpoOUdHTWpFUTZjeFB5SU9kVGtscG14Y04ybWJCV1hXdUVLUFdDblpZdjU1RjdEeUR1cS0wR1V1bExuUnVadXBETEtXZzlJNE9DVjBCaTB5Y9IBiAFBVV95cUxOVmVXS3FIZWduS1JYcDVHVGVYaXZqWDFfRnZzZ3pVLVRndkhFSWNyVjFkR0VjbXRUTzJaLWpwaGk0cUhjbXNIQUE3TEE1NGp3Q2RUX2xNbzZYdUJhblhTSU9ZRmhEZkxCQWZ0NGpUNVlOZ01DTmhKX0ZKR2NISkU2V3lmMW13Si1i?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
