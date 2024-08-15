# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Joaquin Phoenix’s Last-Minute Exit Sparks “Huge Amount of Outrage” Among Hollywood Producers**

You can read more about it [here](https://news.google.com/rss/articles/CBMimwFBVV95cUxOZUE2bDV5QnY1V0ZveUxiOVQzbm96WUNqZ2xsVGMzM2x3T1F2RjdUZ2dYZm1KcnU5TnRiVzFLNGhIS1liM1B1ZGJQZFRaUGpwT3VxUUthZzV5M1U2YVRZQzlSUU1xbnR4eWpGRjlGR2xZMWswZ1VyRDlHTVFXakFidnFCVnRhOU9pUlBURXBhZFhCS0JVekhQa2cyY9IBoAFBVV95cUxPamxKNGN3ejg4aUhsNlJEeUx5MWpiV2ZScThJVDNtVEVHQ2VCYXpNREtoT0UxeWpheG1fV3ZJOV9tRjFlYVZjRUlkYXZsWXRYRi1wTjNqeFpMR2l0MWJfZGNtMWg2NUxjeEdTY3hyUjB0SGFTMG5ncUpSX0JtQjdfVlc1LVBYMzZkeVBmenBweFRaQmc2cUVxRkpBak9PWG9i?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
