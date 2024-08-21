# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Parents of Dimitrios Pagourtzis, accused gunman in deadly 2018 Texas school shooting, found not liable**

You can read more about it [here](https://news.google.com/rss/articles/CBMivgFBVV95cUxQMTFSTURuVV81U01IeXREN20wMk5OVVdDLUVUcldENWEwU2JQQjY0OHZ6dWNQR3ZoY0xvWHRURzVJRFMzVXE1SDZhbXRiY25rNE9YMldjMXFGQWpLSkN3U0dKRk1vdzZCeC1DQ0FTZlNvTTdYQTRxaEItZ3NaM0h4UkNXZjNVQ1llb1ZyQmlCdmpJd2NRNHFoY19ENE1VR1lINGpEQmpOSzU2d3I5TFNuSTdJc292VkNDb0lGTVlB0gHDAUFVX3lxTE5wSkVtTzBTYTMycjZOQjlZd1NJaXRrNlBBQ0pDak5KTWE2ZnZkcXZIaXU0d3RUQWVpR1JfeE8zeS1WRnp5Qk9USTNnYWN5cmVwVXBMY3JCTm9JME5yc3NRUk9xM0RGZUR6R2pIS1hHOUFUM1dGOFBLMEl5UFBZSmRUenZQc2RQSExpOUhUR2U1dUtOdE1KZF9YZENla2FMbEtIU0c1VjlEdHA0RG1GcnU1X29SVi1iWFZ6VlA3R3gtdjRLTQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
