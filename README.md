# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump hires new aides but defends his personal attacks on Harris**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxPZ1U5ZlJOZ2UwUEpFWWFoQTE1SmUwOEVxSnlVc0tlZzJPRXZNMGNlV2xaRkpKMzlONEk3ZkFyMkp0UUhvQWhLemZpMmdJUG43ZWFKbm1lOUN2T1FVMUhzaWNnZGplM2FuNU85dmNROGhhdjktbFB1ZEN3NlVFVlJsbXdtUFBWYlhhVDVPV3VzcTkxZw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
