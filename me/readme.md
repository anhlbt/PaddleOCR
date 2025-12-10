## install
python -m pip install paddlepaddle-gpu==3.0.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

paddlex
pip install "paddlex[base]==3.0.1"

## train
python3 tools/train.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml

## train dataset paddleocr
## train
python tools/train.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_a0.yml

python tools/train.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_all.yml


## export 
python3 tools/export_model.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_a0.yml -o \
Global.pretrained_model=output/PP-OCRv5_server_rec_a0/best_accuracy.pdparams \
Global.save_inference_dir="output/PP-OCRv5_server_rec_a0_infer/"


python3 tools/export_model.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_all.yml -o \
Global.pretrained_model=output/PP-OCRv5_server_rec_all/best_accuracy.pdparams \
Global.save_inference_dir="output/PP-OCRv5_server_rec_all_infer/"



## infer
python3 tools/infer_rec.py \
    -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_a0.yml \
    -o Global.infer_img=/media/SSD3/paddleocr_dataset/dictionary_text_vi_bg_5/dictionary_text_vi_bg_5/4.jpg \
       Global.pretrained_model=output/PP-OCRv5_server_rec_a0_infer \
       Global.save_res_path=output/PP-OCRv5_server_rec_a0_infer/output.txt



python3 tools/infer_rec.py \
    -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_all.yml \
    -o Global.infer_img=/media/SSD3/paddleocr_dataset/dictionary_text_ko_bg_5/dictionary_text_ko_bg_5/12.jpg \
       Global.pretrained_model=output/PP-OCRv5_server_rec_all_infer \
       Global.save_res_path=output/PP-OCRv5_server_rec_all_infer/output.txt


## eval
python3 tools/eval.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec_a0.yml -o \
Global.pretrained_model=output/PP-OCRv5_server_rec_a0/xxx.pdparams


## formula_recognition
https://github.com/PaddlePaddle/PaddleX/blob/release/3.0/docs/module_usage/tutorials/ocr_modules/formula_recognition.en.md


```python
from rdkit import Chem
from rdkit.Chem import Draw

mol = Chem.MolFromSmiles("CC(C)CC1=CC=C(C=C1)C(C)C(=O)O")
img = Draw.MolToImage(mol)
img.save("molecule.png")

```

```latex
\ce{CH3COOH + NaOH -> CH3COONa + H2O}

```