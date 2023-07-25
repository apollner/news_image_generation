# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: The Open Championship payouts and points: Brian Harman wins first major championship - PGA TOUR

[Read more](https://www.pgatour.com/article/news/betting-dfs/2023/07/23/the-open-championship-payouts-and-points-brian-harman-royal-liverpool)