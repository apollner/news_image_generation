# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Plane crash in Brazil's São Paulo state kills all 61 on board**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE5QaGtEWmE4QzBpRmtNb0JFX215Q0w2N0F6OF9fY3ZybXV3U09JSGxBZUczeHJwVnpIVEJyelV3akNkWmpnR3doNFU4VU01RWFWRlIxQW5aVUstQdIBX0FVX3lxTFBCeVJadVoyYk9Kdl9ORzRyeWdrY2FHMkQ3ZGItYUxvUXc2Yk9LV3FieHJHbjN0ekYxNXJOQzhCM3FiQ0cyVG5SRm5NNzFza0tRcUFVTmRFT0NmOFpvMTdF?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
