def finder(x):
    while True:
        input_text = yield
        if x in input_text:
            print(input_text)


f = finder('python')
f.send(None)  # priming the coroutine 1. send none, 2. call next
f.send('some text including python')
f.send('elves are happy')
f.send('that python bucket')
f.send('crispy chicken')
f.close()
