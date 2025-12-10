import numpy as np
import cv2

try:
    import albumentations as A
except ImportError:
    A = None


class Albumentations(object):
    def __init__(self, transforms, **kwargs):
        """
        Wrapper để tích hợp Albumentations vào PaddleOCR Config.
        Args:
            transforms (list): Danh sách các dictionary cấu hình cho từng transform.
        """
        if A is None:
            raise ImportError(
                "Vui lòng cài đặt albumentations: pip install albumentations"
            )

        aug_list = []
        for op in transforms:
            name = op.pop("type")
            if hasattr(A, name):
                # Khởi tạo class từ tên string trong config
                aug_class = getattr(A, name)
                aug_list.append(aug_class(**op))
            else:
                print(f"Cảnh báo: Albumentations không có transform '{name}'")

        self.aug = A.Compose(aug_list)

    def __call__(self, data):
        img = data["image"]
        # Albumentations yêu cầu ảnh input là numpy array (H, W, C)
        # PaddleOCR DecodeImage thường trả về BGR hoặc RGB

        res = self.aug(image=img)
        data["image"] = res["image"]
        return data



# Bước 1: File Wrapper cho Albumentations
# Bạn cần lưu code này vào thư mục ppocr/data/imaug/albumentations_aug.py và thêm dòng from .albumentations_aug import Albumentations 
# vào file ppocr/data/imaug/__init__.py để đăng ký nó.