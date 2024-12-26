import render
import noise
import random

def main():
    noisy_images = []
    for i in range(20):
        noisy_images.append(noise.add_random_noise(render.to_matrix("sample.webp"), 30))

    sample = random.choices(noisy_images, k = 3)
    for i in sample:
        render.render_image(i)

    truth = noise.reduce_gaussian_noise(noisy_images)

    render.render_image(truth)

if __name__ == "__main__":
    main()