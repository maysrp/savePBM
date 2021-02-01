from PIL import Image
from pathlib import Path
import sys

def savePBM(filename,x=128,y=64):
    e=Path(filename)
    if e.is_file:
        if e.suffix.upper() in [".JPG",".JPEG",".PNG",".BMP",".GIF"]:
            f=Image.open(filename)
            f=f.resize((x,y))
            l=f.convert('1')
            # l.show()
            pbm=e.stem+".pbm"
            l.save(pbm,"PPM")
            print(pbm," size:",Path(pbm).stat().st_size,"bytes")
            return True
        else:
            print("请导入图片文件！")
    else:
        print("文件不存在")
    return False


# savePBM("b.jpg")
if __name__=="__main__":
    # savePBM(sys.argv[1])
    if len(sys.argv)==2:
       savePBM(sys.argv[1])
    elif len(sys.argv)==4:
        try:
            x=int(sys.argv[2])
            y=int(sys.argv[3])
            savePBM(sys.argv[1],x,y)
        except Exception as e:
            savePBM(sys.argv[1])
