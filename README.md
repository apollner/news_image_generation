# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Wolverine Co-Creator Roy Thomas on His ‘Deadpool & Wolverine’ Credit: “My Name Should Have Come First”**

You can read more about it [here](https://news.google.com/rss/articles/CBMiugFBVV95cUxPR1ZVOTRwNTA5cWRvZmtQWWdxMHRRY1M1MWtrZEJVSzZxUHJGeDY4Uk1HdHZYcDlyeEd3MDRHRkh5YXhqTVBVbE5tdExSazk3d0ZQWW5LR3AtWmd1TzhNSExNalFITWhWVFBIQko3S2xqbGJuZzQyd2JOWlYzeWxXY2dWTFhmanZRT0JnM1lRc0VZQXM3cnRxb3FPcUtPRGFzbTVqbFk4ZFc2bnZ3LUFodXR4ZWRmZFBDYWfSAb8BQVVfeXFMUFhNX1ExWEFaNE14RE5NVWZuZWhrSlJUc3J0ZWFaNkdKZlQ5TnpiSVhnOEF0TGdQb0xDS3VFdnVmdkNhVTZ6MjJrSWlUWi0wNy1qZWl4MjR0U01PTHExMUgxTTZGclpPQXFXZ0llSGJORHdXY1lDQjZrcURMOFhhYjByOEUwYW55ZHdYc3J5VE1CcDRJSkoyOHVZclZXQWdVSlltd0RoUnFvd0JqeFhEandkLXZ5dkZxd0VSYmdYb2s?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
