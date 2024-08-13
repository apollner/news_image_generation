# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stock futures are little changed ahead of key inflation and retail data: Live updates**

You can read more about it [here](https://news.google.com/rss/articles/CBMid0FVX3lxTE12aXA1SHRtUVRVWmY3NC1TRlhYbnkta1BIcFFyRlhsRDllVHVnQzRCX0RGb1YxbzVCREZMYXYxQ1U2ZjJNTXVnVGdmV0NIR1pkWFBLeS04N0NpaUY0bURXTVJtdl9ENTJWVDdCcVU4aXRHbGkwNWNR0gF8QVVfeXFMT2R4NUJHMlJoS2dpcHc4Y1BqcW9zMHNWM2J2djJWQWU3TVg5VmJsUnVwRDVtdzFHVlk2cy1aVUcycWJ5NTY0b2JfTFZqS3k5dUZ1MWFnVGczNlozQWliYmoyQ3lXM2hieU5GQ3U1dER4ek9fZXdETXpmU3NVQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
