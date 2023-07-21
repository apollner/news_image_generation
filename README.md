# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Powerball jackpot grows to $1 billon. See July 19 winning numbers

[Read more](https://www.usatoday.com/story/money/2023/07/19/powerball-winning-numbers-july-19-1b-jackpot/70435372007/)