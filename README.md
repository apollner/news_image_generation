# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Alaska landslide kills 1 person and injures 3 in Ketchikan, authorities say**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxPazFLSERSVjFQSXZXUUpCQlM4dWlBSlZ6cVEzVV9DV2RwMXpYWklZTm9MM3dXV0pfN3phbklHNEs3TEsydDg4MmNwWmRMbXpoaDZhSE1DdTM2bjd1N2t4bnFhNlJUS1c0TWM2aHczQ1JFcncyVmVDZkFXZm0xRmVNcGNfVVkzbEIzYl9GMW5rTkNzYkh5dDBEaTluZlhIdm8y0gGmAUFVX3lxTE5iN0ZYczRyUUh2TzZNeVR2Y19LY1BJcmZocVFZR0QzLVdmeWlTRjFMd0JBYlhDTkFnZUVWSmlWaG1wYjFkdHNocnZYd20tbWo1c0NmTFE3U254c2NVLU5KaVRRUmplN3RzVWNESTh1Sll4elA0UEJwWEwxalE2YzZZcUNXYnhUSGdFR01EVGljaVV5NHFFUWtIR3FRYUhWMjA4VFlrVFE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
