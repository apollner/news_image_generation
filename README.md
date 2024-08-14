# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Elon Musk interview of Trump marred by technical issues**

You can read more about it [here](https://news.google.com/rss/articles/CBMimAFBVV95cUxQWW1TTzVFcGk1bEh5SEZISjlUeGJ4NTRDSERuSndhazQ0ZWR1cXE2NEowNnB0XzcxV0F6ZTA1RHZfQjl2R0M2RzA0TWFZWWhTSlpWU2tSeUgycWNMdHlORXZXT0FaX0JldklJNjR6bGVxMWhIY09YZE9ndGZFYUx3UmsyQVI5WTR1SG9EMWdCSFk5Z19mb0dLUw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
