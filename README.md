# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Jerod Mayo on Matthew Judon trade: “We’ve gone years without having a premier rusher”**

You can read more about it [here](https://news.google.com/rss/articles/CBMi2wFBVV95cUxPS0pSWUNfd0ZfNzdfX2VhS0Y3R1dMdUxjS1dVcWR2UzVDNU5xVDc3WjltOGZoZGZuNkJPMWIxUmtya1EtUG5zY0hxWFRNRkQ5bzQ5TlhaTG92TUxoU3I0Ri1MUC1ueE10NGcyelRuOUNMdklEcGxTVFZoQ3JzZFBOLU1CRXFWTjhyNkNaYUdQQl9KX0N5OVEwOWJnalk5Rm9uSDZTckVOSXE5ZGE3OVZHcjgxY0FRSnhDXzU4QlpWeHNaU2J6bVNBQ08xQXh2R3N3d0cwVm9saFBneVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
