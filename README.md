# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Mega Millions results for 07/21/23; $1 million winner sold in Michigan

[Read more](https://www.mlive.com/lottery/2023/07/mega-millions-results-for-072123-1-million-winner-sold-in-michigan.html)