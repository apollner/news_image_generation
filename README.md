# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Oasis announce major reunion tour 15 years after warring Gallagher brothers split**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxORnVmVUE4ZzhNelNkdUdqUVRGT0dZWGQwZlQ0MUxmNC1tallwTXVRckx6dHRKeVVjUDFMTjRPdjAzUnZkaHVXeXZid3RTSkFRQ3huVGxUNUVVNERsd0pEVXhjMGdsNVdreklQZWtZZWhEd29ZRi1MMXRMZ1FzeDdFRnVjd2JjamRVdGpiNWdRblFTUVdiRlQtZFdoN1dGbzJNWndFSllzQ2dLQdIBVkFVX3lxTFBKYUN3blpoR0U3cFhHR25KVW0wWkI2cjdoQlBqQUl6MTQxMHFOTVNyMXdOa2ZUcUpWeGdZWW0yN0RTd3MyTjlacWxQYm1NQ0kzdmh2dERR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
