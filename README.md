# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**First at-home syphilis antibody test gets FDA authorization as STD cases spike in US**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxNbGY4cl94eHZ6RmZuQ3dRQXMyN0F1dUdMWEpQdGZyRHNZTUxiXzlxUERYVmpTTlY5eDlNYVZxSFZyU0RWMm9ZUkxNamgtZmpUcGxVeTBIMXhvNmRyRWdRMC14cktmQXoyZTR1aW5JQkdDeGhiY3B4YUdDekVDVjA4eDlaaHZ1Z1p2ekhNU21jMXAzOHhveHJhMWM4eDZfYlFvVmxFZlVqQWJwUdIBrwFBVV95cUxNVkJBZG9JV2F0cUFaY2hZc1pWWDNlZHRxSzgycjJtai0yYmZCYTFYN3lNQ2E3bmhFcDV5a20zMTkwd2pMbzRDN1AtZGhiTktSMVJ4Wk5kWWhCa3F6Wmp3M2RFUzgyR1VmY0tjbHp1aTMyMGlSN0RMYWw4VVVQNkhxcXVnamhodmwxaVJneXB1dDNFMWF2OXIxOVRURTJkcXBTUlNpMmtFd3Z5VzFfU0hN?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
