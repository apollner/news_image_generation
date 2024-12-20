# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**West Valley father believed to have shot, killed family members then himself**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxPNk9NR2hPdmE2OXVBZDZ6UTJRUTV0b0V2OEJScGIzNWRDUV9kWmdIUFpKTUc2aTE4cWFoM2lvWUdRWU9yZVl6bUJjdDRSNXRMLXdKTW9JdTJKM2RmQ2dSS1VxRE9sY3BWY3lsNi1oUHp2aWdGelFjRVM1SVZCU09oc09WNVZtTHFNNWtUWGNmUlJkYmVoR3AzbHpZTjhwNkpM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
