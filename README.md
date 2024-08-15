# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Men’s cancer deaths expected to spike more than 90% by 2050, study finds**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOa3F3LW5qOGp3dE0yT1VWYWtIZWdONFdPX01GVXNjQS1KVW1ReXNlM2x4cGpkTmRMUV9XUWdfbWtFbnJRY0x1VnRITlZxeUFUYU5EYW1VVlFwOVNKQnp3d2wwUlR2bHhVZ3M4VVVBSkJnekdjZ3dSRXVfNEZka1ctNGo1Si1lOE5L0gGOAUFVX3lxTFBsWEpYV0tsV0RLNXRSTE1SLXpCb25HbmRjRlJ6cG53VFdaUGxVYjV1SnZVYXBESTVwckNpenExUF96MVNXVW5BZ0M2NFBHQUI4bnl6SjdKdkJ6Ym1fSlNfVGI4SUpGVE16ZzctRUJCYzJGZlZVUFQ2clJJeTN5NDhQLTVOc1dyMExkeW1NbUE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
