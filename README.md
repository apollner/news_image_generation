# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Washington and Arab states scramble to avert an all-out Middle East war**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxOLXFRS0FEb0lYWko2WE9paUU5ODh1YmI4M01mTVEzMHdFRThndWxqMjU1YXpOdGdycEFYS0NXZE5ieGxwQnFRNlRaZGNJZU8zM3c1WlpkcTVWSlhUcE9GaURVUmU5ckVRQW9FYkJmNUM4d0QzR3NCUlFzRmtnR08xQVU4a0QwVUFNMzdlT0N0cw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
