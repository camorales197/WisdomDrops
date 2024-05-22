import os
import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class CurriculumGenerator:
    def __init__(self,):
        """Initializes the CurriculumGenerator with the prompt template from the config file."""
        load_dotenv()
        self.config = self._load_config()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.prompt_template = self.config['prompt_template_curriculum']
        self.chain = self._define_chain(prompt_template=self.prompt_template)

    def _load_config(self, config_path="src/curriculum/config.yaml"):
        """Loads the prompt template from the given YAML configuration file."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
        
    def _define_chain(self, prompt_template):
        """Defines the LangChain LCEL for generating a curriculum."""
        llm = ChatOpenAI(api_key=self.api_key, model=self.config['model'])
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.prompt_template)
            ])
        prompt = ChatPromptTemplate(template=prompt_template, input_variables=["topic"])
        chain = llm | prompt | StrOutputParser()
        return chain

    def generate_curriculum(self, topic):
        """Generates a curriculum for the given topic."""
        response = self.chain.run(topic=topic)
        curriculum = response.strip()
        return curriculum

    def save_curriculum(self, curriculum, filename):
        """Saves the generated curriculum to a file."""
        with open(filename, 'w') as file:
            file.write(curriculum)

if __name__ == "__main__":
    generator = CurriculumGenerator()
    topic = "Natural Language Processing"  # Replace this with the topic of your choice
    curriculum = generator.generate_curriculum(topic)
    generator.save_curriculum(curriculum, "curriculum.txt")
    print(curriculum)









