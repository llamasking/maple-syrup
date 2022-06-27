from transformers import AutoTokenizer, AutoModelForCausalLM, Conversation, pipeline
from utils.clean_text import clean_text
from utils.config import config

class ConversationalGenerator():
    """
    Abstraction class allowing for simplified use of the conversational text
    generation model with minimal code needed.
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(config["CONVERSATION_GENERATION_MODEL"])
        self.model = AutoModelForCausalLM.from_pretrained(config["CONVERSATION_GENERATION_MODEL"])
        self.generator = pipeline("conversational", model=self.model, tokenizer=self.tokenizer)

    def __call__(self, message: str) -> str:
        """
        Generates a conversational response to the given message.

        TODO: Does not yet implement conversation context.

        Parameters:
            message (str): Message used to generate text from.

        Returns:
            str: Response
        """

        # Generate output
        gen_output = self.generator(Conversation(message), clean_up_tokenization_spaces=True)

        return clean_text(gen_output.generated_responses[-1])
