# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russia-Ukraine war: List of key events, day 906**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxON0lmelFQM0x5T2pLSEM5THlBOG9tSzR4SFIzbkFqT09vVGhaWXRRdnJ3azU1elNBbk9BbGFhMXVWOHBxNlp2WFhnekxScE9lRWlJMW5yV2k3TS1RUHJMdVBqRUtmUS0tRkwzUFJheFQ4ZTZLN09iSGtsV05sY3BjN0dtZTRzbGUyQ0E2R2dnSdIBlAFBVV95cUxPSXNQZV84MkV6eGlQbjdRdVIyalRyclM0Tzc4R200TlhPcUxrOHlBWURNWXZuaUYxbjFUOXNtM3FsaXpLR05OR0p3OWpMU0JMMzI1MVJRVEdrT096Z081bmczNWhBZGhrSTdrZ3M1SmdQRHB1SDhTTkdid0UyYWlIaFVYcE5RaFZ2c1hSclMxdVVRRXRu?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
