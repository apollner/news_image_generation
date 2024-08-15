# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tropical Storm Ernesto expected to become hurricane anytime now north of Puerto Rico**

You can read more about it [here](https://news.google.com/rss/articles/CBMihgFBVV95cUxPcHdHVm0wSHVXbkw2Z3dUc2dWSHVmT2xtMV9xQnZ6WTRzdW05ZUwtT09NTXBxWi11QTdlYnZFRk1aMEI5NHgxNUExdEdFblN0VEt5ekZSN1h0Z19Ed2pqVjBUb0ZnbDRCb1dqa21Zb3M5cURGMEZpRXFxVVprUkU3U3pDWV9yUdIBiwFBVV95cUxOLUFjSUpOM05jMXk1OXoxY3oxeTdoSkhvb3ZYVC02eUIzU1Y2Ym5aNlJTcHBZbi1icm1tTEpCempkOU1Fa0ViWFlBVlE2RFhQejhjOTN6UEJjeVl3VG91VnBVNHhDX3hSTElRMkpZVXNjLWp5VzcxSjUwdmRuSDF6TG9tekdOVFVxRVpr?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
