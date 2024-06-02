# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Lori Vallow's son, Colby Ryan, speaks at Chad Daybell sentencing**

You can read more about it [here](https://www.ktvb.com/article/news/special-reports/chad-daybell-trial/lori-vallow-colby-ryan-victim-impact-statement-chad-daybell-sentencing-idaho-death-penalty/277-79ddfe3c-3f04-4ceb-8b9d-f1b0e8e4e80d).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
