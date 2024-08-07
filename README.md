# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Rioters carry out violent, racist attacks across several British cities. What happened, and what comes next?**

You can read more about it [here](https://news.google.com/rss/articles/CBMijgFBVV95cUxNRzNOQzdMRUFWbmgtdnQwUFF4b3R5X1N2ajRFajh5SmEzbk1FWm55UmI3UEpzTkxmYnE5TGJ4NkxNcnhhV3pob0xaZ0F6cENxQkc3WHNGdDViS3doRjd3Vkl4NkFHM21FUUJ5dlRZQkVCbGU2bkFuS2dOZ3Mwd1R4SzBQM01KbXlnUEQ2Mmtn0gGEAUFVX3lxTE94QzI4MENISmtRTkJEUzlOWWVFRTEwZVVwbzctM3BYeDBabm1CR3djam4tZHlYYVQ1WU9SeDVnWFJFd25IdTBJWC1lQk1XWjRERVhmQzBfM1Z5RVVhSjIwSXlpNVp1Um1XVDBFR2stODhfZzRSeGtKY0tScjV5STNfUkFxQQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
