def print_statement(kwargs):
  if kwargs is None:
    print("Hello World")
  else:
    print(kwargs)

def main(kwargs):
  print_statement(kwargs)

if __name__ == "__main__":
  main(None)
