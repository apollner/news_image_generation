# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**A botched golf course plan, school board losses and an Irish feud: Ron DeSantis faces heat at home**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxQX3puWDVQLUdodnJVU3QzSVQ2U0VqN2MzSkdDbWFzQXJXb1FQV1hDYzU5UG1fR243ZWxrQkx2RDhmeVI5SGc4cE1wUEVKLVloUV9oV3BudEQzajh6Q0N2VllrTVc0QzJSVWN6U1ZBMTEtaHVkM0FYai0wQWZSVkJndmt1alJhTjhvaXdYVURn?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
