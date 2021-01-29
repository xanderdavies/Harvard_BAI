import pickle
import pathlib
current_path = pathlib.Path(__file__).parent.absolute()

print('Loaders are being loaded from: %s'%current_path)
# from loader.multi_attribute_loader_file_list import FileListFolder as multi_attribute_loader_file_list


def get_loader(name):
    """get_loader
    :param name:
    """
    print('Dummy code for loader in place')
#     return {
#         "multi_attribute_loader_file_list" : multi_attribute_loader_file_list
#     }[name]