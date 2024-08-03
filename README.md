# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Amazon says distraction of Olympics, Trump assassination attempt contributed to weak forecast**

You can read more about it [here](https://news.google.com/rss/articles/CBMiqAFBVV95cUxOamU2M3hDbGpTWmdZaW1mWDg5LUp0VS1PZjRDODR4LXNVREhqQUZyYkpzdi03UXhkM21rbjFwQ2pXLUdwY1hMdUx6OThOem9ta29ac0h1NU1aQkJKSWJsWVU1RDAyb201QkN5LXJneWZPNXZfdjBlT0E5TzNyMUQ0cjFhb0UwVEZWQWFzWU9XcC1jZDVKaXprLUlOZFRSS0dUUEZpMHFtYWXSAa4BQVVfeXFMTURiSWkzdThoMno5bGlYRTZIcEF1ME1VcTNJTmNnazFhUnlHN3ZabmFJeE50c2JiWENZUndtaWlWOXZrbWkzdk9iU3dxYm5LWjBxR1MxR1QyYV9haFV0b2RYd1FMSmhBalJDNGhrSnJqa2tvWWhvZWI5azZVZEwzbjg3ekpOQlFzQUo0UlROMkk3UHpfcWx0ajBVeHNhZ3Vjb241RzIwVnowbFoxMFl3?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
