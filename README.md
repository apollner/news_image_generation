# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Leaked Google Pixel 9 Pro Fold promo video shows it opening fully flat - GSMArena.com news**

You can read more about it [here](https://news.google.com/rss/articles/CBMirwFBVV95cUxQWWE4MnQ3d2w4SXpPNWZScmhFaTVwZ1E5WllBR0xBQjdQeWpBTzVnYlFRUkNUbllCeTdGMS1qdF9XUnBmenpVc3pob0xfdXVOSHhkVTk4Y2tvM0tJUERpMmJKa2p2RVpRQy1qYXFob0hmdE1IbVhfcEdBNEdYNENDakFCRnFod0hZOENaRElIM2RMamdrNlhEVGh1SEtPVVNjb3Nlam0zNDRnNU5KNExr0gGrAUFVX3lxTE5HQUlheXktdWNrN01qbVYtWGh4YjFJc3NjZ3FuQ2FGLWEyVEx0NHFpUlR3anNjUmtyQ2VoSk1nOW5lR3JndXI1SEdLLVFLWGJJUjQ1STdpTzFWbUh0azRCUmtkczNudFFhMDZuemVyT2RNUFVFend1cnFnU0F4YU5ja21sX0RGaGNkcUNEVnJfYkRMbkg3WldYNDdqeFp4ZW4tbDNYTS1WaURrNA?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
