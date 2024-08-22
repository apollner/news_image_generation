# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Pete Carroll could coach “tomorrow,” but he’s currently not “desiring it”**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNeDJlOXZ3aldPY1loaFR4d2JwdTBKUVRtX0tSMTJ2dG9jSGs4V3ZJem1RMzhZMDZQUEdscjJvR25xUlpMVVRqUkp1RkJBdFBfMmw4STNXcXJnUzRFLVFZcWN0enJrT09EV0VqTWdzbU1OZ2VSakdORjJkTVR4NVZ3MUxuRUFaYUZxdl93T2J6MGtLOHpTdEVfbzZleEh5Wkh5VzN0Y1hjMDVfSnh4NDZTbjRnWFEtZzU4SWQzdFRqb21YSTZVSFVlRg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
