
# 🧠 Hướng Dẫn Fine-tune Mô Hình Text Recognition PP-OCRv4 với PaddleOCR

Dưới đây là hướng dẫn chi tiết để fine-tune mô hình nhận dạng văn bản (text recognition) **PP-OCRv4** của PaddleOCR trên tập dữ liệu tùy chỉnh, dựa trên tài liệu chính thức từ PaddleOCR.

---

## 📦 1. Chuẩn Bị Môi Trường

### a. Cài Đặt PaddleOCR

```bash
# Clone repository PaddleOCR
git clone https://github.com/PaddlePaddle/PaddleOCR.git
cd PaddleOCR

# Cài đặt các thư viện phụ thuộc
pip install -r requirements.txt
```

### b. Cài PaddlePaddle

Hướng dẫn cài đặt tại: https://www.paddlepaddle.org.cn/install/quick

---

## 📁 2. Chuẩn Bị Dữ Liệu

Tạo tập dữ liệu với cấu trúc như sau:

```
dataset/
├── train/
│   ├── images/
│   └── label.txt
├── val/
│   ├── images/
│   └── label.txt
```

**label.txt** (mỗi dòng):

```
images/img_1.jpg	Hello World
images/img_2.jpg	Example Text
```

**dict.txt**: danh sách ký tự sử dụng trong tập dữ liệu, mỗi ký tự một dòng.

---

## ⚙️ 3. Cấu Hình Huấn Luyện

### a. Sao chép và chỉnh sửa tệp cấu hình

```bash
cp configs/rec/PP-OCRv4/en_PP-OCRv4_rec.yml configs/rec/PP-OCRv4/custom_PP-OCRv4_rec.yml
```

### b. Chỉnh sửa `custom_PP-OCRv4_rec.yml`:

```yaml
Train:
  dataset:
    name: SimpleDataSet
    data_dir: ./dataset/train/images
    label_file_list: ["./dataset/train/label.txt"]
    transforms:
      - DecodeImage: {img_mode: "RGB", channel_first: False}
      - RecResizeImg: {image_shape: [3, 48, 320]}
      - KeepKeys: {keep_keys: ["image", "label"]}
Eval:
  dataset:
    name: SimpleDataSet
    data_dir: ./dataset/val/images
    label_file_list: ["./dataset/val/label.txt"]
    transforms:
      - DecodeImage: {img_mode: "RGB", channel_first: False}
      - RecResizeImg: {image_shape: [3, 48, 320]}
      - KeepKeys: {keep_keys: ["image", "label"]}

Global:
  character_dict_path: ./dataset/dict.txt
  use_space_char: True
  save_model_dir: ./output/rec_PP-OCRv4_custom
  pretrained_model: ./pretrained_models/PP-OCRv4/en_PP-OCRv4_rec_train
```

---

## 🚀 4. Huấn Luyện Mô Hình

```bash
python3 tools/train.py -c configs/rec/PP-OCRv4/custom_PP-OCRv4_rec.yml
```

---

## 📤 5. Xuất Mô Hình Suy Luận

```bash
python3 tools/export_model.py \
  -c configs/rec/PP-OCRv4/custom_PP-OCRv4_rec.yml \
  -o Global.pretrained_model=./output/rec_PP-OCRv4_custom/best_accuracy \
     Global.save_inference_dir=./inference/rec_PP-OCRv4_custom
```

---

## 🧪 6. Kiểm Tra Mô Hình

```bash
python3 tools/infer_rec.py \
  -c configs/rec/PP-OCRv4/custom_PP-OCRv4_rec.yml \
  -o Global.infer_img=./dataset/val/images/img_1.jpg \
     Global.pretrained_model=./output/rec_PP-OCRv4_custom/best_accuracy
```

---

## 📝 Lưu Ý

- Đảm bảo cấu trúc thư mục và đường dẫn chính xác.
- Tải mô hình tiền huấn luyện phù hợp với ngôn ngữ.
- Tùy chỉnh batch size, learning rate... cho phù hợp tài nguyên của bạn.
