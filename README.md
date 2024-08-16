# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Matthew Judon trade winners, losers and grades: How did Patriots, Falcons fare in deal?**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxPcXZ0TVUyQjJIMGFjeG9iOGtNRW5Zbm9TUFpzQks1dlhubFNXZ09OQTBmZGNsYjRpSlJJTkFYLWo5RUJZRVdIVllDamg0WFdaeHhKSWc5VDFtZEJyWXJqWEk4NmxJOVB6c3RPQzR4UmpUb0I2YU9GaDc0TV83Z0RDc1F5ejRyTDFleUFabm5MeVZpMjE0LTQ0ZVFIQWFBU2RTYUh4QXlHenNYZGFYRWlXcnhKSnE1d3daOFRBZmk5SzdEaFE3eklqVg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
