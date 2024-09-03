# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Exclusive: US seizes Venezuela President Nicolas Maduro’s airplane in the Dominican Republic**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxOYm9jMDU4R0xlbC1Ea0tCUGJyMFJfaFlVUFd1Y1ZiWUd1RnFGb1c1SFhqTnNIUHhYZmtmek9vanVmM3QzOGt1cnQ5ZFBpOFo4TzVQdjY2SUZMTC16eEFpZ01Wazd1MWhyN01nMkNiREI1bjBEUzRMcFVwYWtMc2xOem1PU3V0SXktRm16dXpsLXlOMUJPbk0tTTBUMHV0Z9IBlAFBVV95cUxQUnRNWll1Slp1Q3pUV2ZlbkpwQkswQUZRcDdkaFhvcVhjYmpRR2d5Y2poMU5aMlpjUG5ua1VLUmlUYjk5LXk3UTRTTmZTeXplWkZxZmNGYThyUTAxQXd4N2lVX0xZNGF0QzFDSGJuVXFFRENtc3pPYldVd0YwMVloMXlkcG5Lc0JaZGVfQ3pDV244ZmJk?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
