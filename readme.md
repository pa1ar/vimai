# vimai

a Python tool that executes Vim commands based on natural language input, which are applied on target file.

[![demo](https://i3.ytimg.com/vi/PjNn66o_-0g/hqdefault.jpg)](https://youtu.be/PjNn66o_-0g)

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

## Usage

> Disclaimer: This is largely just a demo, which is powered by AI, so probably don't use it for anything important.

when you run the script for the first time, it will ask for API key, which will be stored in constants file locally. not ideal, but i wanted to make it simple.

1. run the script with `python path/to/vimai`
2. provide instructions
3. (your working directory is the directory where the script will look for files)

### what else

consider checking [Apple Shortcuts](https://1ar.io/tools) which i am using myself, maybe you will too. :3