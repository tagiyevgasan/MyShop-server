def dekor_maker(slovo):
    def my_dekor(my_fn):

        def wrapper(x):
            print(f'vozvedi v stepen {slovo}: ')
            my_fn(x)
            
        return wrapper
    return my_dekor

@dekor_maker('pojaluysta')
def my_fn(x):
    print(x**2)


my_fn(4)
