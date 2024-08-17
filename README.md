# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**History shows investors should keep tight leash on risk once the Fed cuts rates**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPTTlneU5Ba1J5Q3lEcjJRUWNVTC13cGxJSTZadzlSNklQSm5xU2lrbGR1cHpwcE90N1YteDZyRjdtM3I0N3ctMkptX21rWHZjUnBiWmhlbkxvdnd0RUU1N19zZU1GUGdOdW42dGU0cjVWQUdZSFh1cmV4RjU1T3JBaXM2RzFzSGttZHJEbkhBWTNRMFZPVnhRaWZrMTRscGZFbi1qdU9aS1RmNl9lMnFvNXptNUIxQk1SLVY3VFlOQzVJbUp2Sk9VaTgzdWllXzJTZTJjUlpyNNIB3AFBVV95cUxOb2IwQy1hMm5WQjFfOE1kS2FwWFd3ZVU4M29hZ0M4eWpJS1A2b1I5ZmM0YTRneVdvamxRM1hEWlU4ZllCWkFlVjA5dHlSLUpiY0ZEQVZOd0l1TGlNSHVISEViMm16aVJ6ODA3ZFZOLWMtR1dWczk3SHNnRWJvc1F5NHdyUkw0Vl9SaFI0ZE0xbjJXZXdvX0VHU3RvTHZFN0FsNXlWRzlSUFpyamhWQVdPcXp1aHpSeWdzZkFlYXZRV09CdFVXUGRsZHpIYlRFMFJPN2NKeGhZN0pKOWZn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
