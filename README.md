# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Mortgage rates plunge to the lowest level in more than a year after weak employment report**

You can read more about it [here](https://news.google.com/rss/articles/CBMif0FVX3lxTE4tUU5tR0JxTE4tV1ljY1pJckxVMHRXMEpkTHEwR1FIeHNOenVrdjBHajZ2V2NkM0RvX3FUWENHdXNxU2FZNWJ1b1FVb1hic0xvTzdDR3RIZEdhMFBISnBleGJBaTRWMTltM0VtWkxtYnJIY2RBYmhlbDBCTFg0YlnSAYQBQVVfeXFMT1dVSkNFQm5adU1aaVJmVDBPUU50YU5aRE1QZmJJVlkzTUx4WEdGbjZHRGtHMHJiS3JDYkJJSmh2WTFkUUtSajFEX0JrMmEzZkNvN1hGUWtodk5iT2k3RmE0MWQtUllwdEtDUmZTS0tITG5MUzh5T2d5RmFXLU0tMG8zV3dO?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
