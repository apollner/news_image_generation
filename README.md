# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**President Biden campaigns with Vice President Harris in Pittsburgh on Labor Day**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxNWmF1WVRWQTJPV2xnbjh0MVNqX1o5SzliekVGV21RM2F3bzlmM0E2UmdITkdYSlRGeEJPcHV3Z3VlVlVycHBxMW1ObXFvRXBBN2M2RHFXeFZZNHBfN0NuNU9BV1l5ckp1dU83NmNVSFhDYU5KZDVuVFJIRjZOdjg3X29JUG4tTWFCeko5amR30gGTAUFVX3lxTE5EbnBlTU9aUXdmcC1rRXB6N0tRbjUydnBaLVNPLUdORmYycHFnNkJPWWFBajRBRFJUOWNIVVNKbk1XRHhwRjNNb2RXd0ZiOW92TVM5ZnI5clI1aTJnbnNhQmwxLWJSVl9EdzctaDN5NVlzNTZ6dHR4cnd3SE1PMk92M2Z3RTNRaWFXSGdfbXdSOFFXWQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
