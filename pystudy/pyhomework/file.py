import os
import sys
def main():
    input1 = input("Pls enter a source file:").strip()
    output = input("Pls enter a target file:").strip()

    if os.path.isfile(output):
        print(output + " already exists")
        sys.exit()

    infile = open(input1, "rb")
    outfile = open(output, "wb")
    
    l = infile.read()
#    print(l)
    encode = eval(input("加密请输入0，解码请输入1:"))
    if encode == 0:
        for byte in l:
            byte += 5
            byte %= 256
            outfile.write(bytes([byte]))
    elif encode == 1:
        for byte in l:
            byte -= 5
            if byte < 0:
                byte += 256
            outfile.write(bytes([byte]))
    else :
        print("你的输入有误，已退出")
        return
    print("操作成功，已退出。输出文件保存至：", output)
    infile.close()
    outfile.close()

main()
