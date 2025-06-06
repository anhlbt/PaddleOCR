from paddleocr import PaddleOCR
import os

# Chọn GPU số 0
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import paddle

print("Using device:", paddle.get_device())

ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv5_server_det",  # "PP-OCRv5_server_det",
    text_recognition_model_name="PP-OCRv5_server_rec",
    # text_recognition_model_dir="/media/anhlbt/SSD2/workspace/OCR/PaddleOCR/PP-OCRv5_server_rec_infer",
    text_recognition_model_dir="/media/anhlbt/SSD2/workspace/OCR/PaddleOCR/output/PP-OCRv5_server_rec_infer",
    # text_recognition_batch_size=None,
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
)  # 更换 PP-OCRv5_server 模型
# ocr = PaddleOCR(
result = ocr.predict("train_word_3.png")
for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")
