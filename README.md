# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**UFC 305 notebook: Exec Dave Shaw on Perth's no-brainer top moment, the judge relieved mid-event, more**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxQM3JuMnBxV1NSbE9WbjhTRnpIR2xLdmpaQm90djdSOUxJV2xEWldHZTY0VmE2ZnlzY0xSR0NCb280dk81U0s0ak0wQ3gxaWRwazVTSVI0aWFxUE5Yemo2c0FxUjgtZk0wbnpNTjc0bE5RR0F1WWdKVlZ2OGpDUkdjUXQ5SmRBQ1dVXzUxNFdpTUZJQzRtLXdiTkh0MldfSHJ2NTBYczhjNnhmaDU5ZjNWVXI2OE5FMUU?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
