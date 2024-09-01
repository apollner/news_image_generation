# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**US, Iraq team up to kill 15 ISIS operatives in early morning raid, US military says**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOdHlJWlBKYnEtTHM5UFFsaEhmQkhCOWNkOWUzQU52S2twdXVLV3owT2lKM2w2THNnS3FzVXVJd241ZWtkcWRyNEg3c0tiTUkteC1INzJQUXpzbFdoT1V3XzFwMG5RaVdBVFdFbi1yS2xiSUd1VV9YUDc5QlRsWXJRMGVqNUgtT3BFVlBQY3p4M003RDBDVkkxd0NNNXpSeWdJbUdGb291OW_SAa4BQVVfeXFMUExHMUdxcUxjRGJienRNVEtzendWNVdVaW13MXNXWE9zbWQzdWxrblk5LU9fOGc0ZU9tenZDcnhMVFRlOEtPSnFRVi1Scl9yb3VDMlY3VFVtclpCWlJyajFCdWhjTVNISmpJZkJtT2JzN0R1Z21OU1JqVTNpejhJN2ExSWxjd2tpTkdrdjJ5NjROVTFRQ3A1dnZsaDFYX3huOGJhcUhmTjY0aG5HVVNB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
