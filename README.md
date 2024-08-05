# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Violent Protests Grip English Cities in Wake of Knife Attack at Dance Class**

You can read more about it [here](https://news.google.com/rss/articles/CBMihwFBVV95cUxQeTZTaWdKNHJJZTBFaXg2T3pQZ1d4cVAtSFNPLUJ5bTE1OTl6TGVIRGNyRnlOcGVUWDNhZTk5TkQ3WDB1ejF0Qmt6LThFRTA5TEV4UXE4Y25UX2ExRjg5YldmdGZjUHZZRW9remgxVUF4Wml0aS1xbU1mVDA2OHo2WkFjTGZYQzg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
