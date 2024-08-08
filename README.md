# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Tim Walz: Chinese internet discovers that Harris's VP pick taught in China**

You can read more about it [here](https://news.google.com/rss/articles/CBMiWkFVX3lxTE9aWnhtS1Jld1dYVHUteUpxc2VDVExEQ0dteWkweHZzNjZBY2ZHbUc1WlJXYzFNblY4aG8wazFPNUc1TUttYUxfX3Y4N2lfa1lRaG5oMlY2UEoxZ9IBX0FVX3lxTE9hNDA3VFdRc3BnZ1hyTnRRRXNxblB4dWx6blpQTEF3Y2E4ZDFLRTkyaG9ka2xKcGE2ZnFVZDE5MmxocjVzUE43dk1BWElua0FuaFBmektfakNoVzhJSVZ3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
