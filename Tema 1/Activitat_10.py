llista = [1, 5, 4, 6, 8, 11, 3, 12]

llista_pars = list(filter(lambda x:x%2==0, llista))
llista_impars = list(filter(lambda x:x%2==1, llista))

print(llista_pars)
print(llista_impars)