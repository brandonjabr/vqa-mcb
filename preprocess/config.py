GPU_ID = 0

# True: resizes images to 448x448. False: resizes images to 224x224
USE_LARGE_INPUT_IMAGES = True

# True: flips images horizontally
FLIP_IMAGE = False

# These are in the repo
RESNET_LARGE_PROTOTXT_PATH = "./ResNet-152-448-deploy.prototxt"
RESNET_PROTOTXT_PATH = "./ResNet-152-deploy.prototxt"
RESNET_MEAN_PATH = "./ResNet_mean.binaryproto"

# Download caffemodel from https://github.com/KaimingHe/deep-residual-networks
RESNET_CAFFEMODEL_PATH = "./ResNet-152-model.caffemodel"

COCO_IMAGE_PATH = "/home/brandonjabr/CompleteDatasets/VQA/Images"
OUTPUT_PATH = "/home/brandonjabr/CompleteDatasets/VQA/Features"
OUTPUT_PREFIX = "resnet152/"

# Which layer to extract and the size of the layer
EXTRACT_LAYER = "res5c"
EXTRACT_LAYER_SIZE = (2048, 14, 14)
