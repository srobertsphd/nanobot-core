from typing import Dict, List, Tuple
from tiktoken import get_encoding
from transformers.tokenization_utils_base import PreTrainedTokenizerBase


class OpenAITokenizerWrapper(PreTrainedTokenizerBase):
    """Minimal wrapper for OpenAI's tokenizer"""
    
    def __init__(
        self, model_name: str = "cl100k_base", max_length: int = 8192, **kwargs,
    ):
        """initialize the tokenizer
        
        Args:
            model_name: the name of the OpenAI encoding to use
           max_length: the maximum sequence length
        """
        super().__init__(model_max_length=max_length,**kwargs)
        self.tokenizer = get_encoding(model_name)
        self._vocab_size = self.tokenizer.max_token_value
        
        
    def tokenize(self, text: str, **kwargs) -> List[str]:
        """Main method used by hybrid chunker"""
        return [str(t) for t in self.tokenizer.encode(text)]
    
    def _tokenize(self, text: str) -> List[str]:
        return self.tokenize(text)
    
    def convert_token_to_id(self, token: str) -> int:
        return int(token)
    
    def convert_id_to_token(self, index: int) -> str:
        return str(index)
    
    def get_vocab(self) -> Dict[str, int]:
        return dict(enumerate(range(self.vocab_size)))
    
    @property
    def vocab_size(self) -> int:
        return self._vocab_size
    
    def save_vocabulary(self, *args) -> Tuple[str]:
        return ()
    
    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        """class method to match HuggingFace's interface."""
        return cls

    def _encode_plus(self, text: str, **kwargs) -> Dict:
        """Required by PreTrainedTokenizerBase"""
        tokens = self.tokenizer.encode(text)
        return {
            "input_ids": tokens,
            "attention_mask": [1] * len(tokens)
        }