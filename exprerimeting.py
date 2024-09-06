import numpy as np
import colorama

# colorama.init(autoreset=True)
color1 = colorama.Fore.WHITE + colorama.Style.BRIGHT + colorama.Back.BLACK
color2 = colorama.Fore.RED + colorama.Style.BRIGHT + colorama.Back.RESET

arr = np.zeros((3,3), dtype='int')
print(color1 + "Created The Numpy Array --> ")
print(color2,arr)

arr2 = np.full((3,3),'^',dtype='str')
print(color1 + "The Full Array --> ")
print(color2,arr2)

arr3 = np.ones((3,3), dtype='int')
print(color1 + "The Ones Array --> ")
print(color2,arr3)