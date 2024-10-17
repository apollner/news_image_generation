# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Amazon goes nuclear, to invest more than $500 million to develop small modular reactors**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxPeDhVQXRraXRaQWZhRFNkX2I0dDd4YlVia1M0dnR1cndkT1lBM3pqS21rdjRYVEFnOEI0ZWFtNUVWWXdWLWYxSlFsTWV1RERXenR0V0hXSEhRTzFSM1dxSV9lZTk1eVZKVlE5NTZOSElxU3VSV2VWcTBUVnBVY0xBNzlnN1A0VW9RTThKbnNob2N4ZDVpR3FLaFhyWUZjWHUtUWdlcVJfWEp2Z3RWWldNaDk1NS1lOElnTEtVMllB0gHDAUFVX3lxTE9MUmZTTjB1SmIxeWpZNkk2NHlGcWh1X2djU1VfazY4WnRlOUxPQVdZZC1hdmN4Q0FPcnBzdkk1cEpaTHBvRDZTWkU5dTZFOWtFZFFVakUwbnBWNFZKeGh5cDhOTVNZQ0xnS2Z2WFJySHI3Z01ycUtLUEJ2V3JhZ1k2dF80eE55MUJQOU96azEzRTJzSmcyNnJnTmhVV0N3WkZ5dDhsZjJ3YjNIZnRHLWl2NlM3a29xR294am8yVXgyZ2ZPdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
