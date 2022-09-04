from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from utils.clean_text import clean_text
from utils.config import config


class TextGenerator():
    """
    Abstraction class allowing for simplified use of the text generation model
    with minimal code needed.
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            config["TEXT_GENERATION_MODEL"], cache_dir=config["MODEL_CACHE_DIR"])
        self.model = AutoModelForCausalLM.from_pretrained(
            config["TEXT_GENERATION_MODEL"], cache_dir=config["MODEL_CACHE_DIR"])
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def __call__(self, prompt: str, num_results: int = 1) -> list[str]:
        """
        Generates predicted continuation to the text starting with the provided prompt.

        Parameters:
            prompt (str): Prompt used to generate text from.
            num_results (int): Number of results to generate and return.

        Returns:
            list[str]: List containing `num_results` many generation outcomes.
        """

        # Generate output
        gen_output = self.generator(prompt,
                                    num_return_sequences=num_results,
                                    clean_up_tokenization_spaces=True)

        # Reformat output
        results = [clean_text(output["generated_text"]) for output in gen_output]

        return results
