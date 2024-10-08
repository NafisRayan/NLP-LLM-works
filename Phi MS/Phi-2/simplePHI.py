"""## Tokenizer and Model Prep"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/phi-2",
    trust_remote_code = True
)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/phi-2",
    torch_dtype = "auto",
    device_map = "auto",
    trust_remote_code = True
)

prompt = """Give me a list of 13 words that have 9 letters."""

with torch.no_grad():
  token_ids = tokenizer.encode(prompt, add_special_tokens=False ,return_tensors="pt")
  output_ids = model.generate(
      token_ids.to(model.device),
      max_new_tokens=512,
      do_sample=True,
      temperature = 0.3
  )

output = tokenizer.decode(output_ids[0][token_ids.size(1) :])

print(output)