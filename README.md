# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Atlanta rally: Harris tells Trump to ‘say it to my face’ and challenges him to debate**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOajNIMTQtS2FYMTZaamdoUG93UnFvdFdEWkFYYTRkRFVpM3ljMndxVmsyY2VYdHVMd3pOU2JqS0VScGdycmx1NG5hdk9zU3BrRjI5REtJb3I0a2hxcS1zUnJ3ZS11cFJ0N19SUEZIRTlpclV1NWdzT0hvaElQWGZQYXdiOEdCakhGcGVN0gGLAUFVX3lxTE5mVmpUZ3BNcVloSFJidXpCeEhKRHRSRDFDVFRSR191UmtLcV9qcHZRdlo3TkI1TGZDUHEtV1RSUEhVNE1oMkt6OHU4WjhIR0syMkMxYWM4ZlVTYldCSXVMZndpWTRYRmtYX0JTenZwWU9CNGx3bTNsZXNPMWgyVVRwTVphYl9nd1poaTQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
