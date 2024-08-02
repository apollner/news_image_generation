# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Gen X and millennials have greater risk of developing more than a dozen cancers, study finds**

You can read more about it [here](https://news.google.com/rss/articles/CBMicEFVX3lxTFBpZUQwc2JwVG5pb21DYXg3a21tdVBaTjFCZllXcnkxUnZ6cmZUa0RzN1A2eV9ScTB4M2JHZHd0MmU1VktmMlN1b1JFaXNqM1BadmUwTVVkaGNzb2hDTS1ES254eFNBRzNaQXR4eFpmcmPSAXZBVV95cUxOUkNWUWszMDNQb0NlNXh1R20xQS1SblY0dnFpTWpSSEZrZEZmSjlaemE5TjZqMk55eFg3LXM0WXZTd0d6T1JtS0RNZzdSc2xvRXdHVnp4c3FHLXJWVDVZX2tyaVg2cm54RXNJTlZvaG5SU0JfVTF3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
