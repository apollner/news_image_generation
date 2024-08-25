# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**F1 Dutch GP: Norris takes dominant pole from Verstappen**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxOcGg0UjlNOFFTY2t4OXFlUHNzbHZKWE9HSU10ejEyQllRcmFiUTlVMVM5dVQyVWczbkJRYVgwUG80MnZtMkk3cDhHajdIS1A3SmxDc0tIcnktYWUtQ2NieEU2aWNZd0RZWTdmSUo5U3FCT1p1enpzVUJFejF5cS16cmhDQWdoakhNb2dWS1JScEEzOWhSU29JMFpOdzVFcGFR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
