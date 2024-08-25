import zipfile as zip

class Unzip:
    def __init__(self,pathDecompress):
           self.pathDecompress= pathDecompress

    def decompress(self, namesZips):
        
        if len(namesZips) <=1:
            self.nameZips=namesZips[1]
        else:
            self.nameZips =list(namesZips)
        pathUnzip = self.pathDecompress
        if (ruta != null) :
            pathZip = f'{ruta}{name}'
            for name in namesZips:
                zipStructure= zip.ZipFile(pathZip)
                pipeFile = zipStructure.infolist()[0].filename
                fileName = pipeFile[:-1]
                with zip.ZipFile(pathZip,'r') as zp:
                    zp.extractall(pathUnzip)
                    print(f'Archivo se descomprimio {name}')
                newFileName= os.join(pathUnzip , name)
                os.name(f'{pathUnzip}/{fileName}',newFileName)

