# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**This after-dinner activity went viral for helping you "age wonderfully." Does it work?**

You can read more about it [here](https://news.google.com/rss/articles/CBMifkFVX3lxTE9JVEtOaXdxMFI0NV9fSkptd19fcklodEFISy1EN0ZvcDFzUmY2bWpGaDAxbGFGcjMzYkdsSWlDRGRlcU9fanZMam5zR2xNaTg1NFFfRVc1MThnUFRjWUF4TldLdFNuVTlRbnlKbzBMYk1TamVhcm9qT3BST3BpZ9IBgwFBVV95cUxNaUo0VlpuUi01eHh5S25yQkZSTGw4Mk4xc3ZqZ1NyMDJXUnBMS2hmb1FQR1BkZlJtUGtGNGFrOThNSXJBd1hRRGZHOWh1aExNTkNhM0Z3amlLZ0hnRmdoS3pGRHpZWTlmZkdOellQYWdIdmpCcGRqeEtlRklZakc4djlXMA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
