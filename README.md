# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Marvel Fires Back Over ‘X-Men ’97’ Creator’s Claim He Was “Stripped” of Season 2 Credit, Cites “Egregious” Investigation Findings (Exclusive)**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxOOUdtbXRZd3RuLTZkbndaTW92NXd4LXBKbzJvMU1uUmJBSDBBOTdxU1hVYUJhYUJORmpVajZOY0ZwTmgxeHNjQmlPbklfa1hUM05DODdmektqTjBkS3RKT3BzNHZINmx3ZzJCUnpnZ3oydFZUVHdqcnZYUFBKbU9icU5NVEM5VzY2TUtEVFpBYm9WYWpEemtFcmFnVEFyQdIBowFBVV95cUxNNi00Q3lSYmUyanNDNDhCSnRqT2pqaFFiS3lyQVMxemhuLU9LdHo4WGppRXVXUG5yMlQ0SEdZdldfN2hWR21xSE1RdzJJSHlxSEpfUEMtdlRaYmM5R0gtd2VpLUgyVEJHVnp2WjhoVV80RGxGN2YyU0lSVWQzZlNqc3IxZGNTLWF4Mmo3THlsd3gwOHJiMEdvcHFfU01KMTdpcTJB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
