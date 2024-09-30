# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Dana Carvey’s Joe Biden, Andy Samberg’s Doug Emhoff, Jim Gaffigan’s Tim Walz Join Maya Rudolph’s Kamala Harris To Kick Off ‘SNL’ 50th Season Premiere Cold Open**

You can read more about it [here](http://deadline.com/2024/09/snl-cold-open-andy-sambergs-jim-gaffigan-dana-carvey-maya-rudolph-1236102778/).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
