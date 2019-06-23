import cv2


def match_images(img_list: list, output: str) -> None:
    img = cv2.imread(img_list[0], cv2.IMREAD_COLOR)

    cv2.imwrite(output, img)
