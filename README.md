# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A16z’s Joshua Lu says AI is already radically changing video games and Discord is the future**

You can read more about it [here](https://news.google.com/rss/articles/CBMixAFBVV95cUxNaDVhQkdPcnEzZUtZa2JldkRmOURJWlZheV8wWXVuZlZER2xucmdabFl1UXJ1RGlVNEd5WkhPb09PbU8xTElvMDFiS2U4OGtMTHdLcFhkcTRBZzN5SHNUVDNQYW1sU0wyOWtnTm1meUhXdHZWYTB4QV94aS1CUk5lVEY3cm1MMGFYYzY1bkZDVEQ3RUhIaWppSlZMZXc5WnRjNHBWdUFJbU5TejR1VWd4TlBqZ0M2VGMxd1ZVLUVpZ0lmUTRz?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
