# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mosquito spraying this week in 13 communities at risk of dangerous virus**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxQX0gycXByZUZzVWJwU0RFM0JmcXAyWXJkUTFSTU12VWhBNEN1Tk9RdHFlcmh1SWcxYlQ2a05OV2dnNWJnR0tLa1BwSkhvSHV6MmwzcHlmTkVhUk5NdC1TYXJSelg5UV9wa01CWVZ2REJpRUNwQmRGVl9uNXN5dFl0Zjc1UGZ4TlRhQUloU25QaEJ2UVZhN2FrbGswUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
