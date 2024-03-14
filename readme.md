# vimai

a Python tool that executes Vim commands based on natural language input, which are applied on target file.

## Dependencies

- OpenAI API
- OpenAI python package 

## Installation

### get your OpenAI API key
Go [here](https://platform.openai.com/docs/quickstart) and follow the instructions.

### install OpenAI python package
`pip install openai`

### clone vimai
`git clone https://github.com/pa1ar/vimai.git`

alternatively you can install it with pip
`pip install vimai`

## Usage

> Disclaimer: This is largely just a demo, which is powered by AI, so probably don't use it for anything important.

when you run the script for the first time, it will ask for API key, which will be stored in constants file locally. not ideal, but i wanted to make it simple.

1. run the script with `python path/to/vimai`
2. provide instructions
3. (your working directory is the directory where the script will look for files)
