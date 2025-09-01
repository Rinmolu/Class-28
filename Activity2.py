class employee:
    def __init__(self):
        print("Employee Created.")
    def __del__(self):
        print("Destructer Called.")
def createobject():
    print("Making Object...")
    object = employee()
    print("Function End...")
    return object
print("Calling Create Object Function.")
object1 = createobject()
print("Programme End.")

