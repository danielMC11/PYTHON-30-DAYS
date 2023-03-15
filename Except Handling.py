
# Execute except
"""
try:
    mydict = {'one': 1, 'two': 2, 'three': 3}
    for i, j, k in mydict.items():
        print(i, j, k)
except:
    print('Something went wrong')
"""
# Execute try and else
"""
try:
    mydict = {'one': 1, 'two': 2, 'three': 3}
    for i, j in mydict.items():
        print(i, j)
except:
    print('Something went wrong')
else:
    print('All good')
"""
# Execute try, else and finally ( works )
"""
try:
    mydict = {'one': 1, 'two': 2, 'three': 3}
    for i, j in mydict.items():
        print(i, j)
except:
    print('Something went wrong')
else:
    print('All good')
finally:
    print('Period')
"""
#Execute except and finally ( Does not work )
""""
try:
    mydict = {'one': 1, 'two': 2, 'three': 3}
    for i, j, k in mydict.items():
        print(i, j, k)
except:
    print('Something went wrong')
else:
    print('All good')
finally:
    print('Period')
"""
#Execute Except TypeError
"""
try:
    var = 1 + '2'      # first error to occur
    print(variable)
except SyntaxError:
    print('SyntaxError occur')
except TypeError:
    print('TypeError occur')
except ValueError:
    print('ValueError occur')
except NameError:
    print('NameError occur')
"""
#Execute de Python Error adn type of Error
"""
try:
    print(numbers)
except Exception as error:
    print(f'Error: {error} ', f'Type of Error: {type(error)}', sep='\n')
"""



