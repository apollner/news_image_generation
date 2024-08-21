# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘It Ends With Us’ Star Brandon Sklenar Slams Rumors That Are ‘Vilifying’ Blake Lively, Colleen Hoover and More: ‘It’s Been Disheartening to See the Amount of Negativity’**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxQXzMtVVpHbG45T2dFdFBuc2plQ1Z2eUhITGsxT1U1T1YzYS00b2ZIQ0lfYXJZTzU5VmhtNlZDd0g3MnhvdE5yX2k2WG9hZlJ6cnNyU2ZLRnowV1ZqWlhUcExNNXA5QkU0UWxKaWtBcEZyNkEyRGFzU3JCTFdlSTZndlpXYTg0dUxacjQteXZXTEU5WWk4S0ZLcmxSd1dySG81bW5QTzh6SmRoTDhC0gGyAUFVX3lxTFBxd3NwMWdHLWNVTk1oYndjU3JSaFpKaFowalV6QlExOXY2eVZKTWZ4NTEyR2RoTkxuYk16TV9mZGtXa0NZOTRtNTZ6elhyWG9JRU1jVWhfN2QzSFJueDkyaUNsV2ZkaTZkeURvZEhDSW1EaUEtMWdYNGNDMGJmdWhiSzRoOHRWTFMzaUcwY2J4MGZvZ1hxcGM3dlFLOFktQ3NEcGZrX1BhaGZYOUxKV2xSV2c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
