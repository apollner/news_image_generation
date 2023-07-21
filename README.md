# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Headline: Colts to wear 'Indiana Nights' alternate uniform for Week 7 game vs. Cleveland Browns

[Read more](https://www.colts.com/news/alternate-jerseys-black-helmets-indiana-nights-blue-heather-browns-game)