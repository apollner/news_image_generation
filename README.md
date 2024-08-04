# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tropical Storm Debby forms in the Gulf of Mexico, expected to reach hurricane strength before landfall in Florida**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxOcE8xcHF6LXBPVjdPNFFMOVp4b2U2aE1uZlNvVDFjbVpXbXZaaVk2Sm9ua25ZaEJMUXpuM01KZTRSbktzT2l5bVVoMW04aHdXVXZpejJ4WUxvOUdzMGpsckVfcnVjb0xhc2x0RENEdkNoYUdOa3Vqc0V3RlF5dlJZc3V4YURIWXpqZmZsRldyOTBtT19TbnN1RXBmTFJxOVJPUFhZeWczMmR4cUQ50gGjAUFVX3lxTE02ZUdjSldTZU15LXctdHBqSmdkR0REZ0ZkWmR5ckZMX2FWdzJ2V085NHZQVzBMLTJuQVRTY2RxMXZHQklqR1lRVF82TUJ1ZVh6ZW90eVdhV0ZsMUtuM3U4UEZmQmtybnFCa29nQmZGczQ4c3pDZ0ZTVXN0YURRbF9NX3VVeUx6cjdoNjVUNzFtNEU0aHlXY3V1YlVJYnhnOVRsQ0k?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
