import os
import random
import shutil

src = "../data"
dst = "../datasets/test"

test_len = int((8762 - 8153 + 1) * 0.2)

randomlist = []
for i in range(0,test_len):
  n = random.randint(8153,8762)
  if n in randomlist:
    i = i - 1
  else:
  	randomlist.append(n)
#print(randomlist)

for i in randomlist:
	if os.path.isfile(src + f"/IMG_{i}.JPG") and os.path.isfile(src + f"/IMG_{i}.xml"):
		shutil.move(src + f"/IMG_{i}.JPG", dst)
		shutil.move(src + f"/IMG_{i}.xml", dst)
	else:
		print(f"file {i} does not exist")
