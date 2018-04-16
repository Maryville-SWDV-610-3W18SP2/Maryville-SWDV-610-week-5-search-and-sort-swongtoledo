''' From my research I found https://edhenry.github.io/2016/12/21/Hashing-in-Python/ and tested with my own list of calendar months'''


def rehash(oldhash, table_size):
    return (oldhash+1) % table_size

def weighted_ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + (ord(string[position]) * position)
    return hash_val % table_size


def lp_hash(item_list, table_size):
    
    lp_hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])
    
    for item in item_list:
        i = weighted_ord_hash(item, table_size)
        print("%s hashed == %s \n" %(item, i))
        if lp_hash_table[i] == None:
            lp_hash_table[i] = item
        elif lp_hash_table[i] != None:
            print("Collision, attempting linear probe \n")
            next_slot = rehash(i, table_size)
            print("Setting next slot to %s \n" % next_slot)
            while lp_hash_table[next_slot] != None:
                next_slot = rehash(next_slot, len(lp_hash_table.keys()))
                print("Next slot was not empty, trying next slot %s \n" % next_slot)
            if lp_hash_table[next_slot] == None:
                lp_hash_table[next_slot] = item
    return lp_hash_table



def main():
    items = ["Jan", "Feb", "March", 
             "April", "May", "June",
            "July", "Aug", "Sept","Oct","Nov","Dec"]
    print(lp_hash(items, 15))
    
main()
