from tlang import lex

lexer = lex.Lexer(r"./test.t")
print(lexer.fc)
for i in lexer.get_tokens():
    print(i)