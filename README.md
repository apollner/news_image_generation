# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Brian Harman stays steady to maintain five-shot lead at The Open - PGA TOUR

[Read more](https://www.pgatour.com/article/news/latest/2023/07/22/brian-harman-takes-five-shot-lead-at-open-championship-british-cameron-young-jon-rahm)