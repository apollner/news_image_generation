# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**1 deputy shot dead, 2 suffering gunshot wounds in ambush**

You can read more about it [here](https://news.google.com/rss/articles/CBMilAFBVV95cUxOMnppZ0liRkVzSjByNWpoUTY1RFJsRThlWmpOT3FuXy1GMlozSjNodkFHbmdJenc0ck8yTVFfWFhxYjZXNXhGblRGcEtWYXN3czNGZDM0Zk1mLXZBX1Q0aWJJMkY0QXlwd2FHaWNJbk0zeTBORW5nSkIxSXFobXY5aFNkd3Z4VDBNTUlKRmRQWU5aWUhj0gGaAUFVX3lxTFBScjU0T2JMelIzQ0pqa3pjVngyazhJZ0djVXd5NUs4VGhrVm1PNWxSWXpNdUtOZ2UyWE13R0xqT1hfYU5OUktjZkNpM3JGRlh3VE1jUEtiMWZ0bEdBVXRBTjVINXNhOWVEMm5SaVpNMTdrb2tEWHlPTGI1VGR4clZXUkFPS0dlVDN0b2tIZ01hUEZ0VTdtV2U0aXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
