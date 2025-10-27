from dotenv import load_dotenv
import os


load_dotenv()
deepseek_key =os.environ.get("DEEPSEEK_API_KEY")

def main():
    print("Hello from langchain-langgraph-project!")


if __name__ == "__main__":
    main()
