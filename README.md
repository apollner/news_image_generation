# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Avowed Delayed to February 2025 to 'Give Players' Backlogs Some Breathing Room'**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOTUs4dXNvTHF4OVFPeTVNamwxdVNldTdCQ043N21qNWllTW5VWFdfSURoOFp1ZHg1cG00VU5tb1RvaW5vbWlqdE9MeHBSTWlKWlpWZ29sZzY1X212WkhqQ0FSMTFFeTdoV3V5MnppcHI2WHk3U05XMHJZNW5zS1dKa2hRdTdsbXJTbVdDR2UtVFBFZENDUGpRc09sMVhYdVl1NzVMb3VFY1U?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
