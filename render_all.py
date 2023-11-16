import os

for i in os.listdir():
    os.system(f'./rife-ncnn-vulkan -m {i} -0 0.png -1 2.png -o {i}/1.png')
    os.system(f'cp *.png {i}/')

