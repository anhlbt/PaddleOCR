# illustrate

This project is based on FastAPI integrated PaddleOCR to realize text recognition of pictures and PDF files.
Using the new identification model PP-OCRv5 released on May 20, 2025, the test found that the recognition accuracy and speed have been improved.
The original content developed based on PP-OCRv4 has been switched to the branch PP-OCRv4, and you can access [PP-OCRv4](https://github.com/self4m/PaddleOCRFastAPI/tree/PP-OCRv4) to view

# Identification instructions
It should be noted that untrained models are more suitable for identifying text with uniform formats and font specifications, such as:
>Standard printed text:
> - Such as books, printed documents, PDF export content, clear scanned copies.
> - Font specification, alignment rules, normal spacing, no distortion or occlusion.
>
> No complex layout format:
> - Plain text or simple structure: such as left alignment, neat paragraphs, no multiple columns, tables, and mixed pictures.
>
> Clean background, no noise:
> - Black characters on white background are the best, without interference from shadows, watermarks, modifications, wrinkles, etc.

If you need to identify and extract text in a specific format, such as tickets, tables, etc., you need to do data annotation and then train an exclusive model.

----

# Installation steps


1. Installation dependencies
* First visit the official website to install PaddlePaddle (select the appropriate version according to the system and environment)
[https://www.paddlepaddle.org.cn/install/quick](https://www.paddlepaddle.org.cn/install/quick)

* Install other dependencies:
```bash
pip install -r requirements.txt
```

2. Model files and configuration
The full model has been configured in the project warehouse and no download is required.
Identify the configuration file contents are stored in `ocr_config.yaml`

3. Start the project via the command line
```bash
uvicorn start:app --host 127.0.0.1 --port 8888 --reload
```
* If you want to allow LAN access, you can modify the startup command and change `127.0.0.1` to `0.0.0.0`

---

# Interface Documentation

The following is an interface call document generated based on the code you provide, which describes how to call the API interface `/ocr` of the OCR text recognition tool.

### OCR Text Recognition Service Interface Document

#### Basic information
- **URL**: `/ocr`
- **HTTP method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Response Format**: `application/json`

#### Request parameters

| Parameter name | Type | Necessary | Description |
|--------|------------|----------|--------------------------|
| file | File (File) | Yes | The image or PDF file that needs to be uploaded. Supported image types include JPEG, PNG, etc.; support PDF files. |

#### Return field

- **result**: Contains a list of texts recognized by OCR.
- **detail_time**: The time required for processing (seconds).
- **image_list**: Base64 encoding list of images processed on each page. Each image is the result image after OCR labeling.
- **error**: The information returned when an error occurs (if any).

#### Sample Request

Use the `curl` command line tool to test:

```bash
curl -X POST "http://127.0.0.1:8000/ocr" \
-H "accept: application/json" \
-F "file=@/path/to/your/file.png"
```

Please note that replace `/path/to/your/file.png` with the actual file path.

#### Sample Response

In the case of success:

```json
{
"result": ["identification", "result", "example"],
"detail_time": 1.234,
"image_list": [
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAA...",
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAA..."
]
}
```

Here each element in `image_list` is a base64 encoded string of the processed image and can be directly embedded into HTML to display.

In error case:

```json
{
"error": "Unsupported file type",
"detail_time": 0.002
}
```

or

```json
{
"error": "File processing failed: [specific error message]",
"detail_time": 0.005
}
```

Or

```json
{
"error": "OCR recognition failed: [specific error message]",
"detail_time": 0.005
}
```

# Offline deployment
Take devices using CUDA version 12.6 NVIDIA GPU as an example:
1. clone this project on devices with the same system with network
2. Comment `paddlepaddle-gpu==3.0.0` in the `requirements.txt` file
3. Execute the following command to download dependencies
```bash
pip download -r requirements.txt -d packages
```
4. Download the `paddlepaddle-gpu==3.0.0` dependency separately
```bash
pip download paddlepaddle-gpu==3.0.0 -d packages -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
```
5. Copy the `packages` directory to the target device's repository
6. Install all dependencies
```bash
pip install --no-index --find-links=packages -r requirements.txt
```
7. Start the project