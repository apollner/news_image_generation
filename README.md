# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nelly Makes Surprise Appearance at Machine Gun Kelly Concert After Arrest**

You can read more about it [here](https://news.google.com/rss/articles/CBMikgFBVV95cUxPcFFYclFVd08wM21uSDRzSkEzQzBxQjdyVE1YZ25hLWRKY3dBb2w2Yl9uWDllZE5NZDNzSjdyUTVyLXBodVVwakVqMktxaDZ1RGZTQVMza2M4QlhHbDloWmU3MFl3eUtHX2FoSDB0VGp0Z1ZWTG0zdGwxWk1aSWhqTVZFeFFmNDl5OWNhdE9GVjk4Z9IBkgFBVV95cUxPR1dlVE5raWw1bzNNNmpJUFJXRVczVmNxanFId25jRFdVTzkzYzAzcXpraWdINXRXemxLZHJCdmhFUzZSZ2NVNjNPSm9vdnZlVWVOcDRCNHlFWkwwazJuX3dlY0c4dmFqY3ozV1NQcUlxb282VnpSOGlHcTVURmJ3MlE0WU5CQ2dkd2kzM050TF82Zw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
