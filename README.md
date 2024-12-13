# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Bill Belichick, North Carolina contract details: Salary, length, bonuses and buyout make for unusual terms**

You can read more about it [here](https://news.google.com/rss/articles/CBMi5gFBVV95cUxPZkk2ZzhCdFNidmNDM1VoR3dWSjZ1OGdSdU9rRlpONmxuVUQ3bEt5OUphUmpMMWF2U3Iwa2pMQmZ4Q20zOGh2aHZieENieDI1WjIwLVRkY2FLOHozUTFUMVA3TDhwdnpWNllxbDRUMUVJbDc4czh3a3FVNjhUaUh0Y2xGWDgwbDlTYjFhdEV5NjM3R2MtdnJmWm1VWHFJeEVmZlROSHBMVW1nVUNHRDM3MFhlNWpRbGRyZzA1SmF5a190RDBtYjFPVWFneEx5SHNGa2RGRDV0YW9YTndLWEtEekxTbVhfQdIB6wFBVV95cUxNdFFfWDJ4dWpkUFR2ajV0VVVUNzRPcGhGYXV2ZlF2RkxnZThuTUt6UUFaWmNpMm5JNHAtQjJJUXRCdl9DWkpnaXlMRVRUaURTbGtheU5VeTd3akJhSm42MDg3WUUxWTlHMDRfRVhVYXNlZmdEU3hXVDFuZm1GdVk5TzVpbEpXQlhSWVZQdlhLRU5IWEEwcEoyMVlQM25TTjhia1hvMVllQk40WUZmYVdrRXVIcEc3UG83RVF6cFJseEQyVVZReG1McWZxSUJlRXBrLUFhX0JIdHZoOHFLY19qUDkwdGR1VzlUdHBj?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
