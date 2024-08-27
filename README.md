# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Russia launches 'nightmare' deadly drone and missile strikes across Ukraine, Kyiv says**

You can read more about it [here](https://news.google.com/rss/articles/CBMiuwFBVV95cUxQQ3gtZXlYYVZ1UklaYWQ1b2Q2MUpHdXB4VFI0LXdoMnhPaFliOXhFdktmQ3ZxNGZHMGZlYTJBS21DN2NWbE9wQUhaR1NiVmNERWl5X0ctRHJqU3UzRXRkWklvcGl6LVZteTcwSDZtYjJQM3JRNlFXWTVDZndHeTNlQUh1Z2hfZThzaEF5TC1FUkl4NnlOaTBmbVpQRnZmU28yZUFoMnZ2VE1GNmpUTmR3Rmx2RnlKNk12SzhR0gHAAUFVX3lxTFBRQUtuZWd6ZGlEbUpYZndPS3JsaVlGN0JMTVdoT25GaVJGWG5VTHJNaTJOdmplSTJjZk1pTFZhN2NxVHdMMzA0MGk2bVFRSC1PdVBfaXZKWElSOFF5Ml9wQkRqUGRwUzZsSHdqTk54ejhqRG1vcGl5c3pWQ0RaaUJRcDJmUUtfa2xVMUpZc1RUY0Q3cEFVSmZMUmRqcHJpbXc2RVZYS21VdXAybFgxNkRFLU1GSTRxUVNlZm1uT1NCLQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
