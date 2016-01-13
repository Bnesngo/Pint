r'''
The lexical format for my language, written in regex.
'''
[ \
"(.)* (+,-,*,/) (.)*": 'var_assign', \ #variable assignment
"(.)*\( ((.)*,)*),(.)* \)": 'func_call'] #function calls

#This is just a rudimentary implement. Will add more syntax later.
