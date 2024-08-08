# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**‘Saturday Night Live’ Rising Star Marcello Hernández Is Using His Charisma (and Support From His Mama) to Conquer Comedy: ‘I Love Everybody’**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxNVnpnTGYyY0hvVHFiRk53M09NSFY5UlR5cGlNUVN1WUE4ZVJpNnlQTVJxTGxxZHp5b1c2RTlURjNCT1QxWW1haXhrQlQteDV3Vk5uWTlLTFZlT0VKUmNKZ2NnVk5Pb0VsVlRuaXNZRjdxd1F1NG5vS1FPSjBNNlRQVzdtQUFSME1oUXBldWh3bDdwYkZ6Y3hURUJaUFRzdld4Uk5tT2hhWjFNcXFZOTdZ0gG0AUFVX3lxTE5TblJuSG03OGFBOGpzeENMNjJROXY2Q2kzX18wY21zN2ZKTURQSm41VGNNRUUzV2tjUmE1RzR0eE82cHVfdHZrWHVlZnlocF9kZUZpZENLYTN3c3QwQTM3SVQzQ2YzZTZmVklBUHEyeEJtUVMydkVhSThqWXVTMGdyeVp6RW5YZERGMHNrMkdhUmlpNWZkT1NCMDFYd2pFS1FoZlZVVlVvQU5LYTBkd1AxbU9wZQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
