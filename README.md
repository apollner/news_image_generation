# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Northeastern towns issue voluntary lockdown to prevent spread of mosquito-borne disease**

You can read more about it [here](https://news.google.com/rss/articles/CBMisgFBVV95cUxQSTJpd1p4dENEWnBxSm1wRU52YlBzS3pJVzhaT1Zqb2QwT2t6MERUT29la1hIXzBQSWdCbWcxS2JGVlV5bTRYRzhNNEJkLUxPdWs0WjF4LUxEY1JNUnpDcXp6RmUxS01tTDZwYlNXdmlxOXZKeW85Q0FrMU1EWUg5dU1KZFpsLWtITmZ2VEZMQlJxZ1IyQUcwMlFJU2Y0U2RISlBNS2ZFSEFNc2VDb01JQXNR0gG3AUFVX3lxTE9VdWxIR1Bfa2xiMTRVUnRkNWp3Vi1Kd0ltYWp6cm5KVmFLWTFzOHNjV2RhX1B4VS1rN1ZCdWtFUlpGRml0MnhhRjQtME9uSjJZblE1aHRDNEZmWlJDVW9ObTg4c09uSW0yZWtfQ3NwRjdsbHJMTm54Y0Z4RUctdWxFVVVnYkVheDhPRGhWTFlVazVST0p1RjBEMGtjY1FHWUwzVGJMRnFUWERVS0Fad29iR1dnQ3E1QQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
