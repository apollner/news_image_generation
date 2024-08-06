# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Australian Dollar declines due to increased risk aversion, awaits US Services PMI**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxNTmlSNjhRRnBlN3B4cDR3RzM4bmZxMHBBSEtoaDgyVVA0ZFZ3bTRrSnhfY2p1bkV2ZDcyTEduZkVhMC1TekIyRjFiLWF2REEwSXNIUjJGQmNGWjdhWmtNM09FdTJhTzYxVVZEc0lvQTR2TkQzOWJhcHh1d1RfMzhNNzFfWnNvbnIxb0xESldRLUZ2Wk9rMDk00gGcAUFVX3lxTE5UaVJSV0xybnUyckVyQ1lWSUFXeS00VFllbHQyMUE4XzdoQjA0U1RtWmZwN1hmbGNjWlJ2eHJEMW0wT2ZLWHhjQnFiVkRhTWxjOW9XQnlBQmJBb0Q3V056Ujlfdm81aWgzNzM4OGw3dmxtOE9lMzZFbk13TG1WejU3MlBwWG4yUDRoUERDSXUyUmFyTDNpSGlHdG5wZA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
