# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Israel's Netanyahu appears at odds with White House and Israel's military over war with Hamas in Gaza**

You can read more about it [here](https://news.google.com/rss/articles/CBMiZmh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3MvaXNyYWVsLWhhbWFzLXdhci1uZXRhbnlhaHUtd2hpdGUtaG91c2UtaWRmLWRpZmZlcmVuY2VzLWhlemJvbGxhaC1sZWJhbm9uL9IBamh0dHBzOi8vd3d3LmNic25ld3MuY29tL2FtcC9uZXdzL2lzcmFlbC1oYW1hcy13YXItbmV0YW55YWh1LXdoaXRlLWhvdXNlLWlkZi1kaWZmZXJlbmNlcy1oZXpib2xsYWgtbGViYW5vbi8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
