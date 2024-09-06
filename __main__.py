import numpy as np
import colorama
from colorama import Fore, Style, Back

colorama.init(autoreset=True)
color = colorama.Fore.WHITE + colorama.Style.BRIGHT + colorama.Back.BLACK

arr = arr = np.array([[1,2,3],[4,5,6]],dtype='int')

oprations = {
    1 : {
        "name" : "Create The Numpy Array",
        "title" : color + "Array --> ",
        "value" : f"{arr}"
    },
    2 : {
        "name" : "Print Dimention Of Array",
        "title" : color + "Dimention Of Array --> ",
        "value" : f"{arr.ndim}"  
    },
    3 : {
        "name" : "Shape Of Arra",
        "title" : color + "Shape Of Array --> ",
        "value" : f"{arr.shape}"
    },
    4 : {
        "name" : "Size Of Array",
        "title" : color + "Size Of Array --> ",
        "value" : f"{arr.size}"
    },
    5 : {
        "name" : "Type Of Array",
        "title" : color + "Type Of Array --> ",
        "value" : f"{arr.dtype}"
    },
    6 : {
        "name" : "Item Size Of Array",
        "title" : color + "Item Size Of Array --> ",
        "value" : f"{arr.itemsize}"
    },
    7 : {
        "name" : "Data Type Of Array",
        "title" : color + "Data Type Of Array --> ",
        "value" : f"{arr.dtype}"
    },
    8 : {
        "name" : "Total Bytes Of Array",
        "title" : color + "Total Bytes Of Array --> ",
        "value" : f"{arr.nbytes}"
    },
    9 : {
        "name" : "Memory View Of Array",
        "title" : color + "Memory View Of Array --> ",
        "value" : f"{arr.data}"
    },
    10 : {
        "name" : "Get Specific Row",
        "title" : color + "Get Specific Row --> ",
        "value" : f"{arr[1]}"
    },
    11 : {
        "name" : "Get Specific Column",
        "title" : color + "Get Specific Column --> ",
        "value" : f"{arr[:,1]}"
    }
}

def print_oprations():
    for i in oprations:
        print(oprations[i]["title"])
        print(oprations[i]["value"])

try:
    print_oprations()
except Exception as e:
    # To Print The Error
    print("Erro While Running :",e)