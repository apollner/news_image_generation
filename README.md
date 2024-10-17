# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Global Chip Stocks Erase $420 Billion After ASML Sales Warning**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxPeVR5M0JDd3FJRjAxUm5qU2g2ZVIzVWd5c2xYNU5PNFdWM00tWUhqbmRHMF9oUjk2SHhjVVNrMnBDOEZhS21OSk9LaFRyZVNBX1hZd1kwcW1tcTVvbk5pV1V0S01qb3B5SmZLUkNLWHJ3U3V6UUtHSjdDVkk3SjJ4ZXlNVzBfT1o4TnJQdXhVTVJxWVozWE1UMVRmQmgzSDNhU0RSTW44bHMzS2VNZ0thWHJ6SzE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
