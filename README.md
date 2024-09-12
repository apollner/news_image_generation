# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Trump, JD Vance repeat baseless claim Haitian immigrants are eating pets as Ohio officials say there is no evidence**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQeURhQWRVdm1BNDU3TTU1Z1VqTndXb0NmR25vQ1YtUTVSNmh1M2RmZ2g4OHB4Vi1rdlhMenllRXBKa3lIdTJxMmZscmhmMk4xcmdLLWotdEtQMmx3eFdZcDlKNXlHbmNNcU1GaWREaGFEbmlSMDZxUk0wZ3BmLThLcUk4X29MYnlPUmlZ0gGQAUFVX3lxTE5oQWJSOWJwSUwyN0k5QTFPajR5MEtHQ3hrS05uUFM2Ty1rWklMdGdGQWJjNU81cDRRRzFqTEdvemlKd0xHMjJhSV94U213OUtScUhOT1BmcGc5TWpDTEp5THhHZDFrd1JtNDdpMXlpU1R3SDdVak43RGNueDllRjZ5N1ZVNVhkQTJIcW1fczI3Qw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
