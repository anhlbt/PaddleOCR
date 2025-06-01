
# 📚 Hướng dẫn chuẩn bị Dataset tốt nhất cho Recognition với PaddleOCR v4

## 🎯 1. Kích thước ảnh tốt nhất cho Recognition

PaddleOCR resize ảnh Recognition về dạng chuẩn:

- **Chiều cao (height)**: `32 pixels`
- **Chiều rộng (width)**: tùy theo độ dài câu, thường ≤ `320`, tối đa `640`.

### ✅ Khuyến nghị:
| Loại Text | Width khuyến nghị |
|-----------|------------------|
| Text ngắn (5–15 ký tự) | 100–160 px |
| Text trung bình (15–30 ký tự) | 160–320 px |
| Text dài (30+ ký tự) | 320–640 px |

> ✅ Resize sao cho **giữ tỉ lệ gốc**, chiều cao = 32, chiều rộng có thể co giãn hoặc pad.

---

## 📦 2. Số lượng mẫu bao nhiêu là đủ tốt?

| Ngữ cảnh | Số lượng mẫu |
|----------|--------------|
| Nhận dạng 1 ngôn ngữ đơn giản | ≥ 50.000 |
| Đa font chữ, đa nhiễu | 100.000–300.000 |
| Đa ngôn ngữ (EN + VI + CN) | 300.000–1.000.000 |
| Tiếng Việt viết tay | ≥ 500.000 |

### 💡 Sinh ảnh tổng hợp:

- Dùng `trdg`, `PIL`, `imgaug` để sinh ảnh từ từ điển (`dict.txt`) + font thực tế.
- Thêm hiệu ứng: noise, blur, affine, shadow, rotate ±10°, brightness shift.

---

## 📚 3. Chuẩn hóa và quản lý dataset

### a. Format file `train.txt` / `val.txt`

```
path/to/image.jpg<TAB>ground_truth_text
```

### b. Charset (`dict.txt`)

```
a
b
c
1
2
!
你
好
```

> ⚠️ Charset phải chứa đủ toàn bộ ký tự có trong tập dữ liệu. Thiếu sẽ lỗi khi decode.

---

## 🚀 4. Mẹo Production-ready

| Yếu tố | Gợi ý |
|--------|-------|
| 🔁 Augmentation | Motion blur, noise, rotation ±10°, brightness shift |
| 🧠 Charset | Giữ tập nhỏ, đủ dùng |
| 🔤 Max token length | ~25–50 ký tự, dài hơn cần crop hoặc dùng transformer |
| ⚙️ Model nhẹ | `rec_mv3_none_bilstm_ctc` phù hợp edge/mobile |
| 📉 Inference | Convert ảnh RGB, resize, normalize trước khi đưa vào model |

---

## ✅ Checklist huấn luyện PaddleOCR Recognition tốt cho production

| Mục tiêu | Trạng thái |
|----------|------------|
| Dataset > 50.000 ảnh | ✅ |
| Ảnh resize chuẩn H=32, W≤320 | ✅ |
| Charset đầy đủ | ✅ |
| Augmentation đúng thực tế | ✅ |
| Tách train/val rõ ràng | ✅ |
| Label đúng format | ✅ |

---

> Nếu bạn cần hỗ trợ thêm cho use case cụ thể như: OCR tiếng Việt, hóa đơn, viết tay, app mobile… vui lòng cung cấp thêm thông tin để mình tối ưu kiến trúc và pipeline nhé.
