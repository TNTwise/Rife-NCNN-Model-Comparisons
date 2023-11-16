import os

for i in os.listdir():
    try:
        os.system(f'./rife-ncnn-vulkan -m {i} -0 0.png -1 2.png -o {i}/1.png')
        os.system(f'cp *.png {i}/')
        with open(f'{i}/README.md','w')as f:
            f.write(f'![{i}](1.png)')
    except:
        print("Not a model")
