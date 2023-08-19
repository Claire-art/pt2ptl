# 안드로이드 스튜디오에서 YOLOv5 적용하기


**1. Clone Yolov5 GitHub repo**
```
git clone https://github.com/ultralytics/yolov5.git
```


**2. Install dependencies to export YOLOv5 model**
```
pip install -r requirements.txt
```

**3. Export YOLOv5s torchscript model**
```
python export.py --weights yolov5s.pt --include torchscript
```

**4. Optimize model for PyTorch Mobile use**

3단계를 완료하면 토치스크립트 형식의 파일이 저장됩니다.

해당 파일을 이용하여 ptl 파일로 변환하면 됩니다.
```python
import torch
from torch.utils.mobile_optimizer import optimize_for_mobile

torchscript_model = "Your model.torchscript"
export_model_name = "Your model name.torchscript.ptl"

model = torch.jit.load(torchscript_model)
optimized_model = optimize_for_mobile(model)
optimized_model._save_for_lite_interpreter(export_model_name)

print(f"mobile optimized model exported to {export_model_name}")
```

```
python optimize.py
```
