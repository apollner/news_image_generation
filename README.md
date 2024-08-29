# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Salmon will soon swim freely in the Klamath River for first time in a century once dams are removed**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxNSlkyWk5jeVVkQnpCcEhtYzJwazhvZ0hRbmF3YkVuSW84ZlJhc2ZyR25yd2JXaUVHdFVSZTktN3pzU1JHRGdnSC1WY3NIUFFUWmpMcl9HU3lFdFp5VmY4dGlfMXc0X0VaY2lqa2wzS2d0a2liQVdBNFZ3eWpTY2hYSWFmUkpjYy1jS3ROdFB1cm4zMUoxcnlXakFvY2Y2VEczZHRTMDNpUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
