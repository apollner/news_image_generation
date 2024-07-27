# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FBI Wants to Quiz Trump Over Truth About ‘Bullet’ Wound**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOWW1Ga3pVTnRaSEtpMW1MSEw4YUZoRFZyd2dDcW5BZWFTVjRFMEZxb0hHRE5aTmNLaThyTGVnZG1UUGlfdTMyazBaSFFYLWdmdkR3bEl4VmtPRGNYeU5pSGxGM2o5SklqT1NRXy1qakV3WHZHaEFTeHRwdWFyc2M2d0cxYlZNWHdUTmRr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
