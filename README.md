# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Exclusive | Jennifer Lopez ‘furious’ and ‘humiliated’ amid Ben Affleck split as he holds back on filing for divorce to ‘protect her’: source**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxQQko4RF84V1VJdHVEcks5XzVORlh5Q2VRaU5oVGpuckx6SXVBOXM0UTdSQ3RGbXRKVjltNTE4d0JLWHFwcnJBMGhlRHZ4OWh3NjhpRjhEOEdQaEZwQlV2SW1UM3JTMGJoamhvTkRPSXJXREpXQWJUVF9XN01KSXhncDNCSjBxaGdQMjlKUW5saHBLalpXZ3RXUVJtcw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
