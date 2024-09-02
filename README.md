# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**'Wolfs' Review: Brad Pitt & George Clooney Face Off In Jon Watts' Action Comedy**

You can read more about it [here](https://news.google.com/rss/articles/CBMiwAFBVV95cUxOejlTQ0EycUcyM0JpM1Nfd004Z3JsczNWbDJrTUYyb0dkY2pQTXNJbUF4SW9NaWhmeUNWTkpEN3YyazhaQVlEWVp2N0pRa1RWLXIwNzcxVFlUcFJpTlU5VEF3ZVZ3YlE3OWg5UHB2TVQ1d0ZWOEJzWFNNNzR5SzY1Q1BUV3QyRW1HOG1CYlRvSmZTN25JSXpRRWdyTndjWTZjY0NVSXVfdmI3UHcyMks0eHdrQW14Q043T3JuYm9HbTQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
