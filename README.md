# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**German police hunt attacker who stabbed 3 people to death at festival**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxPOVFfRXVGTm9zM3BUakhraHR3Y2pOOVJnZjFHM3NUUkNGMW1QRmVGZ0NZeEFsYXdjSjJEeF9RekczVkV3UWlwU1dlQm8tWjcxejNuU25rbWY4MFF1cEtRRS1CVGRlOVVTcWQzZE9GZy1kekRKZEFTeEViZUI0ZTk1aGllTjJQdDkyaGpxOTFob2prOHRSTnVV0gGOAUFVX3lxTE1fVF9qQW5udlc3RzBMUUhEUUJqQW5CV1lmdFlwbnd6dWd6N1hVMVBTWktzWnEtVkpWdHhpY2dsdjVvLU9jT2ZMVnBJbWRiaFlFbFJfanpiWXlNa1o0a3hhNG15SW4tSzQtVUp3a1VvdnVtMGNGU2NOck9YbGU3VmY2SllycldaOHZMRVh2bUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
