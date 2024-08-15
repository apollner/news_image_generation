# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Agents find more than 2,300 pounds of meth hidden in celery at Georgia farmers market**

You can read more about it [here](https://news.google.com/rss/articles/CBMiggFBVV95cUxQU0EtWjBBU2gwMkpvajlmOXZjQkZ6MFZ1U3pDNTRSVDVwOEN2emFvT296WWtGR0Mxd3ZicVpjVWRnNGE3SFd6X1B4bmU4V21QcFo4cXYxLWFhc0tGcEZtUEJoUXlmQ2t2V0VBRzFvTk13VG0wVXk2ODdzZl9VSURVeFRB0gGHAUFVX3lxTE1GSTBRbU4tYzJveFVjQVptMzdTYktyM1BtR25sRV9COUt5U0UxcjdxVXI0NV9WRGVlY0l4UGRNUjRKb2V6WE94czY3UTF1QlNDbWxsQXY1N2ZCX2lwcWJGci01dGVqZDM4dDBDTnVsSWZuclRHcjdZX3VkbTAyU2JIT05zUV9WWQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
