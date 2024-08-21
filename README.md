# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**European Union slashes planned tariffs on China-made Tesla EVs, other Chinese firms**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxNRDU0WU9VU3h2Qno4VGl1UTU4YXFfRHFzcTZYeEdjSnU4bzh1eFVreU9TeE9td3lSN1Q0ZnQ1YmxBMHNCc1ZvRWZhN29IOGdzWnJ3dmVEOG9HMlZxV3ZIbHBBLW9QX2ZDb1RZMDdHZVFJcm5TTlI4NV9yekFZZ1h2eVFXWnUtZmltSi1LN1p0a005S2tqNXZ6ejVyYzktYXfSAaQBQVVfeXFMTVBtc2h6TTFwNGIyOUY5QmNVazRkNkZWdWxnVVlCTXkwbk5aeThPX0VGWVpBV0N4M3g4ZEhlcmVyRTlCOVFGZkRQMUJTdXlDN3YxckxjMUdDcGY1bWZNTVVZMEZTREtReTQxSjRPQVBRZEtMeEdfSlh4RXBrVW9XanBtdFZBNEtJTE0zY0d1VnlKcGV6cW9PdktFOFF0Qm9CZ0tUNG4?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
