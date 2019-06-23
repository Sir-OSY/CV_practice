from argparse import ArgumentParser
import os.path as osp
import glob
from matcher import match_images


if __name__ == "__main__":
    parser = ArgumentParser("Tool for combining images to panorama")
    parser.add_argument("input", help="Directory with input images")
    parser.add_argument("output", help="Output image name")
    parser.add_argument("-e", "--extension", help="Input images' extension (default: jpg)", default="jpg")
    args = parser.parse_args()

    image_list = glob.glob(osp.join(args.input, "*.{}".format(args.extension)))
    match_images(image_list, args.output)
