# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Exclusive: Bangladesh army refused to suppress protest, sealing Hasina's fate**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxNWlF6Y2R0SzFIVTVzMGJ0dDVUaklKam5BNG9hYzlRaFFrTHBNeE9fNmgwa1FnRk9JdG9aYWpPR1VmdU05T3FMd2V0aTZLbWRFQTZBZ3VCZlhCM3hpRTBkdVBYd0h2Z1RZV0lLOGpJemhTc2JJeVYwMU9JX2VCRG1HQm9vdmVqclBxZ2RjQ3E5Qmo2Y21PdF9tWTVsZm5yMlNXcG94TUNuVDY2clhab0E3UzVHM2VBdXc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
