import sys
import os
import shutil
import time
"""
COMMAND NAME      :  less
DESCRIPTION       :  To display a file in a page at a time.
PARAMETERS        :  file
"""
def less(filename):

        file_path=os.getcwd()

        f1=file_path+'/'+filename
        sum=2
        if os.path.isfile(filename):
                print filename
                with open(f1) as f:
                        for line_terminated in f:
                                if sum%2==0:
                                        line = line_terminated.rstrip('\n')
                                        sum=sum+1
                                        print line
                                else:
                                        raw_input()
										sum=sum+1
                                        continue
