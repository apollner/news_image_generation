# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**The Obamas return to their hometown to get Democrats fired up for Harris**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPbi1DTWx4NTVFUGxYcWdlRnltcnh4anRrWm1aVWIyMlhHa0dUODdtUzRUZW9IOENyRFNjdTFwWkVYai1sRm9ZVnlydjlDSkoxVnJzRHRMeGlFZlctVkREbmt3bFd1RWY3d2RUT21ncVJpRmJmLVF1WEFIeHhuajdtR1ZfOGNvTUJxT0I4WnRHYTYtUlNKTXdTb3FfZG1RM3BEblBiNWZ1SkTSAVZBVV95cUxPVUxXZTJEMU1kUEd3NS05SHZSc2pIR3B4R0pqX1Yya3ZBRXRfdDVYYnNXWklWOE1KUzhmSlZXNkVfNVF5ZW1BRVB3d08tUTVZdmlDQUpSUQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
