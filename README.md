# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Iran’s jailed Nobel laureate Narges Mohammadi allowed to leave prison for 21 days after surgery**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxOdDFUZDE0d1RUU2lRcWRLekVEbkx3ZW82bUVtelptczA5eDlEcEN4bVh0Nmp5NlNJWUFMYTI5bGhMd3VzZ2JOUGNSVDQyVzFvTWIyUkM3WW9JanBXMUp2bV9UdUw5VXF3UXV4bVdEOURfMWVCTVVldW8zWGlnLVEwMkJkN21tZVh3NDNfY0FBMXVla25GRUluZjkyTXhRemo5d2ZYa1BLb9IBngFBVV95cUxOS0JUTHl2NVJhQzlmRWJaYWtLVVNIZjU4bUZna3hnZWduVDA0RFA5VHpUcGsxdkVKOTZfMDhNdmE2eHZXbUpiRjRWUFJhU213cFBHQjBPUHVDSzZZU3VsOU10RFpXRDE5WGNPdE52Mm0wQ1pCZ1VTTXJVZ1J1UTFXbUVxYkZnYmVfeDdTOG5FeUNLQmNqWUM4a1FNSm1Vdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
