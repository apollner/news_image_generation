# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Live Briefing: Blinken in Mideast to discuss Syrian transition as Gaza ceasefire efforts continue**

You can read more about it [here](https://news.google.com/rss/articles/CBMikwFBVV95cUxQcEJXb3JldjhkQzBoM3ZqTkdqWlJDOFlSNUthOURWTHYtdFNmNXJQUG03Y1RqRGpGUTg2N2lBdTNRa1g4aTVldEwzN3JReDVEQ1MwOE00Uk9oS3l3eGFyUDIxaE5ZejBsQU1RTElMNW9mYWtPQV9HWlJUNXhsNG1zQ2dzbFFva2tFU1dCWTVadjJnTms?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
