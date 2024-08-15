# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Why Starbucks Fired Laxman Narasimhan A Year After His Appointment As CEO**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxObjR2Y3ZhOXgtZnkzZFFmVndaMEZ4ZWFLazAyVVM1RWp0eGlBQWR6eENfMHMtc3d1ZFFkNVpRSUp4RS01NTJLVEN5X09SZXdTeWJwVGZESGY0VlZib2FrX3llYlo3VHpfZkM3cWhrQmpudjA5dG1nYWRzcjBIOF90XzFEd0N4eUNjMEFRb1d1cGhydXN2UHQ0eU9aM2xZOEVqMFlLTGZaLXNEaEJzc2xPdHhJNNIBuwFBVV95cUxOZmdvTjBsS09HRzVSWVYyV3RtQXVPYmFZRWdVRy1tNmNFdGJUeW53eEFzNExvemhfdmtjS2M2bEM1WmxHTHM2UW1pam9lbkQtT0pIekNmbng2MFJHMFo0WnpXY3poZzI3U2d6UVhuUFExUkttSzEzVl82cy15TDZGUUZIUW1wVVFRWjZOTUhidVloZGI4NnN3RnA4dE9RVVZRMGhOMXdhN1NVTEhoNkkxY1dWbkYtZ0pnZ2Jz?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
