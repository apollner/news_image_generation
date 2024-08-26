# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hamas says it rejects new Israeli conditions in Gaza ceasefire talks**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxObXhfVkVuZWdDWkFZTnp6ai1WSGdqeVJNTWRvZllRa2czejRsNXNHQ254Y05HM3RmaFJGelJBd3BHTVg0UG1oWEs5QlhhZ0R3WHhxUG9IdlBKVDFCZFNNZENlaEtOQzU2LWxfeUs5UlRPWUhtS2tSNU83RXFtNGdxeUN2M3dwM3N5WVo3TER6UW42VkJvdDduRGtnOFR6ZVVLdzljY29IeXNmS3A1NlY0UEU4Q0hBQ21ZR2NB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
