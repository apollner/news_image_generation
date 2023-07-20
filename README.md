# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Powerball's jackpot reaches $1 billion—here's the after-tax payout in every U.S. state

[Read more](https://www.cnbc.com/2023/07/19/powerball-jackpot-hits-1-billion-dollars-after-tax-payout-in-every-state.html)