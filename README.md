# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Country Singer Rory Feek Marries His Daughter's Teacher 8 Years After the Death of His Wife Joey**

You can read more about it [here](https://news.google.com/rss/articles/CBMieGh0dHBzOi8vd3d3LmV0b25saW5lLmNvbS9jb3VudHJ5LXNpbmdlci1yb3J5LWZlZWstbWFycmllcy1oaXMtZGF1Z2h0ZXJzLXRlYWNoZXItOC15ZWFycy1hZnRlci10aGUtZGVhdGgtb2YtaGlzLXdpZmUtam9ledIBfGh0dHBzOi8vd3d3LmV0b25saW5lLmNvbS9jb3VudHJ5LXNpbmdlci1yb3J5LWZlZWstbWFycmllcy1oaXMtZGF1Z2h0ZXJzLXRlYWNoZXItOC15ZWFycy1hZnRlci10aGUtZGVhdGgtb2YtaGlzLXdpZmUtam9leT9hbXA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
