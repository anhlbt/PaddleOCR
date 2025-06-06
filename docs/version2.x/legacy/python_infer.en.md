---
typora-copy-images-to: images
comments: true
hide:
  - toc
---

# Python Inference for PP-OCR Model Zoo

This article introduces the use of the Python inference engine for the PP-OCR model library. The content is in order of text detection, text recognition, direction classifier and the prediction method of the three in series on the CPU and GPU.

## Text Detection Model Inference

The default configuration is based on the inference setting of the DB text detection model. For lightweight Chinese detection model inference, you can execute the following commands:

```bash linenums="1"
# download DB text detection inference model
wget  https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-OCRv3_mobile_det_infer.tar
tar xf PP-OCRv3_mobile_det_infer.tar
# run inference
python3 tools/infer/predict_det.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/"
```

The visual text detection results are saved to the ./inference_results folder by default, and the name of the result file is prefixed with 'det_res'. Examples of results are as follows:

![img](./images/det_res_00018069.jpg)

You can use the parameters `limit_type` and `det_limit_side_len` to limit the size of the input image,
The optional parameters of `limit_type` are [`max`, `min`], and
`det_limit_size_len` is a positive integer, generally set to a multiple of 32, such as 960.

The default setting of the parameters is `limit_type='max', det_limit_side_len=960`. Indicates that the longest side of the network input image cannot exceed 960,
If this value is exceeded, the image will be resized with the same width ratio to ensure that the longest side is `det_limit_side_len`.
Set as `limit_type='min', det_limit_side_len=960`, it means that the shortest side of the image is limited to 960.

If the resolution of the input picture is relatively large and you want to use a larger resolution prediction, you can set det_limit_side_len to the desired value, such as 1216:

```bash linenums="1"
python3 tools/infer/predict_det.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --det_limit_type=max --det_limit_side_len=1216
```

If you want to use the CPU for prediction, execute the command as follows

```bash linenums="1"
python3 tools/infer/predict_det.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/"  --use_gpu=False
```

## Text Recognition Model Inference

### 1. Lightweight Chinese Recognition Model Inference

**Note**: The input shape used by the recognition model of `PP-OCRv3` is `3, 48, 320`. If you use other recognition models, you need to set the parameter `--rec_image_shape` according to the model. In addition, the `rec_algorithm` used by the recognition model of `PP-OCRv3` is `SVTR_LCNet` by default. Note the difference from the original `SVTR`.

For lightweight Chinese recognition model inference, you can execute the following commands:

```bash linenums="1"
# download CRNN text recognition inference model
wget  https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/PP-OCRv4_mobile_rec_infer.tar
tar xf PP-OCRv3_mobile_rec_infer.tar
# run inference
python3 tools/infer/predict_rec.py --image_dir="./doc/imgs_words_en/word_10.png" --rec_model_dir="./PP-OCRv3_mobile_rec_infer/" --rec_image_shape=3,48,320
```

![img](./images/word_10.png)

After executing the command, the prediction results (recognized text and score) of the above image will be printed on the screen.

```bash linenums="1"
Predicts of ./doc/imgs_words_en/word_10.png:('PAIN', 0.988671)
```

### 2. English Recognition Model Inference

For English recognition model inference, you can execute the following commands,you need to specify the dictionary path used by `--rec_char_dict_path`:

```bash linenums="1"
# download en model：
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0.0/en_PP-OCRv3_mobile_rec_infer.tar
tar xf en_PP-OCRv3_mobile_rec_infer.tar
python3 tools/infer/predict_rec.py --image_dir="./doc/imgs_words/en/word_1.png" --rec_model_dir="./en_PP-OCRv3_mobile_rec_infer/" --rec_char_dict_path="ppocr/utils/en_dict.txt"
```

![img](./images/word_1.png)

After executing the command, the prediction result of the above figure is:

```bash linenums="1"
Predicts of ./doc/imgs_words/en/word_1.png: ('JOINT', 0.998160719871521)
```

### 3. Multilingual Model Inference

If you need to predict [other language models](../model_list.en.md), when using inference model prediction, you need to specify the dictionary path used by `--rec_char_dict_path`. At the same time, in order to get the correct visualization results,
You need to specify the visual font path through `--vis_font_path`. There are small language fonts provided by default under the `doc/fonts` path, such as Korean recognition:

```bash linenums="1"
wget wget https://paddleocr.bj.bcebos.com/dygraph_v2.0/multilingual/korean_mobile_v2.0_rec_infer.tar

python3 tools/infer/predict_rec.py --image_dir="./doc/imgs_words/korean/1.jpg" --rec_model_dir="./your inference model" --rec_char_dict_path="ppocr/utils/dict/korean_dict.txt" --vis_font_path="doc/fonts/korean.ttf"
```

