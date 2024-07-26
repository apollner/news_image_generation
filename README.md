# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump turns his focus to Harris at his first rally after Biden's exit from the 2024 race**

You can read more about it [here](https://news.google.com/rss/articles/CBMitgFBVV95cUxOZGRKeV9OQUV1azhRcUpScHduQUh1YTFsVnV0ckhpVkVrX3Z3TGZyUldwYlQwVF94VmpYNENLMXNCM0ZEVUtzdE1QYWR1QXpLUTVHY201MHhMSGtJTFpFdHJUYmlpUzNHYl9wak9mb3RENDRqS0J3cXIyR0xmay1mQUZBY2plU3dkZ2dNbE5OaW5zZVJaSHNNNzhEdTR0NzhNRC1lYWdHQmE5QndBX3F0YlRfUlFQZ9IBVkFVX3lxTE9BT2ZJSkdDNWd5dkI5UmVUQ3FBTkgwdkZnNVBpTEItOTl6bzlEaENseFFFYk5XTmdEc0pxM1VJbUloUkdIVjBKVkUxZlA3dE9ZdEFIZ01B?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
