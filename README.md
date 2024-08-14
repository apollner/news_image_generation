# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**ABC Names Second Black ‘Bachelor’ for Season 29**

You can read more about it [here](https://news.google.com/rss/articles/CBMilgFBVV95cUxOUjZ1XzN1YVZHYVBoS3BRVlV2TGlaTEpfbzRGM0pvQUxMWGNPcnZ5V2g3QnRCN25YMWF2VWhtakZFMnNnaFM5NkdDM1UtWWNNcUZ5WGRSMGJzWTExazE1QzUwXzNkTFdwRWNzclhMc3F0bmlxQ0ZFLVhUYWE2WGZibE1LYjVKZzVlSk5FWVpkeUlNZWFocVHSAZsBQVVfeXFMTVlKUWFhUzdKWVRLX25rdjRKbWJNaUR2dlhvWTdBQ0gtM2szVTRCblZWdjB2RlZad2JIeUp6NGFUNzFNODQ0NUc0RW5jSVAwTkFBcmZCT1JxaFUzQ2Rfamx6Uk9SdUNNbmtaTDhMZ0Z3NmxzNUNHeVhqUEVCRERVOE0tV3MtTWRvUUk3Q2R4Z3I3NFgyVHI0S3U1WkU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
