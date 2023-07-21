# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Jets trading Denzel Mims to Lions, swapping picks as New York deals former second-round WR, per report

[Read more](https://www.cbssports.com/nfl/news/jets-trading-denzel-mims-to-lions-swapping-picks-as-new-york-deals-former-second-round-wr-per-report/)