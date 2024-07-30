# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A star is about to explode. Here’s how to watch it**

You can read more about it [here](https://news.google.com/rss/articles/CBMiW2h0dHBzOi8vd3d3LnNlYXR0bGV0aW1lcy5jb20vbmF0aW9uLXdvcmxkL2Etc3Rhci1pcy1hYm91dC10by1leHBsb2RlLWhlcmVzLWhvdy10by13YXRjaC1pdC_SAQA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
