# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Charlamagne tha God on Trump’s racial attacks of Harris: ‘I don’t give a damn’**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxQTFYtY0d4RGxGcGVDV1k5WGRHRjVqM19VNTlFaTBGa2FTYzBzYUFhbXhuVzdPY3dqenVoTm1OemYxTG41U3plR25ZZVdQRUxxeFR5SWNKNVJFZ01FN1JjeXctWWxYZ193QXQxWHQxR0NvVFpaN056eVVRTVczNmxraDV3N1RQd9IBiwFBVV95cUxOQkl5RTM0Y0FRUU9zVGxfTjFjelNuSHFaTzFvQWlSTFl3RWdmajJfczdsSDMxS2FzaXQ5LXBabUZtTlU1ZFNYLUZ0a3IyX3c1dEI5VnRaSUlwdjV6UUxsZml4aTNUZ2NkbmxIQzdWMEF5QW9fS3NQRk1CejlaOEFCeHljNzdXRXM3amNr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
