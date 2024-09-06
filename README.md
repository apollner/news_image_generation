# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Pope Finds Fervent Fans Among Indonesia’s Transgender Community**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxPczBjMXNXNHV3NU9mSVVmWkFuT2lkcjlMOWNKRF9DRGlkUHJKSl9TMUgzSTVLam1PdmNoX0VDc0tibW9rNnVwYmg4WVlIaTZmdDdnQmJKMlU4RjN2VHExR2xnN2JaUHc0bktkTDJuclA5NE5Nb2RveFdfNXFLRE1vRVBic0Z1YUMyTHZUT1RB?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
