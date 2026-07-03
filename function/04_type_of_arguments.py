def clean_name(f_name,l_name):
    clean_f_name=f_name.strip().lower()
    clean_l_name=l_name.strip().lower()
    full_name=clean_f_name+" " +clean_l_name
    print(full_name)
    # positional
clean_name("AkKIiiiII  ", " Priiiti ")
# keyword
clean_name(l_name="priiTIi", f_name="AAKKKIIIIii")

# Mix Arguments
clean_name(   "  MaiREaa" , l_name="akiii ")