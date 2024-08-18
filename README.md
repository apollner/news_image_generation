# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Kansas school employee locked teen with Down syndrome in closet, storage cage, lawsuit says**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQN2dSeXhrbVFWa3hiam54b0gwenBiZ2ZsMmJSb3F1WS1ZZUxLRmh1Z2NWNlA4MWVJSVBEQ3p6RlE0aGF0NXMwWWJvQmpzbWRKendKd1FpWnVzTmo4NXVUWFgySVFBUDNzT0xlU01jSkVKVTFnOTFVQ3hDWWd1OUdxZ21XWHhSMU1mZkdDVVNKeGU1MWJjSEhwV3liN1h4YmhFMUtIRGVaSGQ5Z9IBrwFBVV95cUxObFJ5TkVvYVlDX0YtYklwX08zc3RGVlhYaGpiWUlZd3JNLXJqbTR2ZDIzaFh3S0R0RFdlWmlzUzN1dy1qVWNPdW1RMUFLdm5UVXFHN0lzSTRVMUVTbXh6UWd5VlVzVzFYQXYtQVhvZlRJam10Ny1tbW1EQzM4clhXNVRxc1lYaFpzTmVxeVFCUUZjWXQ3V0RoV0I2QzNSTUhlQ1ozOW1KSHFiQ1R6VFgw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
