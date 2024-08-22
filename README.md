# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A bridge too far? Blinken’s desperate bid for a hostage-ceasefire deal**

You can read more about it [here](https://news.google.com/rss/articles/CBMioAFBVV95cUxOWV9rRTdFWGZYQjlBektzSDRBaERlaUdyZTdnckZZZEhncEhuaGlSVXBmcWpGbVh2dTYzYldBYlNpRzdvbW41d1NWTFljNS1WSnRFYmNXSFlyRWFDSzUyWkxRQ2JuUVNvSl9JYVdGLWZaQkRsSG5lbFZuQ0RReWhwOG9ORjdkd2w2V3JiZU5wbHJDUl9PalhZU093V1dGMGVH0gGmAUFVX3lxTE1kdlpuLUJRTFl2ZzlaSHQ2bG1GSnQ1WlhqTjVwOXFKZmJ5RHhrWDY4OVNjLWdXejRycUZUZFBzaFNhT0N3WUtoWTRMaXJ4NmNLSko3SHJoNjdwdHBrb0hxaWNCc3NhdllteXF3dndnQTlsalktamY5V3Bod1pxemY1d2Z6YnM0ajEzVGR0MTBaRXlCb1p6bWloYnVSUXBNdDZpbnViMVE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
