# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Far-right rioters attack asylum seeker hotels in UK’s Rotherham, Tamworth**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxORVhXaVlKWGhFdzVoTDFCcmtLVkRDeHlMX09TYzczYWpPR25LSF9JRk0tUUFJXzliUUhORFhVckptbk1ONHZxclc3d0RzWG9yRkY4cnczdk8tMi1KOU5IT2RiZWNRbFZJYUx4S3hFdmpWU05XekI5eWZySjliVzBjMGpyMmNOZ2plSUljTmJYVElQNTN6TGpFLWNGekRaa1VU0gGmAUFVX3lxTE1wWDRoRldjYnNkSTZYbFJHRzhaVTZPSDJrOUFaYjZHZFNNRDJVeGF4X0REUGphZWxLbGhZd1pqQ1pwdnRJc1FZR05BZlQ5TFJwQkVwSDlKQlVLY2NCbWN0dkFtR2VlVVNBd19ISk96WndlM3FjVUZLU1NUblhLejByejI2OWJ6eFA3Zi1jN1dRbkNPcTdIMWNiYUdiZlVfa0NrSUJGWUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
