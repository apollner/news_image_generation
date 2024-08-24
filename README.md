# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**U.S. will again offer free at-home Covid tests starting in late September**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxNTlBudVZwcWl0TXVaUXpGSDFPVS1RbllUMkk5RVpFM0NjVWx1MXA0N1RRbWxtbUUzRjJhUm9DSWtLNU1xS2o0UWVGamdoY0NXekZwMURJRkYyLWhIS3hDNlY0U1dBZUxxTVFzeG5jdEI3UXRYYmZTNV9VQzBiRnFUYW5BaFRucTdlRmtWQTl1cjZQRmNIeklDSkMtVDFtOHZwUldxd2NXY9IBrAFBVV95cUxPNWtqcDRwVUlZbHNVcUJzT211X3BqYTJPQ0RWY25yMHVlb2JQdnc4RXp1VEhJdFdPNVBPUGFKdUpKLVRfYnRsTlBjcmUtTHp3bkFKX2YwX2EycWRnbl80TVowVE1DSXRYaHZVV2RTTHYzUnNXbGVLaTZzVmM5a1doMkNXbDNiVTBrVHlxbEFpWmNISERLUi1vb0ZQUngyX3JmR0VzQURTaWJYNi1K?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
