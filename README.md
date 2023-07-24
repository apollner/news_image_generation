# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Massive crowds rally in Israel as vote on judicial overhaul looms

[Read more](https://www.aljazeera.com/news/2023/7/23/huge-crowds-march-in-israel-as-vote-on-judicial-overhaul-nears)