# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 Open Championship picks, field, predictions, odds: Golf expert high on Brooks Koepka at Royal Troon**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiQFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL2dvbGYvbmV3cy8yMDI0LW9wZW4tY2hhbXBpb25zaGlwLXBpY2tzLWZpZWxkLXByZWRpY3Rpb25zLW9kZHMtZ29sZi1leHBlcnQtaGlnaC1vbi1icm9va3Mta29lcGthLWF0LXJveWFsLXRyb29uL9IBjQFodHRwczovL3d3dy5jYnNzcG9ydHMuY29tL2dvbGYvbmV3cy8yMDI0LW9wZW4tY2hhbXBpb25zaGlwLXBpY2tzLWZpZWxkLXByZWRpY3Rpb25zLW9kZHMtZ29sZi1leHBlcnQtaGlnaC1vbi1icm9va3Mta29lcGthLWF0LXJveWFsLXRyb29uL2FtcC8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
