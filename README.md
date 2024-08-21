# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**NFL preseason Week 2 grades for first-round rookies: Malik Nabers has A+ outing; Drake Maye showing promise**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1wFBVV95cUxOT3lnNEY3Nml0aEFld3pmbHZsbmN3QmNCWG1EcmtMY0F6SVhsZjVIOVYzR3lydndVY0h2bHZkcnp3NXRiM1dIcXFLZHVfUW4wMFRMWUV0YU5aaENULUVZazN5RUd5YlRXYjZjS0dPZHNXMUdNVm5pVEkxNU9VVmhIdjBCOUQ1ZnYzenVaa2xZanItdmt1cVROckVzT1MtMzdXQmtoandoSUdfbm0zemJubFpzZ1hSbEtrbl9fa21KejFLdTd5b2wweEJRVmtyWTdCNzF2RkVjc9IB3AFBVV95cUxPSEVEODYzVmlDZ0dpd0lQa0pfSjJDWk9QbWt3UE1Ra1VHNTNZb2RJWFp6UWVOLXVzSnA3em1kaWhDd3ZFV2RXV0FyX0VEeHhrb2t0ZUoybm5jZzF4Z2xrV1dfM2lLNXNISElLNzh6eUFlOEVTeU1fakJtb003cXc1dnpmQUstRTd1WWNVSWNsbE9BcUdhUC15dFE3SzFkaFNDeklELTNVS0p4clFxbWpJNzNLd29MZWZ4SXp6aFktSVV5NXdhc08zb21sa05KNWZlNDlHYmRabkJrTUhT?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
