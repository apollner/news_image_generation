# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Six people missing and one dead after tornado sinks luxury yacht off Sicily**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxPM25HLVJUaXFkdHE0eDZKVlZONnQ5WUYtWkZmSm5fZjZlNjVVX1k1OWROM1lnYVFadUp3UHRsUjl0RExPLS1BSDNUVWl4YTdWZ0pJTWxKRU56bW9WUkJyak9iWXpZa1FReVpOVUM5S193WXUtWklfWUtYNTJycGpocXd4RUV4MDNqMkdxa05fUkdCVlFvZjBMYWZQc9IBkgFBVV95cUxPc0JWR2MzS1FzSUU0TVVWakhLdjlOaE5KSG01SW84WWVvNWpPNVNNUkdzNkhSN2xzVTZ0ZFlGbkNlWWttdENLQ0tjb0daZ0RLSmtBY2dOMXZ4bHFsdGdteTZEblJwMTEwaDhscXRUT2FBNEJtM05JT204TXJ6d3QzZjJURkdEbXROeFpDUmZoaExtQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
