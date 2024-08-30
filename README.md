# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FBI: Trump gunman acted alone, but motive still unknown**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE1zT0QtdHRUSU9FQUkxY0tQaWl4Zko0bmF3Qk1oOHdoY05ISUNzOW14RGpLWk1zd3ZOVFc3dzE5LXlNdklLTlk0SndjNWlNYXdTNWZsZjlCSlVvd9IBX0FVX3lxTE81cWRMc011VWN5bG9GMTZZMS1xOXZRTXk2MW5sS01rUy1aVlFKeVQ3eTdVUWltOTdnQ0xySHBwSE9FTTNXa3BUUmw3QnNISDkzNWkxUUpVYWVUWWdQZk9Z?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
