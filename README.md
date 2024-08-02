# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump spars with reporters at Black journalists' conference over Kamala Harris' ethnicity, immigration and jobs**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxNdldGT3JORUJCSk5zbS00TnhpSTV1Z0I2cm50MTVLSzFUQTNaQzIweGtBLVZhTVBpTmlHMGc2NS1oWVd5dm9US1o0SU9CVUF2MlREWXFWTm1YZWZKYkpJLU1sNkZmSkpBdW1GUmVuSHhwanJzOWpia2FMZTU2TkQ1Qm1NYVpMbHRud1RHQ3hlSEppMkxFS3R1eENWSlNMMWtmWTFjZHhOSzk0NTZiMkZIdXhwLXNQdlJxLTBN0gHAAUFVX3lxTE1sZGNRMUsxd2NER3k0NjZFVUIyUFFiWW9MajB4Zk1nMDY3eFFRb3hLLWplaGc2N1V4d1BxeXh4ejRDeVZFeU9zbEUwSmVEVERHYjNDVnk1cFhNMGJYb09URUtvSkRxYTBYbFE3RjQ5eG1sSlFaVUloZ05iejRPUzkwVGhvR0FfenVHc0ZuLWhoTndjcG5tUkIxb0lHaVpBaEdUanhCY1hMTjdMTFVybFVvczdMdTFHQmtnYmZ0Z1pFRQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
