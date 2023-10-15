import os
filelist = []
folder= list(os.listdir())
for i in range(len(folder)):
    try:
        if not os.listdir(folder[i]):
            os.rmdir(folder[i])
    except NotADirectoryError:
        continue
    except PermissionError:
        continue
print(" Все пустые папки удалены")   



        

    