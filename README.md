# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**WATCH LIVE: Donald Trump speaks at campaign event in Montana**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxOMXNrZ25sUnl4RGxKMkZCbndGZWhUOEg4NjhvTXpwQ0pSNWxnM0RiUTYtT2xYMThTSnJXaXFkNWljRmRoMFFlWEpZU0tQUXJNeWM5Vm5iQ2F1ZEJQTU96SGJadWI4aTJFdHUxamZ0V1NScEdfNmp5bkNXck43Zm1PRjdSQVZuMXZKRDlmYWMyWG8wUWhZdUhxSFdnSnk0Z9IBowFBVV95cUxPcXQ0Z2hrUFlDRDRJNjlLYXQ5NHQwcjUtZFpoa1NrSWpxR284bHJ5WFhqMUZseHdBY0FEU3ljakhHMU5lQ085NTZ4VzJJUTZFbnpJRVhaaWtfWjFnMWRtNjRIRjNRWkpPRGoxdnZ4RzQzWE9QMjk1RmtGQ0pEY0g2MGhHSG9PY3ZSeGFVZUIxa081dHdYYVZTMEx0NmQ0TVRNV2JR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
