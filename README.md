# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**SpaceX will take Starship catch one step further very soon, Elon Musk confirms**

You can read more about it [here](https://news.google.com/rss/articles/CBMipwFBVV95cUxQV0VyT21rU21xckp5LUxQUExGTWNfbE5KelpjZWNTbFRWeV9zRGJQVnBhanVEdTVPbWNOXzNwQ2k5X293dXJQZkVfa0sydEZXWDlkdnBhd0RjNXFmZFRYakpCRGg4emJUM25rakhteFlyU1FlbHRnT3dvMzIxeDBMSjZiTFkzSEVUSUk1S0VSUmF1eDQtVXZ4empTeVg3dk9TdlhuTEFYTdIBrAFBVV95cUxNNjYwU0tuVnVncGo3TE52WGh6dTJHMUlCLXRSdDVLVFdnR3gxVVlhY0hLX2pmbHRqXy03YnU4ODhnemlpTWU3VmhQX0R2ODM4R1p6ZE0zdU9LN0l5QmJ0YVBJN3ZCbEVIN1lIbDhTLVhZSjA1eTF5RDcxMkx3QlBHamJYcDdBU0JST0ZCVTl0dDFDUjQ5Qjc0bzBJZTlWalpvRmhEN2pWbDVZZ2Zn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
