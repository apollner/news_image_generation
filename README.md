# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Video: Patrick Mahomes Completes Behind-the-Back Pass to Travis Kelce, Stuns NFL Fans**

You can read more about it [here](https://news.google.com/rss/articles/CBMixwFBVV95cUxNZ1JYTF9RSDlOblFjN0pqemtkTGltRjI5U2RyWThKTXN4V1dSci1pbTMzS3lPd1NpdXpjRzhnbW5RRU5BM2tISC1zUFhvZGloVFppbkZSRkw0ZHBWelY3U1MzWjM3Q0V5aktOdmMtc1FOTER2Tnpwa25VdE9pZHJEdDlLWXNpZnI3cS1mMS04YUJQT25ZT3l6MnNwY1VSaG00UTdvVENydFNueHJKUHNQMVI3bW5YRVhyTXFNcWJtR0d6QUFMYzJn0gHcAUFVX3lxTE90YmNOUGFiN2NwYlhyZE96Y3J1TzNNR1pJdTJKY2VObWI2THdZUi0xRFR1X0N1X19SMW9CbW1XcUc5VExjclFKMExKeHc5Y3M1ZEN6X1RHdnFQOHQ4VXJyTTBHZ2d5a1V1cHNuLXRvQW0yZDRfMm1zRUpfb1ZPWEtaM2dXVFQ3a2haWHozZ29FekxDWXFzYU1WUXFTXzBMWE9fRmtKMElEc01EV1pMa2xpZzRLRlV0cTE3bVNoQVkxaml2WmpSaEg0bVRRdFNUS3BpdzFZZ3NuZ0ZlcFE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
