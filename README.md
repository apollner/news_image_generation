# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: ‘It comes up on you fast:’ Scorching heat is crushing American businesses

[Read more](https://www.cnn.com/2023/07/23/economy/extreme-heat-economic-impact/index.html)