import requests

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        req_result = requests.get(sys.argv[1])
    else:
        req_result = requests.get("http://www.iciba.com/")
    print(req_result.headers)
