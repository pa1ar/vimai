import openai
import os
import subprocess
import json
import glob
import openai_api

def main():
    while True:
        # Get user input
        print("current working directory:", os.getcwd())
        user_input = input("enter your request: ")
        
        # Updated system message
        system_message = "you are receiving natural language input and outputting a response in a dictionary format. The dictionary consists of two keys: 'vim_cmd' for the Vim command, and 'files' for the filenames or file patterns. Based on the user input, generate the appropriate response. For example, if the user says 'remove word 'test' from all .txt files', you would output something like '{\"vim_cmd\": \"<vim command in following format: vim -c 'command | update' -c 'qa'>\", \"files\": \".txt\"}'. Output only json, without markdown syntax. Generate a response to: "
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ]

        # Get the response from OpenAI
        response = openai_api.openai_call(messages)
        print("your vim cmd:", response)

        # Parse the response
        try:
            response_dict = json.loads(response)
            vim_command = response_dict["vim_cmd"]
            file_pattern = response_dict["files"]
        except (json.JSONDecodeError, KeyError):
            print("ERROR: parsing the response failed. GPT probably screwed up something. Try again.")
            continue  # Continue to the next iteration

        # Ask the user whether to apply the command
        decision = input("apply command? (Yes/No/Restart/Exit): ").strip().lower()
        if decision == 'y' or decision == 'yes':
            try:
                matched_files = glob.glob(file_pattern)
                print(f"matched files: {matched_files}")
                if not matched_files:
                    print("ERROR: no files matched the specified pattern.")
                    continue  # Continue to the next iteration
                for file in matched_files:
                    full_command = f"{vim_command} {file}"
                    print(f"-- executing command: {full_command}")
                    subprocess.run(full_command, shell=True)
                    print(f"-- command applied successfully to {file}")
            except Exception as e:
                print("ERROR executing the command failed:", e)
        elif decision in ['e', 'q', ':q']:
            break
        elif decision == 'r':
            continue
        elif decision == 'n':
            restart_or_quit = input("Restart or Quit? (r/q): ").strip().lower()
            if restart_or_quit == 'q':
                break
            elif restart_or_quit == 'r':
                continue
        
        # loop
        next_task = input("again? (y/n): ").strip().lower()
        if next_task in ['n', 'no', 'exit', 'e']:
            break

if __name__ == "__main__":
    main()
