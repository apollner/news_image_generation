# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Aaron Rodgers, Garrett Wilson downplay animated exchange during Jets practice: 'It's about winning'**

You can read more about it [here](https://news.google.com/rss/articles/CBMivAFBVV95cUxOVU5XcUhnVHNwanpYVERPMlUyZ19SVC1KZUotX0dNM1k3dGlfbkNXZGZNRm5pOFNIeGNmVHZKYlNqa2wxcEZ2eUhXV2RkTzBJODJZYzBnVlcwckxCNlQ5VUczcnJHeDlBZGEtTlNKbl9LemVnOVZJdGR6UTFWWmJBdzBQOGl3Y0xqTTNGX1paNF9ISjk5OXRYUjFkUXM4N1JuZHIzUVUwV0RJcGdEYXZ0VS1UNkt6b2xScmt5bQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
