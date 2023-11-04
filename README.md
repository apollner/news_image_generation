# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Prisco's Week 9 NFL picks: Chiefs drop Dolphins in Germany thriller, Cowboys edge Eagles in NFC East clash**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL25mbC9uZXdzL3ByaXNjb3Mtd2Vlay05LW5mbC1waWNrcy1jaGllZnMtZHJvcC1kb2xwaGlucy1pbi1nZXJtYW55LXRocmlsbGVyLWNvd2JveXMtZWRnZS1lYWdsZXMtaW4tbmZjLWVhc3QtY2xhc2gv0gGPAWh0dHBzOi8vd3d3LmNic3Nwb3J0cy5jb20vbmZsL25ld3MvcHJpc2Nvcy13ZWVrLTktbmZsLXBpY2tzLWNoaWVmcy1kcm9wLWRvbHBoaW5zLWluLWdlcm1hbnktdGhyaWxsZXItY293Ym95cy1lZGdlLWVhZ2xlcy1pbi1uZmMtZWFzdC1jbGFzaC9hbXAv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
