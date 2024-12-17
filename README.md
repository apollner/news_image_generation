# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Live Briefing: Gaza death toll crosses 45,000, Health Ministry says**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxQcmwtX3pHN1ZRa0hTdVBrekd4Vm9yWEJiUkcxRVZuOWxwMUQtVFhNTTNTY3RHR0VLTm9HLXZlSmZNc2h6LThsQjNfa0tRb2YzN28wYzJ5MGhwMVRRYXV6V1RKVERJSUp5R0hZc0ViX2VJR01EOG1zZVYyVGRYVDRGVXBWdDMzWDJ2ZU93WG5oalpMNzJuUmc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
