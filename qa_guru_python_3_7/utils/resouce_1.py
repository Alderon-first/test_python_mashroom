import os


def path_file(name_file):
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__),  os.path.pardir, os.path.pardir, "resource/текст_1920-1080.jpg"))


print(os.path.abspath(
        os.path.join(os.path.dirname(__file__),  os.path.pardir, os.path.pardir, "resource/текст_1920-1080.jpg")))
print(os.path.join(os.path.dirname(__file__),  os.path.pardir,  "resource/текст_1920-1080.jpg"))
print(os.path.join(os.path.dirname(__file__),  "resource/текст_1920-1080.jpg"))

print(qa_guru_python_3_7.utils.resouce_1.path_file('resource/текст_1920-1080.jpg'))
print(tests_demoqa.resouce.path_file('resource/текст_1920-1080.jpg'))