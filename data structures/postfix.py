from stack import Stack

def postfix(expression):
	operators = '+-/*'
	
	expressionStack = Stack()
	expressionList = expression.split(' ')
	
	for expressionItem in expressionList:
		if expressionItem not in operators:
			expressionStack.push(expressionItem)
		else:
			operator = expressionItem
			
			endExpression = expressionStack.pop()
			beginExpression = expressionStack.pop()
			
			evaluatedExpression = eval('{0} {1} {2}'.format(beginExpression, operator, endExpression))
			expressionStack.push(str(evaluatedExpression))
			
	return expressionStack.top()

expression = '6 22 6 + *'
print(postfix(expression))

