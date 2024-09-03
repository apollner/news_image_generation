# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**BYD sales hit a record in August despite broader China EV slowdown**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxQdWRlejB2RFFPVUpjWTNJUFUweE9nUUtTVHI5akhGamlsMmZ4dVNpM0R4N29uN3NrdTEtLVgwbVVnUjEyaS1ybmR5RHRzWFFZLWRmeEtTY3hUeDIyd2hsbUI0aGpZZGttTXZMa29SRXpfUF9rVi1hdGczeDFYSUo0Zy03TkQwcGFwMjZpNU9ZVVFDVm9qcGFwaERVbmNPZjk5N1JCVWdR0gGrAUFVX3lxTE1QMHAzSTAzU0Y3alFMYzBKdTktVXdiSDdBajBmbnI3Ml9MSWZvTmRZanU4TUMzRHRLdG9KYTNlQ3VDUVhYWndVcjI5dU9WdGJkYUJTQVhDZFprc0dQcXVOanVIb3dZeV9XTjZqV1BHZzllQ2szT05oWjlyalV5bXN2U1BvZy05SzN2ZExacG9jM2c5d2JnWjBZeUxxVjY0WW8tU1B6NHZtSm4wYw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
