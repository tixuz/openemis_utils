from pprint import pprint, pformat

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def catcher():
    try:
        method = request.method
        print(request.method)
    except Exception as e:
        e_message = "Catcher Exception 1: {0}: {1}".format("Error", str(e))
        print(e_message)
        return e_message
    if method == 'POST':
        try:
            request_json = request.json
            pprint(request_json)
            b = open("caught_webhooks.txt", "a")
            pretty_json = pformat(request_json)
            b.write(pretty_json + '\n')
            b.close()
            # return pretty_json
        except Exception as e:
            e_message = "Catcher Exception 2: {0}: {1}".format("Error", str(e))
            print(e_message)
            # return e_message
        try:
            request_form = request.form.to_dict()
            pprint(request_form)
            b = open("caught_webhooks.txt", "a")
            pretty_form = pformat(request_form)
            b.write(pretty_form + '\n')
            b.close()
        except Exception as e:
            e_message = "Catcher Exception 3: {0}: {1}".format("Error", str(e))
            print(e_message)
        try:
            request_form = request.values.to_dict()
            pprint(request_form)
            b = open("caught_webhooks.txt", "a")
            pretty_form = pformat(request_form)
            b.write(pretty_form + '\n')
            b.close()
            return request_form
        except Exception as e:
            e_message = "Catcher Exception 3: {0}: {1}".format("Error", str(e))
            print(e_message)
            return e_message

    if request.method == 'GET':
        return 'Hello, Catcher!'


if __name__ == '__main__':
    app.run()