![img](./images/1.jpg)

After executing the command, the prediction result of the above figure is:

```text linenums="1"
Predicts of ./doc/imgs_words/korean/1.jpg:('바탕으로', 0.9948904)
```

## Angle Classification Model Inference

For angle classification model inference, you can execute the following commands:

```bash linenums="1"
# download text angle class inference model：
wget  https://paddleocr.bj.bcebos.com/dygraph_v2.0/ch/ch_ppocr_mobile_v2.0_cls_infer.tar
tar xf ch_ppocr_mobile_v2.0_cls_infer.tar
python3 tools/infer/predict_cls.py --image_dir="./doc/imgs_words_en/word_10.png" --cls_model_dir="ch_ppocr_mobile_v2.0_cls_infer"
```

![img](./images/word_10.png)

After executing the command, the prediction results (classification angle and score) of the above image will be printed on the screen.

```text linenums="1"
 Predicts of ./doc/imgs_words_en/word_10.png:['0', 0.9999995]
```

## Text Detection Angle Classification and Recognition Inference Concatenation

**Note**: The input shape used by the recognition model of `PP-OCRv3` is `3, 48, 320`. If you use other recognition models, you need to set the parameter `--rec_image_shape` according to the model. In addition, the `rec_algorithm` used by the recognition model of `PP-OCRv3` is `SVTR_LCNet` by default. Note the difference from the original `SVTR`.

When performing prediction, you need to specify the path of a single image or a folder of images through the parameter `image_dir`, pdf file is also supported, the parameter `det_model_dir` specifies the path to detect the inference model, the parameter `cls_model_dir` specifies the path to angle classification inference model and the parameter `rec_model_dir` specifies the path to identify the inference model. The parameter `use_angle_cls` is used to control whether to enable the angle classification model. The parameter `use_mp` specifies whether to use multi-process to infer `total_process_num` specifies process number when using multi-process. The parameter . The visualized recognition results are saved to the `./inference_results` folder by default.

```bash linenums="1"
# use direction classifier
python3 tools/infer/predict_system.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --cls_model_dir="./cls/" --rec_model_dir="./PP-OCRv3_mobile_rec_infer/" --use_angle_cls=true
# not use use direction classifier
python3 tools/infer/predict_system.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --rec_model_dir="./PP-OCRv3_mobile_rec_infer/" --use_angle_cls=false
# use multi-process
python3 tools/infer/predict_system.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --rec_model_dir="./PP-OCRv3_mobile_rec_infer/" --use_angle_cls=false --use_mp=True --total_process_num=6
# use PDF files, you can infer the first few pages by using the `page_num` parameter, the default is 0, which means infer all pages
python3 tools/infer/predict_system.py --image_dir="./xxx.pdf" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --cls_model_dir="./cls/" --rec_model_dir="./PP-OCRv3_mobile_rec_infer/" --use_angle_cls=true --page_num=2
```

After executing the command, the recognition result image is as follows:

![](./images/system_res_00018069_v3.jpg)

For more configuration and explanation of inference parameters, please refer to：[Model Inference Parameters Explained Tutorial](../blog/inference_args.en.md)。

## TensorRT Inference

Paddle Inference ensembles TensorRT using subgraph mode. For GPU deployment scenarios, TensorRT can optimize some subgraphs, including horizontal and vertical integration of OPs, filter redundant OPs, and automatically select the optimal OP kernels for to speed up inference.

You need to do the following 2 steps for inference using TRT.

* (1) Collect the dynamic shape information of the model about a specific dataset and store it in a file.
* (2) Load the dynamic shape information file for TRT inference.

Taking the text detection model as an example. Firstly, you can use the following command to generate a dynamic shape file, which will eventually be named as `det_trt_dynamic_shape.txt` and stored in the `PP-OCRv3_mobile_det_infer` folder.

```bash linenums="1"
python3 tools/infer/predict_det.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --use_tensorrt=True
```

The above command is only used to collect dynamic shape information, and TRT is not used during inference.

Then, you can use the following command to perform TRT inference.

```bash linenums="1"
python3 tools/infer/predict_det.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./PP-OCRv3_mobile_det_infer/" --use_tensorrt=True
```

**Note:**

* In the first step, if the dynamic shape information file already exists, it does not need to be collected again. If you want to regenerate the dynamic shape information file, you need to delete the dynamic shape information file in the model folder firstly, and then regenerate it.
* In general, dynamic shape information file only needs to be generated once. In the actual deployment process, it is recommended that the dynamic shape information file can be generated on offline validation set or test set, and then the file can be directly loaded for online TRT inference.
