import torch
from torch.utils.mobile_optimizer import optimize_for_mobile

torchscript_model = "Your path"
export_model_name = "Your pt name.torchscript.ptl"

model = torch.jit.load(torchscript_model)
optimized_model = optimize_for_mobile(model)
optimized_model._save_for_lite_interpreter(export_model_name)

print(f"mobile optimized model exported to {export_model_name}")
