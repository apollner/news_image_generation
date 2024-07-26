# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Powerful Typhoon Gaemi hits Taiwan, expected to drench an already soaked China**

You can read more about it [here](https://news.google.com/rss/articles/CBMiigFBVV95cUxNSG0wcHh3LVgtazc0eHpab21VdlBUMFo2N3pTeGxfbU1CNDdvel90S2dnNXItbHp2bDkwWkVZMUhfVzU5ODNFekNLVEN4enN3R2c4Z3dEVWxVc00xMXRKZHVHaXVaNHN6emxoZjloQzg3N3YxMnF3V2NUVVQtUS1JckMtQ2JuREtJbWfSAYABQVVfeXFMTm5fZm44UF9pOEdhb1RVTzNyLXJtRW1nUmJrOGhPd2ZVZ0c0VDE1X3k1bmlQRDYxU0I3SVJXOWlfRGd1V0YxbkdLYl9oUU80ak5JMFd2anlmeV85NzdZamtYck5GNGJ2TmRmQ1ROd1YyaVdhbEVuMTF1ZE5zMGtoWnE?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
