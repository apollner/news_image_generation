# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘It didn’t happen’: Becky Hammon denies mistreating pregnant Aces player**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxQNmg2WmJHcGZqZnVXMXBBVFR5YmVESFZ0ZzFtUktmdC1mXzYxT2dnVW90a3RwMUhfNDMtQm01YmNBc1dQRU85OTRvN1lkc1VfTmRoVkVMZEVnU3JvZkJXVW1DdU5hRWRDSWVjS0RGMU5SUHFnNlJIV0M2b1pmSndKbHJpZkNtNFR0Qkl1TGFldFlIUEhGRjd1bExFX0tOT0VIak5sTE9zYXI2UXNueGh5SVQzdHlaZkxCOW1wZkdVVQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
