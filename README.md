# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Abundant Life Christian School shooting in Madison: 2 killed, 6 hurt**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxPdTQxUzlLdWhEb0J3Q3VYb2FTNlRLZ1EyZ08zUlp2UEFaY2h5c2VYR0VQYk9INDdtUU5PTk5LcDc5VTVPTFVhTEkzSW9Gc1VSSWMwTFBvbW4yZEdiMVpHYi00YnpaNWRJTlFWQkliVDlzRVhQSHVmUzRQZDFVdm54eUFlMHBzVEVWT2hudGdiZVZWQi1iMHZMWU5ITFJLM3hSU3M4R2tURdIBrAFBVV95cUxQaEhFdWpfYTBNUzEzcjBvSFN4RFNObTNia2t5WDRaOXFEdFk0aVhXM2ZGOUhRUVBkQWs3aTlGYlZZQlBuV2lYcm1fZ1ZidXI2UnpwWFF6U3JpNF80c21iS1c4cXpaaUI0ekJweVhSNHE4T0I0Wm40bjVCR19Da2kwUmVFb3Rid1E5ckI5WG12UEFJZHVNWTV0ZkprMlJDUGd1d1JGcGtvMFM2QllQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
