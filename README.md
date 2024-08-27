# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**China Box Office: ‘Alien: Romulus’ Becomes Hollywood’s Second Biggest Film of 2024**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxPX0RMdW9QVlduMDJxZVU4by1jQzFKb1NPak9oakZxaTRXa2Q4R1VtRGlBRC1YLS1rRVZSQWUtbHM0OUZIYXVQVGs4YVI1VEk0T0t5eFcyTEI5d3BMN0VkdTgxVFpIblJ0WUsxel9wS1RvaDBEd1c2UElfZnJhN0hUQm0xVDVYYW1MQVBXVmYwYkdoUdIBlwFBVV95cUxOZnBldWMtdURscFdkZURuc0s2WmlNbHJvamFWN3RQZWZTdFNFSl9Cemhpall2ek9ra1plWlFZS2p2QVkyNDlMblQwMFFBeTBCQUQwSTVGSXJ0MHVDT0c3Z1ZxTUtmTDc5SnhpNkVOZkg2UzBiWDV6Qm1tWGxxMFlGNnZiOG9kREdBeFlhcVgyS1Q4ekJxQ0Y0?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
