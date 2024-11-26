# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Earth's rotation has tilted 31.5 inches, and humans are 100% to blame**

You can read more about it [here](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNS0Vrdm9xRktpakJycjlhNXZQa2tnXzlFUEpueUNqQl9NTmc3VmNfRV9Pc2t0UHhlVjdNbk92OFFLUG9GTUlSTlhQQ2hER1Q4a0NyOXRlT1ljZ2FpNVgyRGFCM0M4VHZjVG1GLVE2ODNCZ1VvVGM4RXhocEhzYmttSG1pZ1dIM1Nv?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
