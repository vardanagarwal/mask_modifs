def get_labels():

    Dict = {
        "maskrcnn_coco_labels": [
        "background", "person", "bicycle", "car", "motorcycle", "airplane", "bus",
        "train", "truck", "boat", "traffic light", "fire hydrant", "N/A", "stop sign",
        "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
        "elephant", "bear", "zebra", "giraffe", "N/A", "backpack", "umbrella", "N/A", "N/A",
        "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
        "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
        "bottle", "N/A", "wine glass", "cup", "fork", "knife", "spoon", "bowl",
        "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza",
        "donut", "cake", "chair", "couch", "potted plant", "bed", "N/A", "dining table",
        "N/A", "N/A", "toilet", "N/A", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
        "microwave", "oven", "toaster", "sink", "refrigerator", "N/A", "book",
        "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
        ],
        "deeplab_pascal_labels": [
        "background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car",
        "cat", "chair", "cow", "dining table", "dog", "horse", "motorbike", "person",
        "potted plant", "sheep", "sofa", "train", "TV/monitor"
        ],
        "face_labels": [ 
        "background", "skin", "left_eyebrow", "right_eyebrow", "left_eye", "right_eye",
        "eye_glasses", "left_ear", "right_ear", "ear_ring", "nose", "mouth", "upper_lip",
        "lower_lip",  "neck", "necklace", "cloth", "hair", "hat", "face"
        ]
    }
    return Dict
