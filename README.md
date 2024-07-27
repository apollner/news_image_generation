# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Prince Harry Reveals All in ITV Doc on Tabloid Lawsuits, Saying U.K. Press Is “Why I Won’t Bring Meghan Back”**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPOWFVTUYybi1WR3g1RGFoVVZ6bUlBRDBxT2tlRHE2YmpldFVncmtMUm5SNTJ4amlIMG81ZzliSTBNeGhxNjBsc3FuQnNRYmVQeHBoMDVCVE9PcTYzTVNVanFncTExeTR5VkZtTDZoOHd5RHpqMGdGZWZ4TmpiUnhRVnRNSjFkRGVYaHd3RC1NVndiOVpvV25CRng1S2piNFQzM3hUV2hTQXRadVVhcVlUUHU0ejZfY0c20gG-AUFVX3lxTE9DS2NISXJpSGl2eHU5X0NITkdIVFcyYTFTeE5walFXVDA1ZS1DbHRpeG9wVTl6V1hxTlIzZ05ZVDU2Xzc2S0JYR2ZGYi1XN1hGVFVtX0ItUTlkckJNOTkzVnJZbnlyZlcwTUZYVkpWZWI5UFJabzZScTExS2tKQnlFbFRGdk9PV2FnSzBGZTVVWVdycG9xUEx1R2JZbG5WX2FXdW5TSzRWX1ZhZVJXZG1UbUxxWkg4WGdWX0ZQU0E?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
