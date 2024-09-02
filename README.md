# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Germany’s far-right party AfD set to win one state election, and is level in another, exit polls show**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxPYW1SOVJ0QnhLRGF1Y3JCVGR2OE00MVNpQThjNHpoRkx6clpvVF9ZSGY5Q2ppb1Fkc1VTdW0xUjJrZDJKQzFUTWwxRlkyVVpzd2tVeHlaNnplc29taUVacXYzeE1rdDlKSTJaWjRISUFhaURGbnlGVTBPWWlrUmdfZVZ0WjhvX0hVSlZyOWNnSlVRQmlDeGtWUzdUTkc2cHdB0gGXAUFVX3lxTE1KcFNxNV94anZaeWJVUmcza3FmY3VTQ3ZvczZDR2hqQWZRX09vYlFhYlRoV2pOOGxGMmVPTXg5MkVFOTZfcmJ4VXZMYzBvYTgyMDlxSFFyUlRGOGhTNHp1X1BGM3dUa0lnYmxNY2YxRXJCcGd5ajU4dWpseWN6TTZ5bk01ZjJIT29iX3BpbVhWZGV3S2ROM3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
