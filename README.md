# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Rice University student killed in apparent murder-suicide, police say, prompting campus-wide lockdown on first day of class**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxOM1EwcjZ3NGdiMU9sZnlacksxWW1fVTFPdFAxeHJxX3lpZEh0Y3pGSEN0eEpwUWRCWFJmakx3UkxVbEFtTmV6bjNIOTVzd3hxZWozX0lGOFhIV1U4WUQwbkdTTENrc05rYWFZUXhINDBYLWhMYXhrR0N3S2syTDZVbEpHTzQ3SHZfVTdQc0VSb2h6a3ZjQ1HSAYwBQVVfeXFMTlRnd2hkZWtaS05qZ1ZIT0I2V25ZZEVoZlpvUER6blhPRUN0LWVXVXROWS12aUd1akxDOTNGR1BmTGIwcWVBcDRELUt6b2o4YV96Q1RKQ25FWEVXbU1WWHo3U0RaWDR1ZzA1amhzYU82YlJFcWZDTVFlM080SFBPTlJZM2tCamVSanJ4WjM?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
