# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**China's Honor will have Google AI features, including Gemini, on its upcoming smartphones**

You can read more about it [here](https://news.google.com/rss/articles/CBMiY2h0dHBzOi8vd3d3LmNuYmMuY29tLzIwMjQvMDUvMjIvaG9ub3Itd2lsbC1oYXZlLWdvb2dsZS1haS1mZWF0dXJlcy1vbi1pdHMtdXBjb21pbmctc21hcnRwaG9uZXMuaHRtbNIBZ2h0dHBzOi8vd3d3LmNuYmMuY29tL2FtcC8yMDI0LzA1LzIyL2hvbm9yLXdpbGwtaGF2ZS1nb29nbGUtYWktZmVhdHVyZXMtb24taXRzLXVwY29taW5nLXNtYXJ0cGhvbmVzLmh0bWw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
