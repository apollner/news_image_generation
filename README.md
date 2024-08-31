# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NASA finally gives Boeing Starliner capsule a return date. But it will fly home without its crew**

You can read more about it [here](https://news.google.com/rss/articles/CBMingFBVV95cUxQejhoOUhROTZsWG8zalMyYndlV05hZ3hNSlBIOGlUQ1BtYzJzVFc1TEI3Q2JPNFJCSE81SHF4aTR5U19WTnpsRGNPeFZYNG9NUEtEblE0NWhxSlJsVXdWdGRCZ3N3T1dQTzVLRXFUd1IwaTlXNm8zV3BzeHdZUWFUZDhGT1ctUFhUS1N2aTA3dF95YjZ4OEJhd1g0YnctQdIBlAFBVV95cUxOd0Fza19GTTJLVzI0dE05OEoxUWZXSkk3d3c5aGlWS0d5Q18zM0lSV3dvVTliZ29rZlVkNFJ2Zl9VOWtVQVh6U0sta2tJcVlIZW9YZXlxX2pBZ3Y4UlAwWFlKeDBBNVYza1FBS1NBTi1mckhHX3V3WmsyQ3VXMmZKYmJtU0JZM0tXV21uZWNJd2lWNkpU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
