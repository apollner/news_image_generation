# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Here's everything to expect from Fed Chair Powell's speech Friday in Jackson Hole**

You can read more about it [here](https://news.google.com/rss/articles/CBMitwFBVV95cUxOZHQ1c0pfS1cwN1ZBUTkyU0lyUF95VmxNZEFlQmVzenhfZmgyaTNnZ2JjeUJVNUU2RmR3UXJRcFEzaHZnZ3FsYU5LYldKSEU5d05XdEEtRFE0TURVV1NCY3hmZUptbk0zOGtMR0tsSXpjQUN4cDRoT2hzNDZ1SzhxWFRmV1BmOFFLcE9FVU5fTS1sZldSRV9OZFhZNEtCdFQ2VkV6RHo4QkZKSnBVdndoU2FLbUhDdzTSAbwBQVVfeXFMTzJqLXBoVU44c2VRc1hCMnBUOEdjUnRzUkFTaHdtNFB6RVdzbWxmVUlYY2lpc3JubjMzX3RteXN1bW5pdENWNFhTSjJVNlFkNzZ6SUJkeWFNYWxnaExWblhfOFp3bjR4T2ZmREhKWV9hQmY2Uk9IWUU2bDhmRTRKMjY5VkduVGR4RVFxNmNaTE5EVkZuaXhUaUI3Vlk4MTlKakZMSXloQ3JDS0JmQUFBUmdFVWtNQ2xkN2RTVkQ?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
