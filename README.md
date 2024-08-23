# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**July home sales break a four-month losing streak as supply rises nearly 20% over last year**

You can read more about it [here](https://news.google.com/rss/articles/CBMiswFBVV95cUxOSXIwZkk2TUN4VXljQzk2WGNCZWlnQ05CZUExck9Fa1pLQ3VJNEstMml5bHNNemJNMEw4OHZrdEFnZk1YS3hvclBlZzVNVHJDZUxydHF6QjJVUXc5RUhVWG9xNEtzaEZUZ3JURWRxRFpKbXp0dEprWm1sTU04NXdPQWkyaXFuZEpJYjh0ZmwyVk5lSERNbGFIbnFYamZTdU54THpQNXRfM1h0dWVuZUUyZnpGTdIBuAFBVV95cUxNX0NheHFMVWNzbzBsVV9yMWxGTnhOcURSLU5ZUlZLVzl5aHlqOW9pZzhDa0dhNExXbkJxYXY5clF5U2REWlRBcGVSck1TVldHa1dXNm54RGhkRHYtU0haaHpqdThlVDlhWS1YeWF0aV92VEZyUFZTMnVMYXo1RnlLeEt0R1lMMVBHWGhkLXBYYmkyZ05MVXRsTnhIMEttWTdKblhEZGx4VWJXLXVuOFUxLXR2bU96MHJC?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
