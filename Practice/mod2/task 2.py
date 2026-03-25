import sys
import re

def main():
    text = sys.stdin.read()

    pattern = re.compile(r'[a-zA-Z0-9+_\-#]+@[a-zA-Z0-9.-]+')
    emails = pattern.findall(text)
    for email in emails:
        print(email)

if __name__ == "__main__":
    main()