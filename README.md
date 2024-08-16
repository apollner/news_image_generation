# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'I see a lot of denial': C-suite advisor says business bosses still expect a Trump win**

You can read more about it [here](https://news.google.com/rss/articles/CBMinwFBVV95cUxQWVIzX25GamkzdXp5YzhBT014UW90bFY4enpxcXMzRFhXdHVEbG8tTUxUY0p2Tm92YUYtOEJ4QXd6TFFIUkd3SVAtbk1CVlpkcnp5QjUwbG5veTJnUFA1Ukd1T3U4UUhjRFhPTmVtTS1YUVBqR0NvSFlmMHFzWDZWdGlXSWduWVpFRU1aUS1nY2l0NnRpS1RKYzh3LXZhdUnSAaQBQVVfeXFMTUxZVjNPNE44aFQybGo3eUZfY3hRX0VFVUY5QnNnYWlSWWJsNFJTSEFsNFRBT2hqSzVrcG1RTndlLXhpMW1MMFcwNTZodlhManBXMkh1aEo4SGZLcDNBZVdmNk9mdHVBYkV5UkMzZmxPcG45VVJMU2hkc1RpVmhmTF9pMURGU3Q5TUJtczFqdHVOTkpSdXJHVGU4cXVUTS03MkF1S0I?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
