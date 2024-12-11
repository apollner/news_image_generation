# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The top 25 recruiting classes of 2025: Where does BYU land?**

You can read more about it [here](https://news.google.com/rss/articles/CBMixgFBVV95cUxPQ09XV1FfaEp1ZnFzRW9zRmpPQ25YY3RBREFOVG44S2NQMTZJSk5JN3BpUW0xY2FfMV9BSG5UWFBDYVdBS0x2emh3TFNpRERUR1RpRVRJY2o4amZBYWJsdnltOU52dDNGMlh1aUlCdEZvaGQ1TlBwWnh0RmhLTGY0R2RQam1GWHRPUzQwQlRhWG9iTnJheXRtVGgzal9LWjVFVVBNQUZGM2VSdGt6WFdhby14elAwa284M1RSekF6eEFsU3hDdFE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
