# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Asteroid breaks up over Philippines hours after detection serving as reminder of bigger threats to Earth**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxPMW5Ec3BfSUs4VWFlMWdwTmVkSEdrUVZYUjdaZjRCTnVLMWNTa3BQNFVNczZxd0pDelNFQ2YxbXV5UnkydXAyUnRESjVDVUJXM1BsaUw4NjFIVFQ5ZDRzLXhyTzF2OEI0VzFMcUxFU3dCbXRHU3FHdUgwc1pycnZhR3pUZm5FdWJ5Rlhfc1V0ZUVteXFvYlJYT00xS3ZNZ9IBowFBVV95cUxNc0s2Z19vWEtYQVFkeHVjX1p2cXBJamtxSFhMMHdYdXpJWEVNYXFGN2ZlS3dJcktwZFhNcXVaRXV3T28tYnUtYTVfeG01eDR0UElENlAwR0M2VUxvY1lQVEZVN2FhZkl3cUxpUGZRczJHVkV6OGRTWUtfSEZ1a2VUZmFJNnhmQlI2UjM2VnBCR2lCTzFwLWJYYVBvekdGTkhWNFpF?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
