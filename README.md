# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Police say suspect in UnitedHealthcare CEO killing wasn't a client of the insurer**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxOdVpDeGM1c1RPbUc5N0VhVFdRUEVRNm9XakoyZjhMbVlranBQNldUekt0UkNkQjVhd0s1RkZGTXBZeHlzOW5KOHloZy1id0l2a1VSa2h0My1ENE9pd0FMVllBN1RQWERaT3MwNDROaFV1MHFhc3p3SkRYbHYxVEJ0bGJ0VGd4NS1Ia1dycXNxUHZudFFreXdCOWlrUVd6R2NhcExVbE00TdIBrAFBVV95cUxOOTVreGE2SGtLTUY3LVIxdlQ4Rl9RWlpFeUt4VnJRZXNNX1VvRWt6VFZaR01BZGJoRWNOZ0RqQVJwQ2lLSWNyMHJoWGRyQ2p1ZnU2aUJxNGxMbFh2QURvWVZLSUdhUWtGdW0zRHNsVVN0amRHT1FMRnYtVEkybXNYYWVKcDNQNGRxcFFFekgwV0xnaEFwTXNWc2JKQTFNRl9NS3h6ZURZWnFEQm5s?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
