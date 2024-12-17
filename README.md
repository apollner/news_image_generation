# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**China Races to Squelch Unrest as Signs of Economic Malaise Spread**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOdkZ4QUtUR0F6Y2o1Y0V0UnlSUkVNdENtVGFrdUVvMWxkckhqRzl6TmNabjhEUm44Unl3WjlKeEJrTU5SVnJnVk9LaDNwWUsyVE4tRGJHWXhCTmprdUN4ZFVqVmlXMnZvNDRudm1zSHVNdXpYcmZDVTl2eEJ5YWZiQzE4Rm92d0FNM2oyT05OSFFkRTR6N0E4TVFzX0pSSUd1MWF5LVJ6d2ltdw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
