# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Deadliest' mpox variant spreads in multiple African countries; know signs and symptoms**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgJBVV95cUxOM0NxUWpKWjY2d012MGlkZG9jMEJlczZjZEd0bEd6S0FHZ2I3bVBkcmM0VTU3SXkwU1VkZmJjMk1rWVJqX09DcG1heHJfWEVmMXc0Mm1oVmYxdHFQRUVPd2UxSm5wZ3ZRTS0xN1hBWlZFY0lwLXFzMVQ4SVAxel9rZXl1dXBHcDllYUtKaXZqOWlPX0VTNDEyZUdFTzBZb0RCSk1HS2JSZE9hLU4zT1dkZkxRSVNmOHpqWVFJMXVDb0l2TmMtVFh1ZVNtTVo1Zi1xMkt5RWVMUFVZUFF1cTg1SGRIdXB1a1JHZVRYNUU4MVdjaTZKVzNCdDI4NEE1Y253TFJ6VldyYk9mekRMVnR4U2xR0gGXAkFVX3lxTE5EVkU3MTl0Ylo5TU4xRnJSSjQyUlI4MjhTWkliNDZlZl9kZ3RqUy0yR09UaW1vTTltRldyX21PV0VWZlU5Q2xYUk44bHdHeURVakJhaHdQR3hEbkdPNDRfQUZJQVdEVG5hc0s2ZC1GQzBjSDJETjRqM0dKQzZmd0h2eEdJQjJwUm9hRFdMSmRUWVMwTmRuWU54M3phU29Na3hSaVFYT2lwTG5SXy1tRjYwNWxicHU2aElrbjBZZEdVMXFsMHZLc3pLMEpsbG91VWxURmw5bkNDWmNabTBQQlNLNk0wOFRIMGk0VFU2UWx1Y2NNZDhNQm5BMTU2ZEE0dlpYdHhxVmliNnplRFpyT2VtZjNJUm03MA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
