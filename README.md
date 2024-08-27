# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mandatory evacuations issued for areas of Ketchikan after landslide**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPY1haZUtiTVY5eHJJR2JjNmVTejRYN09vQWJGelZlTHo3ci00Zk5hLWtuVS1fcHc5WlFFTDNyTDRfdnRDTjIwU0xRTjN4WE1tbmRfQ3ZSU2NJV3RWNUNkcFV6d0RCdGlGRUVpdGNYWUx2cVJ4NE81U1Z2bGgydWFqU3RfQlZuNFd0Z0lDTnNhSG03dU0wT2RUQmpIRkp1VmxlY2hiMnhhckttQdIBvgFBVV95cUxONTM0MWpVc1QxN1BzdzhSeXNadWJUMmduSkpubHpJd1NqNXpnM3NlU3dUaXp2MDFiT2pZLTMzVGx5c2RocGZqRGV4WUtzWjRCSHNGOHZTTDhpUEJITzBwR0hnTW9zZTdYOTVwaUx4XzBMQlJEWWtfU0VXMTEzU1Utbl8yY0ZkV2xyaktsRWZvdEpSVk9mWHVMMS0xZFBUdzlieTRjOTZ4OWdQNm5fYTFwZnhLM3JIWlJlNVc1NHFn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
