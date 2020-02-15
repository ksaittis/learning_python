from time import sleep
from random import randint
from concurrent import futures
import threading


def get_image(image_id):
    sleep(randint(1, 5) / 10)
    img = f'image-{image_id}.png'
    print(f'Got image with id {image_id}')
    return img


def add_meme_to_image(img):
    sleep(randint(1, 5) / 10)
    print(f'Added meme on {img}')


def main():
    image_ids = [1, 2, 3, 4, 5, 6]
    with futures.ThreadPoolExecutor() as executor:
        jobs = [executor.submit(get_image, image_id) for image_id in image_ids]
        for completed_job in futures.as_completed(jobs):
            img_path = completed_job.result()
            executor.submit(add_meme_to_image, img_path)


if __name__ == '__main__':
    main()
