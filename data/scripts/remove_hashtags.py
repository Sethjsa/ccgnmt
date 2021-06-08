tags = []
with open("corpus.tc.en", "r") as f, open("corpus.en","w") as g:
    d = f.read()
    d = d.replace("#", "")
    g.write(d)
    #with open("output_1M.en", "r") as g:
     #   with open("output_1M_proc.en", "w") as h:
      #      output = g.readlines()
       #     for count, line in enumerate(f):
        #        if line.split()[0] == "#":
         #           h.write("\n")
          #      else:
           #         h.write(output[count])

                    


