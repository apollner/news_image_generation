# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**UN Says Thai Opposition Party Ban 'Setback' For Democracy**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxNcjQwYnE0dkhkajBkWndxR0NSLUJTWHE1cFZobjBtWUJHRTZmbzhQaTJ3VGJBaUFDYVUtSndnTGFGVmZNU2JhbTZudVhmamk4N3BKMGhHN1R3bWtOTkIzUE5nVXZfZVdnWk5vdEtfSjNvRVZtRVgyTTFQY1p2T3d5YWVmdDBNVnZKcVYxUWZrQXoxajZ6RVItWkZ4S3VnZ9IBngFBVV95cUxPQUI4Nm1mTVdick9RWTg5MGw2LXVidHBzR05WNHZfellPZkYwMmlHQ2hFa19lVU1nc2k3X1hDb0FmajM3LS1oMmpGdkxSRDZta3VtYXVBaGhMLTRUUm90R2dVZ2VUekY5SDNNVTM4S0kyUUdpeFkxWEZvRFBfTE1tVXZmY2dOcWZ1akxwSDFTZGRZZG4yaDk1RV9YaE1HQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
