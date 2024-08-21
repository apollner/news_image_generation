# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harley-Davidson hits brakes on DEI**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxQcXVZVVZKR24xMlVnNlp6V2NjTVhGT09JT09KY1BzV1B3OXJJdDZSa3VIN3RkOTNobzQ5M2RCaTMtSzF6SnAtVThjSXBzOTg1X1p4LVM1VE16bGZvTDlTNHZTdVBlaHl6MkptYmJ6b3B2R3pxeWxJN21kMmpORE41RE9MZG1NSDFLQ2lVXzFYUdIBlAFBVV95cUxPbDVoekJkbWFrVC1DdGpUdi04R0R2YmU0MmhiQV9hLTRILTFZSGZ0Um9ZZEY0U1FhLW5mQ2dHX3lkamZwZ0JxY1ZFbURJa256ZW9aOGttQ3JCWDdQQmFMeXlUSmF3ZzRzbG03TGN0MTNETTNoaEd6VjVvNkNEYUlWOTlaVmtHdV9LMGNQcmc3aGV3Tkcx?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
