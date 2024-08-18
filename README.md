# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024-25 NBA schedule: Which teams have most nationally televised games, and the reasoning behind it**

You can read more about it [here](https://news.google.com/rss/articles/CBMizgFBVV95cUxQOEVWa1c5d2tPb1JSMHNhR0pObDdHd2tlVEd3cHJfYXdrSnpINzRMLXBqRy1jRWc1OEpuWmZLRnpaWm41QkxacFQ4OVI5NXRRaGZ2OTZLczJWODRrOWJzYkMxQ3pFd3FwTU1Wb251bUloRFZ3dEJfUlo5TkoxUlJseDJOXzVUYjJZZmxqeUk3djZFQ0JEOXFIS0g0OWlQZGtjMkVZRkpjMVM0QmJjQUNjZFpOT0tLZENWc1JCY09SWWZuOXJra2lKU0RlU2gwZ9IB0wFBVV95cUxPQXpzejU5RGEtZTByaklMRlpNclNjQ0ROdXJBbTVXUjc1OWxkUE1PLUs0Tmd1QmRCQ25WMkNIU1V1VTdmUjN3MHZUbFNxNGJIWnJRSjlyT3F5QkVZbXhSd2ZhZG0yOHJrNDVRVHFwaDhIbXZhaktTX3BPNHZHQTZTbUh6em15S3J0aDZuMXpNX3FNQk8xZzBVYVA0bXIxRjJzeHY2c2w5ODFCQWpvN09EZ3pmWkhpS2pYZ3lDdEh0UHVqUGFILTNFbEtIaHlibmdhejdn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
