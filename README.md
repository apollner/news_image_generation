# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Projecting Aaron Judge's career home run total: Where Yankees slugger could finish on all-time list of legends**

You can read more about it [here](https://news.google.com/rss/articles/CBMi3AFBVV95cUxPc2ViY0hTNkw1bE9VdzJPU01sSVVHeTVjU3ZKZjJMQndlRmpXTnpZZjZtRTZ4V1NWT09DZjNKcUcwdlFPdDhMMk5lNnU1dWpEWG1HWURaaWMxNmVnVzUzUkQ4WVRXd1ZZd0N0NXo5aUk4ODhFbUcwODRnVk5UYzlnUGN0WU9VUktQTVhuYXFONDJXOE53d3dqOEhfOGZtZWxyeHlzbm9kY0hWZmgtTHVJbWpfNktmVjhnVmFqaXE4b1V6Q2p3Q3A1bU9oV3h5RG15c2hMZVk3MUdOWm8x0gHiAUFVX3lxTE1rMEdlVGhPQjRjT2RDS0x6VFRPZDJhSXlpbmZVeW9DVlNhR3Bhc2pZVjVJWHFXVU9NVjBRTFdYSVNyc3EtcDBkTjhJaEdqY0hhOTIxTHdHQWRJZk41OHRYSndvVldZSWh2V1J5OHhtQjJ2a0hKUWNGRVFFZ3lZUXZBbE1SNUdvbVNianVMM3o4QUtvLVMzdG92UzZ4UmluRGkzNktOWTlJdU1NS1RjV1JVRzk1NktXbUY5a2lLNjZocnlZeU1pNTdieG9hSWhJbXFhVGZvdzZ4Y0RXNG9iZnRiQWc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
