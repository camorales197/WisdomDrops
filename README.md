# WisdomDrops

Distribute knowledge from LLMs in a structured way.

## Installation

To get started with this project, you need to have [Poetry](https://python-poetry.org/) installed. Poetry is a dependency management tool for Python.

### Installing Poetry

Follow the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation) to install Poetry on your system.

### Setting Up the Project

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/wisdomdrops.git
    cd wisdomdrops
    ```

2. Install the project dependencies using Poetry:
    ```sh
    poetry install
    ```

## Usage

To generate a curriculum using the `CurriculumGenerator`, follow these steps:

1. Activate the Poetry shell:
    ```sh
    poetry shell
    ```

2. Run the curriculum generation script:
    ```sh
    python src/curriculum/generate_curriculum.py
    ```

Replace the `topic` variable in the script with the topic of your choice.

## Configuration

The configuration for the curriculum generation is located in `src/curriculum/config.yaml`. You can modify this file to change the model or the prompt template used for generating the curriculum.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
