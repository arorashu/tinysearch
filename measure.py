# measure time taken to do search with particular method

import time
import os
import sys

if len(sys.argv) > 2:
    if sys.argv[1] == "grep":
        search_term = sys.argv[2]
        file_search_pattern = " data/guten_2003/ "
        if len(search_term) < 20: # just a sanity check
            sys_command = 'grep -R --include="*.txt" ' + search_term + file_search_pattern +  " >/dev/null"
            print(f"running: {sys_command}" )
            start = time.time()
            os.system(sys_command)
            end = time.time()
            print(f"time taken: {round(end-start, 6)}s")
        else:
            print("search query too long!")
    else:
        print("search method not supported")

else:
    print(f"Args not correct!: {sys.argv}")

            

