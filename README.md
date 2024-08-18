# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mega Millions winning numbers for August 16 drawing: Jackpot rises to $464 million**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxQYVU3RlVUaVlqeDl0Z3NoWGEzR0hLZ2FSdTc1VmE1WG1Bb2h6eXJmc240WWI3dDE4Ny1CWUtjaFptWXBFR1NhZXFqRXFoV2thOHhvQkxvbEJiUklYUnNTa2FTTFhhOEQwcFNFU09lSFd2QzN0NXNvdVF6R0dfbEFyY0VGOE5fWnI5S2RNZ2dpdVF5LTRUT2ZlVlBVN3FteUU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
