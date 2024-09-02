# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**"Deportations are 24/7": Migrants are quickly returned to Mexico under Biden's asylum crackdown**

You can read more about it [here](https://news.google.com/rss/articles/CBMic0FVX3lxTE4tNlBuSm1oZW9PLU1OYm45RUU0cjk3dnJtZFNXRmRfNE85OE5JR1hZcVhOdVhyZzlHbjNybUYzclVIVm1ZbmhxeFZGTWl4QnI3RXd4dmhQQk5VZVZWaVpfekJ4U1lhaFhNcTZtZWZWaVdSNG_SAXhBVV95cUxOclVHbEtKOElYWnNEWElGeTIxMEpvWVRzSmJNX3QwVF9fYkJCVGo5UzRhQVRVRk9LdDAydGx0Q3l2UTVuRmZid05TS1Zsc2Eza19ZN01UOF9CTy1McGZiVE1JMUFQcERFLVprbGlVTGJWWGRHY2o0SVU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
