# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Lady Gaga flashes megawatt engagement ring as she and fiancé Michael Polansky arrive at Venice Film Festival**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3wFBVV95cUxQSEtRVGRURFR3bklic084dkZqekhRVVNMMnZWaUNQRWoyYTdfZlVsbExPVFJ0cU5jRDNZOWYyQS14eUlsTmlXVGM4UEVRbUxhaWVqRzRrNTBTcXQ4RWE5QUFwbFNqNEFTUlF3bGVFTHU3X01YUHV5UlJ1Ni1DY0k1cTk5MkNIYkpPQUMwOWFpX2xDZTN6cjgzRUJWQTNQUXluQWhMaVNHczZZaE9jRmotNEtfWjh1OHdRUENBdGszRkhzdlc3XzN5YnNXWDF4aU1uVk5NTW5OUDNWVnJ4UUFv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
