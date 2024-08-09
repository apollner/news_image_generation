# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**New Boeing CEO seeks to restore trust, meet factory workers**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxPVFJrM0FMalc0VGpBeUFDR2xTaVdaSzZXaGI3VUFFeXZ2ZmZzOThkVHV1d2wzY2NweHl2Q2JWQ3gtUVYwUEZPS01zM1BVUHI3ekttd05uWnBXa2xucW9OMEplS0E5SkdCWEhIcXA2ZHdkeUp3M0MwTEZCdzRhckFNM2VBVWwydnlMYUUzZUtoUW9mSGVuTXl1dTNrLW5vVkNNM2t2c2s3Zm5IRWhjVThJSTdBbWVJTV95SXpZ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
