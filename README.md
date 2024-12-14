# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nancy Pelosi hospitalized after she 'sustained an injury' from fall on official trip to Luxembourg**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxOZnVacFhsQ0xheTFHQ3d3ak9mcmhEZjVUZl9FLXBKeS1fUmEwcm42a014b19Oa043bVh4aU8zMEhHUnNXSEloWmRmb2FuQldLclR6Y01jbU1DS2RoTmFITllfb1FRT2tnOFpBbmxOd0ZSNG5JZGlrdDU0YTJkcEsySFR4U2tqYXFBRzl5SEMzZHhWMGZIdzR4YVRDb19Fa29s?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
