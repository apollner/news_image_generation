# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Carter Center unable to verify Venezuela election results, blasts officials for lack of transparency**

You can read more about it [here](https://news.google.com/rss/articles/CBMivwFBVV95cUxNbmdadldGdlA3elc3b1lvOHcydUwyV3QxcldVdUI2Y1lZbHRZakw1V1FOdklTU2RDM0VDcmVGZTVFaVdETVQ1S3JFSmhpSFlXamw5MnV3NFBIaXQwdmJxREI3ZjVxZWtqSDZZanpWUTdZaHh4aU1KVkR5d2hoWmxRcFp5SjNEcjR5ajlhcFZDczc4RUV2U3ZmaVRWdklsSXBTbnNQX0ctSzVqU0JDeXNwa0FRTDdCa1ZRcGV2NDRBbw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
