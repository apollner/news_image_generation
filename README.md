# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Britney Spears Biopic Film Set at Universal With ‘Wicked’ Director Jon M. Chu**

You can read more about it [here](https://news.google.com/rss/articles/CBMijAFBVV95cUxPbTdoS1l0Nk5TOElTVmVITU5panhnV3ZKaUswMEJVdEhOUkc2RzdwSmxFX2VlU3JzTV9MYXJNX05ndUlWMS1xV1RkT3ZnYkk0Wk1YaXRLWktnVHVuNURFbS1scEV0bjFBU01hbWRXQ2VLZFQzcnZ5TDNtX1RDaFRkbnpQbndvaHZKLUtqZdIBkgFBVV95cUxPdzZtYTVqN2xzRndaUVA4WVRualNfTXJNZE5JczVXRTVOejdqekxGRTM2QkYyMmN6RFdEMThjZHlHWDRJcE1heVJlVC1ta1RTb1FvalNESm9hVHpfWEJqaUtNR05kRmNwUFZOTFl3ODBjT0F6Nm94OW9KdlJBWHBOZ3FvYktrX0FFRVRjeHF4MXRBQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
