# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Greta Gerwig makes history as Barbie has biggest opening weekend for film directed by a woman

[Read more](https://www.theguardian.com/film/2023/jul/24/barbie-movie-box-office-greta-gerwig-records-highest-grossing-woman)