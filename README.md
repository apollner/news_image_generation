# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**U.S. wins first gold medal of Paris Olympics at men's 4x100 meter freestyle relay**

You can read more about it [here](https://news.google.com/rss/articles/CBMiYGh0dHBzOi8vd3d3LmNic25ld3MuY29tL25ld3MvdGVhbS11c2Etc3dpbW1pbmctZ29sZC1zaWx2ZXItYnJvbnplLWZyZWVzdHlsZS1wYXJpcy1vbHltcGljcy0yMDI0L9IBZGh0dHBzOi8vd3d3LmNic25ld3MuY29tL2FtcC9uZXdzL3RlYW0tdXNhLXN3aW1taW5nLWdvbGQtc2lsdmVyLWJyb256ZS1mcmVlc3R5bGUtcGFyaXMtb2x5bXBpY3MtMjAyNC8?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
