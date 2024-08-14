# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Cancer deaths among men predicted to increase 93% by 2050, study finds**

You can read more about it [here](https://news.google.com/rss/articles/CBMidEFVX3lxTE1fTTBlXzRhSUYzMHE4SUFvRUJJSmg4dFkwY3pmZE9XZ2wyaFJaaEF5RWw0SDFiU2VWang1d2hDb0hYQWVYNEp3LWphc2RjOC1IX25XTzBIRGxxZlhjVnh6dDZBTGo4SjNsRmxlcE93WFhfdjNV0gF6QVVfeXFMTVlyZG9BSUEyQjF5dDB3b2E1aWEzemE4T0VCbTZVVzI3MGw4WmtQOEszTEtFUTV3bTlzRkROQmxwSGI5dk4tUTBSTkplMzdGdkRzNzJKLW5MblR1Mjc2eFhTWXRVYXpFNzRlSFlGMUdNQXVfY2RWaDJHdHc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
