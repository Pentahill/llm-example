from typing import List, Any

from tokenization_internlm import InternLMTokenizer
from modeling_internlm import InternLMForCausalLM
from configuration_internlm import InternLMConfig


tokenizer = InternLMTokenizer("tokenizer.model", '<unk', '<s>', '</s>', '</s>')
model = InternLMForCausalLM(InternLMConfig())
model.eval()
response, history = model.chat(tokenizer, "hello", history=[])
print(response)






