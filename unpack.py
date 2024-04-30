#! python3.7
# =================================================================================================
# Rivision History:
# Date          By              Ext.    Version         Revision History
# -------------------------------------------------------------------------------------------------
# 2024.03.06    John She        xx    First           Unpack WorkStation file pack2pc.tar.gz.uu
# =================================================================================================
import uu
import os
import tarfile
from datetime import datetime
import time

start_T = time.time()
date = datetime.now()
date_format = date.strftime("%y%m%d_%H%M")
# print(date_format)

decode_file = "pack2pc.tar.gz"

# remove xx.tar.gz which will conlflict old uu.decode result
try:
    os.remove(decode_file)
except:
    print("[Warn] Not able to remove old decode file")

try:
	uu.decode(decode_file + ".uu")
except:
    print("[Warn] Not able to decode uuencoded file")

# open file
file = tarfile.open(decode_file)

# extracting file
file.extractall("./" + date_format)

file.close()
end_T = time.time()

print("End of unpack.py, time usage: %s seconds" % (end_T - start_T))
input("Press Enter to continue ...")
