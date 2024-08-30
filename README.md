# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Angelina Jolie Spent 'Seven Months' Training to Sing Opera in 'Maria'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOUWpjU2ZBTXB5UEd0MUZCQjlzb2h4NTJLeGotdkVsUm80c3M3UjZCY1BHa1VVY3pGZnNiSVIzb21TVGN0Y0R2V2dVdmlHT0JkNlFGT2V0dTNlcUljT0Y4VlF4Z001TFhqNTV2VHBMamxwelpiZll1LXpnemN5UUJoZHNOYUJfbHZBalY0M0VqOEMwbVZtczZ6czVGU0JNX0Z2R2QwSG9FWHdReDBfR1pOREg0UVozemxsUjBHaWVtd2p4bTA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
