# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**DNC backs virtual roll call vote for Biden as outside groups educate delegates about other scenarios**

You can read more about it [here](https://news.google.com/rss/articles/CBMicGh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3MvYmlkZW4tbm9taW5hdGlvbi1yb2xsLWNhbGwtYXVndXN0LW91dHNpZGUtZ3JvdXBzLWVkdWNhdGUtZGVsZWdhdGVzLW90aGVyLXNjZW5hcmlvcy_SAXRodHRwczovL3d3dy5jYnNuZXdzLmNvbS9hbXAvbmV3cy9iaWRlbi1ub21pbmF0aW9uLXJvbGwtY2FsbC1hdWd1c3Qtb3V0c2lkZS1ncm91cHMtZWR1Y2F0ZS1kZWxlZ2F0ZXMtb3RoZXItc2NlbmFyaW9zLw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
