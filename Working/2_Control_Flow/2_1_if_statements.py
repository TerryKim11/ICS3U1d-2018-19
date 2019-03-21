def cigar_party(cigars, is_weekend):
    if is_weekend:
        print(True)
    else:
        if 40 <= cigars <= 60:
            print(True)
        else:
            print(False)

cigar_party(70, False)