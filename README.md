# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Harris has never had an Obama 2004 moment. Tonight’s speech is her chance.**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQemptSzFyd2luZ2F3WWpGN2l4VnFMVmhkaElXRnB5VFE3Y1B0Nm5PRTJkcEJrWEVxbU9RdWRCMFY2cjA5a3dVbmZEY0hiZlFYd3pDMUlHQ090U1lwZlR1N2NPVF9XU29lb0JFak9LRXd1OS1mLTZrdzBuQmxhMThEdlJpWmJ0TWRl?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
