from paddleocr import PaddleOCR

# ocr = PaddleOCR(
#     use_doc_orientation_classify=False,
#     use_doc_unwarping=False,
#     use_textline_orientation=False) # Text detection + text recognition

# ocr = PaddleOCR(use_doc_orientation_classify=True, use_doc_unwarping=True) # 文本图像预处理+文本检测+方向分类+文本识别
# ocr = PaddleOCR(use_doc_orientation_classify=False, use_doc_unwarping=False) # 文本检测+文本行方向分类+文本识别
ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv5_server_det", #"PP-OCRv5_server_det",
    text_recognition_model_name="PP-OCRv5_server_rec",
    text_recognition_model_dir="/media/anhlbt/SSD2/workspace/OCR/PaddleOCR/PP-OCRv5_server_rec_infer",
    # text_recognition_batch_size=None,    
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False) # 更换 PP-OCRv5_server 模型
# ocr = PaddleOCR(
result = ocr.predict("train_word_3.png")
for res in result:
    res.print()
    res.save_to_img("output")
    res.save_to_json("output")