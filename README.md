# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NFL preseason Week 1 grades for first-round rookies: Who impressed, disappointed and surprised in NFL debuts**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2gFBVV95cUxQYTJlTVhYZjBrZnd2OVJ2NE56S3M3TmZYd0dJM1hIWTd0ZmxOa2syUVBZdUJLRVV4cVBFeU04UUo2WXpPY3M3NDVaeTNaVXZhM0J4dFpVLV9mZXJDSlJJYzdhSXBuLTVvR2swX25pS0s3UF9CM0pIamtRMlQ1Y3lFV3ZTRTE1QV9TZ1h3T2l3cmtlWHo1T3ZxYnA0OHNlcE1qV0RzOWRwN3A3Z1lkeENqdFBPekJ5S3RIcFNFei1ZMW1pTF9VekRpTHRMNGd0emkzWmVBc2FLc3QtQdIB3wFBVV95cUxQemFFMEs4aUF3STFyVnJBTE94RFQ2RmFWamZKVElmblZXa3VOWnY5M0o5dlI5N3l3YU0teXVWWEU1WmIzdzdzbmd6QUtrY0RpWi15cXBRaXNDOVpER3pwcVpWV2VsNi1lM281N3hYT2FKMHlWRlpOU3A1YzRSbTNjOUZUTTNUREtGVDRneVFzRzJncXZudkd1eDZZaXRGZnF4LWl5WC0tUEZJeVV0UWRnTzRMS3d3c2Jja0VIQjQ5QUtrZF8zNF92eDZ2QW9BLXdaLXJLY25NdDFuemZHbjJR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
