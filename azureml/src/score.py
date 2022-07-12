import json
import os

from azureml.contrib.services.aml_request import AMLRequest, rawhttp
from azureml.contrib.services.aml_response import AMLResponse

def init():
    # TODO: onnxのデプロイ
    pass

@rawhttp
def run(data):
        # POST以外は受け付けない
    if request.method != 'POST':
        return AMLResponse("bad request", 500)
    
    # 画像を取得
    file_bytes = request.files["image"]

    # TODO: onnxのデプロイ

    # 結果を生成
    res_body = {}
    for prediction in results.predictions:
        res_body[prediction.tag_name] = prediction.probability * 100
    return f"{res_body}"