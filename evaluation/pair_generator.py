import os


def get_image_paths(folder):

    images = []

    for file in sorted(os.listdir(folder)):
        if file.endswith(".tif"):
            images.append(os.path.join(folder, file))

    return images


def generate_genuine_pairs(images):

    pairs = []

    groups = {}

    for img in images:

        filename = os.path.basename(img)

        finger = filename.split("_")[0]

        groups.setdefault(finger, []).append(img)

    for finger in groups:

        finger_images = groups[finger]

        for i in range(len(finger_images)):
            for j in range(i + 1, len(finger_images)):
                pairs.append((finger_images[i], finger_images[j]))

    return pairs


def generate_imposter_pairs(images):

    pairs = []

    first_image = {}

    for img in images:

        filename = os.path.basename(img)

        finger = filename.split("_")[0]

        if finger not in first_image:
            first_image[finger] = img

    fingers = list(first_image.keys())

    for i in range(len(fingers)):
        for j in range(i + 1, len(fingers)):
            pairs.append(
                (
                    first_image[fingers[i]],
                    first_image[fingers[j]]
                )
            )

    return pairs