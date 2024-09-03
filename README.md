# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Hewlett Packard to pursue suit against tech mogul Mike Lynch, who died when his yacht sank**

You can read more about it [here](https://news.google.com/rss/articles/CBMiekFVX3lxTE5TcUpZN2c2MzhKeXR6MGpwQm9leF9wYUhMVXdidnNaX3lpdXczRmNld1phSlNadWlFQWJpb2t3MnlaenV5VWpkM1Job1pvYm5hYWt4ZTcxemN2azR2dmdYcTFQbHVnbVRpUEYwbWJYX2dkUm1mb2oyMjN30gF_QVVfeXFMUHBMTENlVjAxaVhMNXV5SkJ3aTJLZDZKaHFrQ0I3c2YxN2l0LWRzYmdiZ0F4dHlCOFg5VzJ5QzB6Y1cydUtXWlFfdE9acllHdy1BM3hBU2dMc2pEVXlRQ0lWVmprS2FFZFV4ZE1WM1BJdjMwR1lpV0RaZFJxbklmQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
