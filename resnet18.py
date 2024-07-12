# example code to run resnet18 model with SpaceMITExecutionProvider

import onnxruntime as ort
import numpy as np
import spacemit_ort
net_param_path = "resnet18.q.onnx"
session = ort.InferenceSession(net_param_path, providers=["SpaceMITExecutionProvider"])
input_tensor = np.ones((1, 3, 224, 224), dtype=np.float32)
outputs = session.run(None, {"data": input_tensor})