# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**How a ‘putrid’ find in a museum cupboard could be the key to bringing the Tasmanian tiger back to life**

You can read more about it [here](https://news.google.com/rss/articles/CBMi4gFBVV95cUxNdFNCWmxsbEZwRGZfY1dKMk9YQjdiYVpoYklwR05sVDljTnBQS2Fad2RUaWp5T2lDczNwcjZfMUY5cVBOOWc3NjdUUXNTNHFqTVRwS0RZSENhNEhkcmpwQU1zWTEzWHg1TUpZTUNNUEdEMFljVXBEWDdza3F2SXZ2anlsYkRwcnBsdHRJUHluc0U1dUN2OEd3a1l5OVAwNmFkSlQteTF3ZEZGX1Y2OEtZLWI1aTNOZUZqdEJ1bGVYdWxseFhtUElOdWNXclpQM3RDZExDeFZuTnNDMGxVTWgwbTR30gHiAUFVX3lxTE93LXNKNy1WZlFUNVh1V2pYVnFKdTRpdUwwTFdPV3ZqWUdXV0loRk9jMXZpd0MwcTdJX3dsU0R4ZzU5LUJHXzFhY1F4bFl6dDhXMS0yWlhEcDVtWTZ2SEs0dzQ3dHVjRi1lcXpJRWlXN0dNUGMzN292YllYOFduektQSlduOFJfX3RPbm4wUFQ3Q28tb3BZa3FuZlV2UVRfbmtrUnpla2ZYRmZ2X0FscnVhWFNOYWFqSTBVTUhPZTJ5cWtWaGk2bUw4LXBfd2ZlbkszTUlLV1U3WWVlM09xNUtncGc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
