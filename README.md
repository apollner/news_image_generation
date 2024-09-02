# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**7 people dead, including 8-year-old boy after charter bus runs off the road**

You can read more about it [here](https://news.google.com/rss/articles/CBMisgFBVV95cUxNZ0ptWVlEdTlMeXczR2kzOEt4N2xFM1FPRXFKT0d1bkg4MTVyV1JkM3BsVE9YVTN6a1NkVlc3Vm9WZnNoMl9nUjU5MDEzM29KcGI2TThCTXR1SzQwc0ozeTNIbWd0NHFSMS1pdW85N3VjSlZsa2FWTk9QTFpheWFMT3d3bVRFdkV2dVpReU0zdmtIS2pnS2R4a3dkVXJNYnVJc1FIWUpYRTNwTzE5azlrQS13?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
