# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Cadillac reveals new 'Opulent Velocity' performance EV concept**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxNVmlNR2MybUZVS2loWVo2cGxIQko5akx4OTQ1SlNEQnNDRmpHVUlQN2FuXy1NME1zeXlqazhOLVJhdUVpQk92a2tWZjRvTExyanhwZ1lWU29FUzhVdl9iNXVsLWlEOFVDaC12Ylk3WWM0bGVzSE5Hamp0SVQ3TG9LZWtRS3NzYW51b0ZSVllOakVScVlQeFVfUWd3R3ppbEhK0gGmAUFVX3lxTFBLNEVIWHBGbnVZZzE2aEVxMWdrWnBUTzJneVRpWlFiNEtTLUFwY3RPV2xCaWNkcW8zMksxeWxRdEgyVzBDcjdDUmZfUjlNdU9waTBVVmRNQ1BYOFNzVzJQR2UtOGdBdERmWTdZYUN1aGRzbVJQd1VhS2w0dFZFbzdvS3F6Y29za29NeHl2SnIzNTdmQVpjcXNLb2c1Zy1IanZyLTlqLXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
