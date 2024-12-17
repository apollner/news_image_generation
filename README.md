# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Softbank CEO and Trump announce $100 billion investment in U.S. by firm**

You can read more about it [here](https://news.google.com/rss/articles/CBMitAFBVV95cUxQdklwb1hDM2NWTjVzVlhITmNoMzBmWWgtbkhjTGNDeWh6SFRRVWV1NGFqQ25NamRGeTdxOG1xVnAxV2JVMExJUm85ekd2MkRaYzF5UGNKalNBSnJyLVBrVUUwTHFtc2xxNk9nbEQ2RUVDT3VNWUFoZTRXZlF3MnAzdmdaWTFkQ3hQUnBjNUpWcVI5RWlRd0kybHFoZklWQVFUM2ZXR0J5MHZiTlJzV2hZSmJEYXjSAboBQVVfeXFMTWxoQTAtT2ZFY0ZJZ2VMWjlxYlVsYmFYRklZNHkxRkZLRzJydXEyZ0FkR2czeFE5MWd6bTFSUEVFMzhWejBBWHd1a0o1bmV5dTEyQ1VucTRwSzJOcWZuQzBIVTgxMlhNcm5QeU0xT3k4WF8yUEprOFY5dHEwN05JY2Z0cTJ4MXVseHBMYy1fNHg2SWhXb0VudVl4bUlRZE5OZ3E1ZmF2MHRxSnA0dy1wd05kcTVBS01JZ2JR?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
