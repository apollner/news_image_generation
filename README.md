# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tropical Storm Debby swirls over Atlantic, still dumping rain on the Carolinas before moving north**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxOcmpqUGJHYVhpOFEtZy01N0M2X0l3QUg0YnpOWUs2M2lSSkMxQ0F5NDlBeGFQdGFxS3FMejZNUnRodTBQcDQtNFUwQjdyNEdlU3FCRWE5T0d1RFNJS1dXMUNYbEdpU2J4NFZJVERweWJPVFVLYkN0U0FPM1J3X0VhclJvcWExaDhyMjR5UFhpQTBOZkFmNWRyT3ZwazdOOVMyTDdkWERPSzlyVllC?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
