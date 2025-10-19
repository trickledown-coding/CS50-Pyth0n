import inflect


while True:
    try:
        p = inflect.engine()
        adieu_list = []
        names = input("Who are we saying goodbye to: ")
        adieu_list.append(names)
        p.join(adieu_list,final_sep="")
    except EOFError:
        break