from typing import List, Any

from tokenization_internlm import InternLMTokenizer
from modeling_internlm import InternLMForCausalLM
from configuration_internlm import InternLMConfig


class Inferencer:

    def __init__(self) -> None:
        #self.tokenizer = InternLMTokenizer("tokenizer.model", '<unk', '<s>', '</s>', '</s>')

        # tokens = tokenizer.tokenize("How are you?")
        # print(tokens)

        # ids = tokenizer.convert_tokens_to_ids(tokens)
        # print(ids)

        #self.model = InternLMForCausalLM(InternLMConfig())
        #self.model.eval()
        # response, history = model.chat(tokenizer, "hello", history=[])
        pass


    def __call__(self, *args: Any, **kwds: Any) -> List:
        #return self.model.chat(self.tokenizer, "hello", history=[])
        return "hello"


inferencer = Inferencer()





