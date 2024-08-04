# News Image Generation
This repository contains a Python script that automatically generates an image based on a news headline. The script uses the [NewsAPI](https://newsapi.org/) to fetch the latest headlines, and then generates an image using the [DiffusionPipeline](https://github.com/huggingface/diffusers) from the `diffusers` Python package for Text-to-Image task.
The script is scheduled to run every few minutes. Each time it runs, it fetches a new headline and generates a new image, which is then displayed below. The image generation process is performed on a GPU.

## Generated Image
Below is the latest generated image:
![Generated Image](image.png)

## Latest News Headline
The latest news headline used to generate the image is:

**Boeing Starliner crew still in space, with options open for return trip**

You can read more about it [here](https://news.google.com/rss/articles/CBMirAFBVV95cUxNSkdQS1ZDQ3ppNTkxa0JZelhTcnk4TEc0NzhXMjRpT3pEdUVpWXBJd01GUTNuSFNrOWh2ZzJnbkNkUHM3ODNEUjNvdkY3aWtpME5GeHJLR0VQUHY5QVpLUkZ2clVjdDlJU0FXdXFJcDAtVnNXUkhvSTc0cGpoV1BGREJpY3F3NE5TLTdNbkNMcmcxMW51d2o5RnZySS15am1EMFFmTXQyMmd1ZEhl0gGyAUFVX3lxTE5xcXNjN2I0cU1LWG53U0RDdGZJU0hnck1fNG0zOUY0QnJkSE1CNkkxamljdVpzUHhmMU43TXhBNTFfbGlDOWRRNjNzQVFaaWVrdlNiNmtiNndvRjE2SkJHVEQ2R0l5eUs5Wld6Y09vQXZoRnI5Q0puTGhGdzhVN3B2N0ZicnlZRlR5VlRqbHpUWGNqZDUzLXBSc3BySlZDY2xDeTBzWld4cGc3YW1vcFluS3c?oc=5).

## Requirements
- Python 3.8
- Hugging Face account
- NewsAPI key
- `diffusers` Python package
- `invisible_watermark` Python package
- `transformers` Python package
- `accelerate` Python package
- `safetensors` Python package
