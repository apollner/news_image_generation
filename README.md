# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**FDA rejects MDMA as psychedelic-based treatment for mental health, PTSD**

You can read more about it [here](https://news.google.com/rss/articles/CBMimgFBVV95cUxOVHUtSUk3Vk1CcE1FX0hKd04tZ2lBRjYzRjg0V1FlRTVwV2ZyTnFQSExtbzhMWmktdEpFWmJqMTVwOGxBMzVhTm9fTE91NkNnam5UajhtOTA5bURIR0xRT3ZUVmZSeWtzaVVKTWtqaXh4VVdmQ1BqclpDSjhGM3JwbEoyNHhOcFRYQUtyNTMtMGpoaXBkaDZBMkFR0gGfAUFVX3lxTE9SemF5Y0gzSFpjTFF5UGZ1N3c0Z3E2S2dQbHViQ3F2QjZvX3lfQzl1SVRiTXZVYnplWk9QQ24tX2wwblZ5RFV6RzhCdEZxYTExQmlrOFl4aWdBc3FCekZyY1AzVW9HNjBkTllNRkFETXY1c0RybGF0cDVvc3lMdmpfdUpPT09jOVlCeHJJOTUyVEphaDRVRnNHcXpWdExZWQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
