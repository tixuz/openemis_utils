from pprint import pprint, pformat

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def catcher():
    try:
        method = request.method
    except Exception as e:
        e_message = "Catcher Exception 1: {0}: {1}".format("Error", str(e))
        print(e_message)
        return e_message
    if method == 'POST':
        try:
            request_json = request.json
            pprint(request_json)
            pretty_json = pformat(request_json)
            output_file_name = "caught_webhooks.txt"
            write_to_file(text_to_write="Caught new institution: " + pretty_json,
                          output_file_name=output_file_name)
            return pretty_json
        except Exception as e:
            e_message = "Catcher Exception 2: {0}: {1}".format("Error", str(e))
            print(e_message)
            return e_message
    if request.method == 'GET':
        return 'Hello, Catcher!'


@app.route('/institutions', methods=['POST', 'GET'])
def institutions_catcher():
    try:
        method = request.method
    except Exception as e:
        e_message = "Institutions Catcher Exception 1: {0}: {1}".format("Error", str(e))
        print(e_message)
        return e_message
    if method == 'POST':
        try:
            request_json = request.json
            pprint(request_json)
            pretty_json = pformat(request_json)
            output_file_name = "caught_institutions.txt"
            write_to_file(text_to_write="Caught new institution: " + pretty_json,
                          output_file_name=output_file_name)
            return pretty_json
        except Exception as e:
            e_message = "Institutions Catcher Exception 2: {0}: {1}".format("Error", str(e))
            print(e_message)
            return e_message
    if request.method == 'GET':
        return 'Hello, Institutions Catcher!'


def write_to_file(text_to_write, output_file_name):
    b = open(output_file_name, "a")
    b.write(text_to_write + '\n')
    b.close()


if __name__ == '__main__':
    app.run()
