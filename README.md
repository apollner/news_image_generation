# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Fever’s Caitlin Clark breaks WNBA record for assists in a single game**

You can read more about it [here](https://news.google.com/rss/articles/CBMia2h0dHBzOi8vd3d3LnNwb3J0c25ldC5jYS93bmJhL2FydGljbGUvZmV2ZXJzLWNhaXRsaW4tY2xhcmstYnJlYWtzLXduYmEtcmVjb3JkLWZvci1hc3Npc3RzLWluLWEtc2luZ2xlLWdhbWUv0gFqaHR0cHM6Ly93d3cuc3BvcnRzbmV0LmNhL3duYmEvZmV2ZXJzLWNhaXRsaW4tY2xhcmstYnJlYWtzLXduYmEtcmVjb3JkLWZvci1hc3Npc3RzLWluLWEtc2luZ2xlLWdhbWUvc24tYW1wLw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
