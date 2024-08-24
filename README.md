# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Former Rep. Adam Kinzinger tries to convince his fellow Republicans to vote for Harris**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxON2h5eC1OdVJzQl9BdmR5bG1LQnhqVnpJMWRnV3RVenJNQjhBVGdYS25ZMDFUWVl4YzhDcjVsbE5Tb2dMWXI4cTZpRFZ3S1dUVW1mVUNfa3pibVNVZGZCTi15alU4ZFBIanVUckU1UC03OWQwcWZoMFhsdzBlemtYdVNfLVR5cE5pUy1mMFpzYTNOYzI0S1I1VmE4NzI1THlJYVg1TkM0eUl6UQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
