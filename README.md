# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hezbollah launches volley of drone attacks on Israel, vows revenge is still to come**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxOajE1aW9PSk1pSTJsQUJFbXBYeUp3UFEzQWRYQTBubDFxdlNJa0hkZVRHejdieEJXNlFjODd1dnJpeDV6YkljS0Q1WkhoWVNiajNIek1LSWFnUkVjUXhRQTVxOXF6cFg4TWdRVHYwYVFtMGVKOVdmUGFSa0RVa3d4S2VsUjhNOVlGY21rOFhlQnpFVjFpdG1wYVR5al9xbDBLT2VIVHBWRzZvMHFQVlc0a1dBMXdMMkRHTEE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
