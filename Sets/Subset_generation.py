def print_subsets(actualset):
  set_generator([],actualset,0)

def set_generator(anotherset,actualset, iterator):
  if iterator == len(actualset):
    print(anotherset)
  else:
    set_generator(anotherset,actualset,iterator+1)
    set_generator(anotherset+ [actualset[iterator]],actualset,iterator+1)