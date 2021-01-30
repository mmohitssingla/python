def cough_dis(func):
    def function_wrapper():
        print('*cough*')
        func()
        print('*cough*')

    return function_wrapper


@cough_dis
def question():
    print("Can you give me discount on that?")


@cough_dis
def answer():
    print("No. I already gave you.")


question()
answer()
