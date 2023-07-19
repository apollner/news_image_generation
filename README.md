# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Powerball numbers 7/17/23: Lottery results for $900M jackpot

[Read more](https://www.indystar.com/story/news/2023/07/17/powerball-numbers-july-17-2023-lottery-drawing-results-power-ball-lotto-jackpot-7-17-23/70421321007/)