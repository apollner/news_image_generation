# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Prince Andrew faces questions over links to accused Chinese spy**

You can read more about it [here](https://news.google.com/rss/articles/CBMijwFBVV95cUxPZTlOYjZtZ1RWUExRaGFJNzU3aFlKRjFZTDBSUmhjeWZlcDFqLU84TXFWNzgtNEhsOUxmUk11Z3NNYkxsSm15b2o3eXZ1eEE4V1NyZlo0aGVrZGJIZVlMZDRRZ1pVdHYzR1lmM0dvZXIxWG9TSGFYQ3p6YnBndG9vdzlSa2MyakdrRTdVY2l1RQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
