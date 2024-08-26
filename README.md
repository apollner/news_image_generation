# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Zelensky claims Ukraine will have ability to retaliate against 'any point' in Russia as part of Independence Day message**

You can read more about it [here](https://news.google.com/rss/articles/CBMi8gFBVV95cUxPRDYyQWNsd2p0WXdYOWxCUmpWWU5BSWpUa2ZVbnNGZnBJbXBXLUdocFpNWGloT09abHk0MEtxMVRjaVFYRkMxQ2dMbXQwQkQxby02SEhUQjJsVlBLdDI1ek5qVl9LN2lwdERiVEtnWENHVm1LaGYzdkhPRGRHYVBWMXNSbmEyaUFTNFItMHB3bGNUNlFQZHlqVkVOXzJRYmpnVllOaUpsM01PbjdaRkgzMVVpczRuT25HTE55MG56MF9vVG9ZZVdFTDVCU25tLUd2N3cwM2ltQTRzRVc0ZnZ6ZDVLblhISmZQWmhVMHFTY2dyQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
