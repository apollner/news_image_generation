# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Disaster emergency declared in Pennsylvania after Tropical Storm Debby hits**

You can read more about it [here](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNUTY3OWdLU2pxck94NDRmbnVKbXAwbDdUbFJSSHJ2UDg2TnRHenRfVGFJNVJtbm1KWk95eUJoXzc4eHI4QXJzVEhkbl82bkhMamJWa2dLc1AxV1dXdEVHSXlIQzAtX1FqNWtoQTIyNWdoYU1pdmRzR0FLa3Rnb3JxS1liV0Y0b2QtMnNEbmpBTFRSTFpvZzJwTk1QU1cxb09Sc2h2R3RRSEY5UFNVTkFoTWhiM3V3Qi1DZUhwcTFmNDMwR18wQ2dpbg?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
