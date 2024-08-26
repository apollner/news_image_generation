# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Stephen Baldwin reacts to daughter Hailey, Justin Bieber’s baby news after model said she’s not ‘close’ with family**

You can read more about it [here](https://news.google.com/rss/articles/CBMiowFBVV95cUxNZ2h4NGdEaHR1NHcwZDJ4dEFlanA0RC1Na0xReFhhdm9oYjh6cnA5bDVQdWpmOVZJV1VaTEpXbHhqbFVLclVDM3RjaUl1aTQ3UFVFVE9YSS1YSlZ3ZUlxbUdMNjFrRnMwSzJ2N0JfNHhxeU15Rk40UG5RRXlmaXhtSFhLSHZsQWgySEJMY3pGLU5qZHhvRE51a1FfcHRFU1F3Tm8w?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
