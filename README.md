# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fatman Scoop transported to hospital after having medical emergency on stage in Hamden**

You can read more about it [here](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNTHhINVlrQlFMZnUxMHM5dUJNdzVrOGxPR0NYbUFMZHRXMzRuWk5XQXdRU0U5VTZvVUJoSENOQl9IMGU5anFONDMwdDZuQXc0eGFrNWdITjN2ZUIwNnM3MXVQSjFybnl3VTM4eVZDU3RFVkJjcERreFE4clhFa0VRek54WllHYkpjVjZBdDBWakQ3UnRiVTE1VVZ2MEJab2IzYnB5cGxXUk03UFp1MG5mRVk0ZmdCcHQxZmF0d3lUNFQ2anhadUVEOVluaklIVjli0gHWAUFVX3lxTE5vbXIyZzh5WGZ5QVpNQXlZSFZGbG0tMTJ6aGZab1pTOHFRUjNPcDc3OENpUktpWlFMODRJLTRZejRYLV9Wb210ZGhJRXF4LWx0a1cxRU5USVcxZ2JoWlZqNWxYeHZxSmhuT0JqNmpDSnFfajN1VmdmNkYyMnVoUTlnSUNoaEhnWkdOZDJBT1RabGpLZm5CcnpPSzlzTkxlNzdMdGpjMDN3d1pHdnlXdFVBU2hzcGU4TjYtU3NyeTNVU2taVXZpSC1VOHF5OVFFQ0o4c1ZTTGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
