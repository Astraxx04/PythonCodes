def operation(a,b,operator):
  if operator=="+":
    return a+b
  if operator=="-":
    return a-b
  if operator=="*":
    return a*b
  if operator=="/":
    return a/b
  if operator=="**":
    return a**b

def EvaluateExpression(exp):
    exp_new=exp.split(" ")
    stack=[]
    for e in exp_new:
        if e.isnumeric():
            stack.append(float(e))
        else:
            b=stack.pop()
            a=stack.pop()
            stack.append(operation(a,b,e))
    return stack[0]
print(float(EvaluateExpression(input())))
print(float(EvaluateExpression(input())))