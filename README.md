# News Image Generation
This repository contains a script that generates an image based on a news headline. The image is then saved and displayed in this README.
The news headline is fetched from the NewsAPI and the image is generated using the DiffusionPipeline from the `diffusers` Python package. The image generation process is performed on a GPU.
The script runs every few minutes, fetching a new headline and generating a new image each time.

---

![Generated Image](image.png)

Prompt: Australian man and his dog rescued by Mexican tuna boat after drifting 3 months in the Pacific Ocean

[Read more](https://wpde.com/news/nation-world/sydney-australian-man-and-his-dog-rescued-by-mexican-tuna-boat-after-drifting-3-months-in-the-pacific-ocean-manzanillo-timothy-shaddock-catamaran-aloha-toa)