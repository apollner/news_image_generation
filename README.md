# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Broncos' Sean Payton praises slimmed-down Javonte Williams: 'He looked sharp today'**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxObXM5VFZRbVZJT05haDJ4cjZCcGd1VUFiOWJwaXRWcXRYa1RVODlIYTF2WjA2bUt0cUdya3VvQTkwM2M3dHFKQjE4anE0Ym5zR3pPckJBTVNlRC1VX1I2aGxvRnJHV2dEc20xTFptd3VVd2hMazJRVUNwY0d5TEtGZnRxWF9jdjQ4THFWUk9rM2dnWXdJR1FJcGZmQmJSaUlFZzNEbzNHaw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
