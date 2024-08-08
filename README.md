# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**After a rash of stolen cars, Hyundai and Kia’s new anti-theft software is showing results**

You can read more about it [here](https://news.google.com/rss/articles/CBMilwFBVV95cUxQOFlFY0pHQXBlYVBWd2l0LTMzVDlnejN2NmlRS1l3czdJMm1pYlAwVG9VWEhLMENwSUtneWtEYXhVWXNqWTBPcFFpYV9MMjEyRTZSeVZueXZvekJzUWIyRi1YQ2RFaWs1SVVpMG5aajdsNWhYQnRqeUNzejU2d0VLUVk3NFJ5UGo1UjBJeVN6Z0pNVldnOE930gGOAUFVX3lxTE82STRrMnY4WnFiUjRvbnVuSFNLLWZ0RGpqV1lOOHZic0g4Ul9FRGt2MTdrWjdlVmNBamNNcUlsQkJjYXlocmNWWW1rMUFPbDBEb2FvSTBmVkdTTlF3aXo4Wkg3Z0s0Uk52WmU1cWJJZ3l0TzNVUDhFVlBRQk1TRXRPY1pDUTZiX3o2Vkg0b2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
