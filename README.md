# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: ‘Worrying for a struggling economy’: China’s second-quarter growth fans fears

[Read more](https://www.scmp.com/economy/economic-indicators/article/3227936/china-gdp-economy-grew-63-cent-second-quarter-amid-recovery-fears)