# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Eugene and Dan Levy Officially Set as Emmys Hosts**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxNdGk2eFVHd1h2cTdoeTRzbFpfSkc1RmlBTW9xWXFEMnRNMFE0cGZ6eEhQZ08wT3JlS29ma3ZwRzBHakxpNUJ6cUR0OUljbG1fNEhaaXl1a3ExU3k5aVpZNVg0TWJ5eDdjN29vTUVQcXBhazhWWXVCcnZSdXczSW5nNjR2U2hzUdIBiwFBVV95cUxPem85ZlM1bm5hUktTNjZ0bmh3NzZsVThELW45R1ZZb2k2MlpFd0djVGpCMUprdExUUXlpZmpoSGdSR1ZrX3l2TVhjUmVFWFdpTjFabHFZMEZZb2U0OThmZ01nNTZzdk5TRmxhejFiRWJhbWFiemxEQUx1bFZwYkNVOTQ1MVMxdUVkVTVR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
