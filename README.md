# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Nvidia has become world's 'most important stock,' adding pressure to upcoming earnings report**

You can read more about it [here](https://news.google.com/rss/articles/CBMipgFBVV95cUxObkxYeWVGQnA5TktRazRfVDQxdFpVTXRTeWFVX0xwUzE1aFdlUDJiY0cydnUwN2pIM0p3Ri1uaEYtMHFkdHdHR1kwTHZneVlhRkJER2NjQkRWN1BzRXpzSjVmai1Cb1k3Q0hYenowS1hzSzFuTEswdFRXZ3hwU1ZSbFRDb0VGd2pJUEIwdDlOalQ3TnlJNllvNUI3YXN6cnVMWDQtQzBB0gGrAUFVX3lxTE9pUFJhM1I5QUtIOTJYYWxfWjY3bkkteUxwTGE2Zkd1dVUyOWRtMjhYal9EYTJFeDAtckNwZWhSbklCWk54bEJybnBuZUNpQUlOZXlDMnNRMi1JNGJaTm5fTFFDa00xZEVJdDV4TjZFVFNHMmtIR1BLdWJVRXh0Y21KX3ZBWU1TUXJ3Sk9ZYXd4NnRLMFFIRUNITVhRamtLZU42RFlLOTM3Wi1fbw?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
