# Multimodal Compact Bilinear Pooling for VQA

Credits to the original paper which gave the basis for this model, found here: https://arxiv.org/abs/1606.01847

## Using my Pretrained Model

You can download the model I trained and used here:

[Download](https://www.dropbox.com/s/7rdv1t11yrawosc/vqa-mcb-pretrained-290000.tar.gz?dl=0)

 **Train Time:** 5 days (~126 hours)
 
 **Training iterations:** ~290,000
 
 **GPU Used:** NVIDIA 1080 Ti (Pascal)

## Live Demo

You can upload your own images and ask the model your own questions. [Try the live demo!](http://demo.berkeleyvision.org/)

## Prerequisites

In order to use our pretrained model:

1) Download and compile my fork of Caffe, which includes the required MCB layers [here](https://github.com/brandonjabr/caffe-mcb)

**Note:** You can easily download and compile this version of Caffe using my [UbuntuDL bash script](https://github.com/brandonjabr/UbuntuDL)


2) Download the [pre-trained ResNet-152 model](https://github.com/KaimingHe/deep-residual-networks).


If you want to **train from scratch**, do the above plus:

- Download the [VQA tools](https://github.com/VT-vision-lab/VQA).
- Download the [VQA real-image dataset](http://visualqa.org/download.html).
- Optional: Install spaCy and download GloVe vectors. The latest stable release of spaCy has a bug that prevents GloVe vectors from working, so you need to install the HEAD version. See `train/README.md`.
- Optional: Download [Visual Genome](https://visualgenome.org/) data.

## Data Preprocessing

See `preprocess/README.md`.

## Training

See `train/README.md`.

## Evaluation

To generate an answers JSON file in the format expected by the VQA evaluation code and VQA test server, you can use `eval/ensemble.py`. This code can also ensemble multiple models. Running `python ensemble.py` will print out a help message telling you what arguments to use.

## Demo Server

The code that powers our [live demo](http://demo.berkeleyvision.org/) is in `server/`. To run this, you’ll need to install Flask and change the constants at the top of `server.py`. Then, just do `python server.py`, and the server will bind to `0.0.0.0:5000`.

## License and Citation

This code and the pretrained model is released under the BSD 2-Clause license. See `LICENSE` for more information.

Please cite [our paper](https://arxiv.org/abs/1606.01847) if it helps your research:

```
@article{fukui16mcb,
  title={Multimodal Compact Bilinear Pooling for Visual Question Answering and Visual Grounding},
  author={Fukui, Akira and Park, Dong Huk and Yang, Daylen and Rohrbach, Anna and Darrell, Trevor and Rohrbach, Marcus},
  journal={arXiv:1606.01847},
  year={2016},
}
```
