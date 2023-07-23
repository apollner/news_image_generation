# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Thousands march on Jerusalem as former Israeli officials beg Netanyahu to halt legislation overhaul

[Read more](https://apnews.com/article/israel-protests-judiciary-overhaul-jerusalem-parliament-266df426ff3f0cc78de0d0593250ea28)