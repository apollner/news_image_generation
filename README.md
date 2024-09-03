# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**2024 NFL predictions: Final record for all 32 teams, Super Bowl LIX pick, playoff matchups and MVP winner**

You can read more about it [here](https://news.google.com/rss/articles/CBMi1AFBVV95cUxPYnpyd3p2c1VpQ2RMYWNXNjhCSE5NQzJJVzladW1iTlNKSzJ1WFZOVVJJbGd3WEVxWTgxNU9xUVlYdGl0aWpjN09ZQ2FCUlFzT1gtcHVRVWJXcE1HbGxfS0pCZ2M3djkwREstenlRQnpMenRydlF0UlJJVWg4bWlqYkc4c3Z1RzVNek1kU2U3RjlUMnpHNDlJZ01sMDJCeENabU5KeVVsbzlPcXdXYXVZcldrX1h3eC1mY3hkRjVlel9rLV9ISmpYNzY5Ry1lX3JoSEdJQ9IB2gFBVV95cUxOTXZ2ak55Q3NQbnZBQ25hOEpCUTJUTDlsZHJOU0daNnRzVmRDdGROMWUyQ3VsM1FFVUxhcnRPbzU5NVUtR0hwZ2pxWW5nbjgxNEp3dm1ObW1xcHFyenpQX0xYQnZDNFFTUjRYOEx1TEczQVRnQUJNUHZTNGxLMXQ5YlhSNkY4cWFpVU15cEdDNzh0M19scUlTY29vd1F0ZERtMUVvZW5RbG9mRXZhNUFPTWRMWjZLN0J3aFBLZkJSLXc1Wi10MVRDZk1kZWRfdmtyWnY1dlZ0amk2UQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
