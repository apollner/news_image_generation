# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Chris Evans, Jennifer Garner, Wesley Snipes, and more surprise Comic-Con fans during Deadpool & Wolverine panel**

You can read more about it [here](https://news.google.com/rss/articles/CBMiogFBVV95cUxQNlo3WHU5XzdvaUg3OVFwSzdBSWdVNmY2c1FoWVNOd0xiSkNqdUROSnFDYVhpQTFYTUZya29DVEZKZWF5R1B4N2lGVFVtVFctdFFfZk9Id0JGZncyODdmX0VBM2w1bzN3QTcycFZBdVlFMkNKWlBYb1QtZmY5SzdXc1VPTHpJcW5LVG9zNU1hYXFzaEpaVDBUSlBIMENjVURSVHc?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
