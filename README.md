# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump promises universal IVF coverage, suggests he'll vote to repeal Florida's 6-week abortion ban**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxNRE5KVEFPcm1MSXYwZFc3OTZNNjU1ZDQ1Z2JUQjRuMHdHZk9lMzR0OXFMejVjVWFyS2VHSDA0UkFBWEI4ZE9NVEU2VFN5MTJYc1l6TWRUSncydFo2MG5ENzl3STdJTEhzN3djOWFScHdOVjRyaDJ1M2VGSm5pZWF6Xy1kenBMTU1NVVlkR2szeWZUQ3Rsc0gteDZzWjFlemVKc0FncmE4RXdIX2lHZFRWdm03WQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
