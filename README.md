# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Minnesota Vikings’ Brian Flores wants to ‘grow’ after Tua Tagovailoa criticism**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxQdGlxTThkWlFqNmZNODF6SHAxc0VWc3pJWk1ST3Z0eTdFcDhhcERoZzI0ZWplUG1GSFF0dG9hNUREU1dTNXVCU1RWZTBMYjQ4S0RYRWloVWg2ZlMwUDJlWHNxQW1QUUxMeHRiUlEySmZSZmEtenNUelFFUlZ6NFdzb3E0RHNhd3FpT0d0S2xQOHlidlFmNGF1dFZB0gGQAUFVX3lxTFBHbVROZ3VlWklINm1CdDZzMnltTi1XMDlOZWpvVE5KOHhBN1dfR3VzOS1QUXVtZ3VnQ29KbU1TNXYxSExiaUxLNW1yREQ2ZWF4bVFMSmM5RzQxbnVJZWxNMUtCemx5ejNGZDdYeWJCQldwVWQ3Q1I3VFpvUzdROEhZXy14WERvU2tLMzA3eE9yXw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
