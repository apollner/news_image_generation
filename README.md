# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Honda-Nissan-Mitsubishi Alliance Goes Official**

You can read more about it [here](https://news.google.com/rss/articles/CBMigwFBVV95cUxQS2liUGQ2cmtHa2NOZ3IxUE16M1hVU0R6cWNMYVVLQzBRV1ZsdEZzaTZENXVFRGRlQk9OelV4dWRzdFRnZWVlUVlDTjJBa1I3VlJSeVRnYzgtWmJhNDFQalFfSWt0SVUyMU1JSFdDdGJWOGotTmtVSmRoYkN0TGZkcm1NSdIBiAFBVV95cUxPWnQ3M3hZb2xYOUZCd3E2Vi1Ic240LVRJbnUydW1QNlMxb1RHbndlcFBWMU5selFhRmxHR1pBem1EQjIyTVJCRXpyV194cVkyNVdRQWF4c0F3UGx3Si1CYnY2WldfM0YyVzROMlN6TVdZcW9OUWt4RnZ1TjRNMFVyOVVIY0Y0TTJv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
